def solve(list1, list2):
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            while list1[i] == list2[j]:
                print(list1[i], end=" ")
                i += 1
            # while list2[j] == list1[i-1]:
            #     print(list2[j], end=" ")
            #     j += 1
        elif list1[i] > list2[j]:
            j += 1
        else:
            i += 1
n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))
solve(list1, list2)
