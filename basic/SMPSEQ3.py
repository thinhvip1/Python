# existNum = {} # dictionary
def ascList(list1, **existNum):
    for x in list1:
        if (existNum.get(str(x)) == None): # nếu x chưa tồn tại trong list2
            print(x,end=" ")

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))
existNum = {} # dictionary
for x in list2:
    existNum.update({str(x): True})
ascList(list1, **existNum)
# 5
# -2 -1 0 1 4
# 6
# -3 -2 -1 1 2 3