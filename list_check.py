list=[1,23,13,4,34,5373,8,4,732,41,3,54,43,64,674,1,4,4,858,465,96,4,65,74]
var=int(input("Enter a value to be searched "))
count=0
for i in list:
    if(i==var):
        count+=1
print("Number {0} occurs {1} times in the list".format(var,count))