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
'''E = {0,3,4,5,6,8};
N = {1,2,5,7,8,9};
print("union of E and N is",E|N)
print('intersection of N and E is' ,E & N)
print("difference of E and N is" ,E-N)'''

#check for prime number within a giving range
'''lower = int(input("enter your lower value:"))
upper = int(input("enter your upper value: "))
print("prime numbers between",lower, " and ", upper," is:")
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)'''



#day 6
#print from 0 to 10
'''i = 0
for i in range(0,11):
    print(i)'''




    # functions in python
def is_prime(number):
    if number <= 1:
        return False
    for factor in range(2,number):
        if number % factor == 0:
            return False
    return True
def print_prime(n):
    for number in range(5,60):
        if is_prime(number):
            print("%dis prime"%number)
print(is_prime(5))

