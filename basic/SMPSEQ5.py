def solve(list1, list2):
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            print(i+1, end=" ")
        i += 1
        j += 1

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))
solve(list1, list2)