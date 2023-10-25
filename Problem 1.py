
x=list(map(int,input().split(",")))
arr=[]
for i in x:
    if i>=40:
        arr.append("Pass")
    else:
        arr.append("Fail")
print(arr)
print("finish")
