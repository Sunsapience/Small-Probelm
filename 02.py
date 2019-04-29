#判断一个图形是否和另一个图形相同

# 向量积
def cross_product(p0,p1,p2):
    # 顶点为p0,p1,p2为两边的点
    tmp = (p1[0]-p0[0])*(p2[1]-p0[1])-(p2[0]-p0[0])*(p1[1]-p0[1])
    return tmp

def Polygon_cross_product(points):
    result = []
    for i in range(0,len(points)):
        if i == len(points)-1:
            p0,p1,p2=points[i],points[i-1],points[0]
        else:
            p0,p1,p2=points[i],points[i-1],points[i+1]
        result.append(cross_product(p0,p1,p2))
    return result

def is_same(points_1,points_2):
    re_1 = Polygon_cross_product(points_1) 
    re_2 = Polygon_cross_product(points_2)*2

    for i in range(len(re_1)):
        if re_1 == re_2[i:i+len(re_1)]:
            return True
    return False
