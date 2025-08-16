num=int(input("Enter an Integer Number: "))
i=1
while(num>0):
    num//=10
    i += 1

print("Number of Digits:", i-1)