def isConvex(points):
    last, tmp = 0, 0
    for i in range(2, len(points) + 3):
        p0, p1, p2 = points[(i - 2) % len(points)], points[(i - 1) % len(points)], points[i % len(points)]
        tmp = (p1[0]-p0[0])*(p2[1]-p0[1])-(p2[0]-p0[0])*(p1[1]-p0[1])
        if tmp:
            if last * tmp < 0:
                return False
            last = tmp
    return True
