#get input from user
#odd or even
u=int(input("Select a number:   "))

#Modulus operation (%) gives the remainder
if u %2 == 0:
    print("Your Number is Even")
else:
    print("Your Number is Odd")

for i in range(1001):
    print(i)