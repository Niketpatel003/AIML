a=int(input("Enter base value:"))
b=int(input("Enter how much times:"))
i=0
for i in range(b):
    a=a+(a/10)
print(a)