triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle[1] = [item + triangle[0][0] for item in triangle[1]]
for i in range(2,len(triangle)):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] += triangle[i-1][0]
        elif j == len(triangle[i])-1:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j])

print(triangle)