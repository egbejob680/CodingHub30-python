# day 1:  procedural
'''a = int(input("enter any value: "))
b = int(input("enter any value: "))
c = int(input("enter any value: "))
total = a + b + c
print("total is :",total)'''


# calculating area
'''pi = 3.14
r = int(input("enter radius: "))
area = pi * r**2
print("the area of a circle is: ",area)'''



# DAY 2:
'''a = int(input("enter A:"))
b = int(input("enter B: "))
if a > b:
    print( "A is the largest")
elif a < b:
    print("B is the largest")
else:
    print(f"both A and B are equal: {a} == {b}")'''


#day 3
'''num = int(input("displaying the multiplication table of: "))
for i in range(1,11):
    print(num,'x',i ,'=', num*i)'''

    #day4
    #set operation
E = {0,3,4,5,6,8};
N = {1,2,5,7,8,9};
print("union of E and N is",E|N)
print('intersection of N and E is' ,E & N)
print("difference of E and N is" ,E-N)