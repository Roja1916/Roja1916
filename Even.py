
min = int(input("Enter the number minimum number:"))
max = int(input("Enter the number maximum number:"))

# using for loop to print the even numbers
for num in range(min,max+1):
    if (num % 2 == 0):
        print("The even number are", "{0}".format(num))

