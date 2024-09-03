number = int(input("Enter a number : "))
exponent = int(input("Enter the power you want to raise the number to : "))

for i in range(1,exponent+ 1):
    product = number ** i
    print("The number " , number , " raised to the power of " , i ,"is ", product)