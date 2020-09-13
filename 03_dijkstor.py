'''
@Author: your name
@Date: 2020-05-05 10:38:22
@LastEditTime: 2020-05-05 12:59:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /py_test_0/home/wlg/Documents/Code/Dijkstor/dijkstor.py
'''

import numpy as np

'''
@description: Dijkstor 算法
@param:        
        v0: int ,源节点
        D:  numpy N * N 矩阵， D(i,j) 表示从第 i 个节点到第 j 个节点的距离
            两个节点不相邻时，距离为 10*sum(D)
        gigan: 表示无穷大，两个节点不相邻
@return: 
       dist: numpy N, dist[j]表示源节点到节点 j 的最短距离
       previous：numpy N, previous[j],
                表示源节点到节点j在最短路径上，节点 j 的前一个节点，
                据此可得出完整路径 
'''

def dijkstor(v0,D,gigan):

    N0, N1 = np.shape(D)
    if N0 != N1:
        print("距离矩阵必须是方阵")
        return 

    # 节点个数
    N = N0 
    # 无穷大，表示两个节点不相邻
    gigantic = gigan

    # 每个节点到源节点 v0 的最短距离  
    # dist[i]表示第i个节点到 第 v0 个节点的最短距离
    dist = np.zeros((N))
    # 每个节点是否已计算最短距离
    # is_calculate[i] = True 表示该节点已计算
    is_caculate = np.zeros((N), dtype=np.bool)
    # 每个计算在最短路径上的前一个节点
    # previous[i] = v0 表示该节点的前一个节点是 v0
    previous = np.zeros((N), dtype=np.int16)

    # 初始化
    # 找出和源节点相邻的节点
    for i in range(N):
        dist[i] = D[v0][i]
        if dist[i] == gigantic:
            previous[i] = -1
        else:
            previous[i] = v0
    
    # v0到v0的距离为0
    dist[v0] = 0
    # v0到源节点的距离已计算
    is_caculate[v0] = True

    # 计算剩余的 N-1 个节点
    for i in range(1,N):

        mindist = gigantic
        u = v0
        
        # 找到当前还未计算的节点中距离 v0 最近的节点
        for j in range(N):
            if ((not is_caculate[j]) and (dist[j] < mindist)):
                mindist = dist[j]
                u = j
        
        # 找到当前距离源节点最近的节点
        is_caculate[u] = True

        # 更新和节点 u 相邻节点的距离
        for j in range(N):
            if ((not is_caculate[j]) and (D[u][j] < gigantic)):
                if dist[j] > dist[u] + D[u][j]:
                    dist[j] = dist[u] + D[u][j]
                    previous[j] = u
    
    for ib in is_caculate:
        if not ib:
            print("存在未计算的节点")
            return 
    
    return dist, previous
        
'''
refer: https://blog.csdn.net/mu399/article/details/50903876
'''
test = [6,3,2,5,3,2,3,4,5]
gigan = 10*np.sum(np.array(test))

test_D = gigan*np.ones((6,6))
for i in range(6):
    test_D[i][i] = 0
test_D[0][1] = 6
test_D[0][2] = 3
test_D[1][2] = 2
test_D[1][3] = 5
test_D[2][3] = 3
test_D[2][4] = 4
test_D[3][4] = 2
test_D[3][5] = 3
test_D[4][5] = 5
for i in range(6):
    for j in range(6):
        test_D[j][i] = test_D[i][j]
re1 , re2 = dijkstor(0,test_D,gigan)
print(re1)
print(re2)