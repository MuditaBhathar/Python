# Python
#Guvi python classes Project
t=int(input('total number:'))
list1=[]
list2=[]
for i in range(0,t):
    n=int(input())
    list1.append(n)
    f=0
    for i in range(2,n+1):
        if n%i==0:
            f=f+1
    if f==1:
        list2.append(n)
print(list1)
print(list2)
print(all(list2))
list2
