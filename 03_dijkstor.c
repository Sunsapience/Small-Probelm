/*
 * @Author: Wang LG
 * @Date: 2020-05-05 10:38:22
 * @LastEditTime: 2020-05-05 21:39:27
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /py_test_0/home/wlg/Documents/Code/Dijkstor/dijkstor.c
 */

#include <stdio.h>
#include <stdint.h>

#define GIGAN (1<<15)-1
#define N 6

// 输入
/*
v0: int ,源节点
D:  N * N 矩阵， D(i,j) 表示从第 i 个节点到第 j 个节点的距离
    两个节点不相邻时，距离为GIGAN
*/
struct Dijkstor_input{
    uint16_t v0;
    uint32_t D[N][N];
};

//输出
/*
dist: N * 1矩阵, 
	  dist[j]表示源节点到节点 j 的最短距离
previous：N * 1矩阵, 
		  previous[j],表示源节点到节点j在最短路径上，节点 j 的前一个节点，
          据此可得出完整路径 
*/
struct Dijkstor_result{
    uint32_t (*dist)[N];
    uint16_t (*previous)[N];
};

struct Dijkstor_result output;
uint32_t dist[N];
uint16_t previous[N];

void dijkstor(struct Dijkstor_input input){
	
	// 表示每个节点是否已计算最短距离
    uint8_t bool[N];

    uint16_t v0 = input.v0;   
    uint16_t i,j;
    
    uint32_t (*D)[N][N] = &(input.D);

    output.dist = &dist;
    output.previous = &previous;

	// 初始化
	// 找出和源节点相邻的节点
    for (i = 0; i < N; i++)
	{       
        dist[i] = (*D)[v0][i];
        bool[i] = 0;

        if (dist[i] == GIGAN)
		{
            previous[i] = -1;
        }
        else{
            previous[i] = v0;
        }
    }
    
	// v0到v0的距离为0
    dist[v0] = 0;
	v0到源节点的距离已计算
    bool[v0] = 1;

	// 计算剩余的 N-1 个节点
    for (i = 1; i < N; i++)
	{
        
        uint16_t mindist = GIGAN;
        uint16_t u = v0;
        
		// 找到当前还未计算的节点中距离 v0 最近的节点
        for (j = 0; j < N; j++)
		{
            if ((!bool[j]) && (dist[j] < mindist))
			{
                mindist = dist[j];
                u = j;
            }
        }

        bool[u] = 1;
		
		// 更新和节点 u 相邻节点的距离
        for (j = 0; j < N; j++)
		{
            if ((!bool[j]) && ((*D)[u][j] < GIGAN))
			{
                if (dist[j] > (*D)[u][j] + dist[u])
				{
                    dist[j] = (*D)[u][j] + dist[u];
                    previous[j] = u;
                }
            }
        }
    }
}

void main(void){

    uint16_t i,j;
    
    struct Dijkstor_input input = {
        .v0 = 0,
    };
    for (i=0;i<6;i++){
        for (j=0;j<6;j++){
            input.D[i][j] = GIGAN;
        }
    }
    input.D[0][1] = 6;
    input.D[0][2] = 3;
    input.D[1][2] = 2;
    input.D[1][3] = 5;
    input.D[2][3] = 3;
    input.D[2][4] = 4;
    input.D[3][4] = 2;
    input.D[3][5] = 3;
    input.D[4][5] = 5;
    for (i=0;i<6;i++){
        input.D[i][i] = 0;
        for (j=0;j<6;j++){
            input.D[j][i] = input.D[i][j];
        }
    }

    dijkstor(input);
    printf("--node:    distance:      previous:       \n");
    for (i=0;i<6;i++){
        printf("--%d\n",(*output.dist)[i]);
    // printf("       %d            %d               %u  \n",i,(*output.dist)[i],(*output.previous)[i]);
    }
}


