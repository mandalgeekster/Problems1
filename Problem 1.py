
a=list(map(int,input().split(",")))
arr=[]
for i in a:
    if i>=35:
        arr.append("Pass")
    else:
        arr.append("Fail")
print(arr)
print("success")
