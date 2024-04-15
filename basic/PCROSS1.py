def pattern(m,n,c1,c2):
    for i in range(m):
        for j in range(n):
            if i==c1-1 or j==c2-1:
                print("*",end="")
            else:
                print(".",end="")
        print("")
def main():
    t = int(input())
    for i in range(t):
        m,n,c1,c2 = map(int, input().split())
        pattern(m,n,c1,c2)
        print("")
main()