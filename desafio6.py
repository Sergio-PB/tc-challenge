columns = int(input())
heights = [int(i) for i in input().split(' ')]

leftMax = [1]*columns
rightMax = [1]*columns
for i in range(columns-1):
    leftMax[i+1] = min(leftMax[i]+1, heights[i+1])
    rightMax[columns-2-i] = min(heights[columns-2-i], rightMax[columns-1-i]+1)

heightsMax = [min(l, r) for l, r in zip(leftMax, rightMax)]
print(max(heightsMax))
