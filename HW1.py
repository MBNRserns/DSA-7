u=input("Enter a Sentance:   ")

v=["a","e","i","o","u","A","E","I","O","U"]

count=0

for i in u:
    if i in v:
        count=count+1

print("The number of vowels in the string is:  ",count)
