"""Pass mark calculator: Get input as string with comma seperated numbers denoting marks of list of 
                      students in class room. Print the array containing Pass/Fail respective to the input marks.
                      Consider 35 and above are pass marks.
Sample input: 20,46,75,10
Sample output: Fail, Pass, Pass, Faila"""

a=list(map(int,input().split(",")))
arr=[]
for i in a:
    if i>=35:
        arr.append("Pass")
    else:
        arr.append("Fail")
print(arr)
print("Finsh")