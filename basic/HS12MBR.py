def classifyObj(obj):
    if obj[0] == 'p':
        x1, y1 = map(int, obj[1:])
        return x1, y1, x1, y1
    if obj[0] == 'c':
        x1, y1, r = map(int, obj[1:])
        return x1-r, y1-r, x1+r, y1+r
    if obj[0] == 'l':
        x1, y1, x2, y2 = map(int, obj[1:])
        return min(x1,x2), min(y1,y2), max(x1,x2), max(y1,y2)
def minBoundRectangle(listObjects):
    min_x = min_y = float("inf")
    max_x = max_y = float("-inf")
    for obj in listObjects:
        x1, y1, x2, y2 = classifyObj(obj)
        min_x = min(min_x, x1)
        min_y = min(min_y, y1)
        max_x = max(max_x, x2)
        max_y = max(max_y, y2)
    print(min_x, min_y, max_x, max_y, sep=" ")
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        listObjects = []
        for j in range(n):
            obj = input().split()
            listObjects.append(obj)
        minBoundRectangle(listObjects)
        print("")
main()