#4.write a program for natural number based on user input
totalnum=int(input('Total number of numbers:'))
ls=[]
for i in range(0,totalnum):
    number=float(input())
    if number%1==0:
        ls.append(number)
print('Natural numbers from the following are:', ls)
