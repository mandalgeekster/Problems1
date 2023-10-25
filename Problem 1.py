
a=list(map(int,input().split(",")))
arr=[]
for i in a:
    if i>=30:
        arr.append("Pass")
    else:
        arr.append("Fail")
print(arr)
print("finish")
