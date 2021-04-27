list=['Rohan','Mohan','Rohit','rohan','ROhan','MOhhan','Rohan']
name=input("Enter a name to be saeched in the list")
count =0
for i in list:
    if(i==name):
        count+=1
if(count>0):
    print("{0} is present {1} times".format(name,count))