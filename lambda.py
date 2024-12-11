#For even numbers
list=[]

for i in range(0,101):  
    res= lambda i: i%2==0  
    if(res(i)==True):
        list.append(i)
print(list)

