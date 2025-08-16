n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))
n3=int(input("Enter n3: "))
if n1 > n2 and n1 > n3:
   max= n1
elif n2 > n1 and n2 > n3:
    max= n2
else:
    max= n3
    print("The maximum number:", max)