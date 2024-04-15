def pattern(lines, columns, high, width):
    for i in range((high+1)*lines+1):
        for j in range((width+1)*columns+1):
            if (i % (high+1) == 0 or j % (width+1) == 0):
                print("*", end="")
            else:
                print(".", end="")
        print("")
t = int(input())
for i in range(t):
    lines, columns, high, width = map(int, input().split())
    pattern(lines, columns, high, width)
    print("")