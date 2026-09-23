# 1.Write a program that prints "Hello, World!" to the console
print ("Hello, World!")


# 2.To find largest of three numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


# 3.Accept two numbers from the user and print their sum

num_1 = float(input("Enter your first number: "))
num_2 = float(input("Enter your second number: "))

sum = num_1 + num_2
print(sum)
