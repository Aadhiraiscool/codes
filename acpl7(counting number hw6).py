num = input("Enter a number: ")

if num.startswith('-'):
    num = num[1:]

if num.isdigit():
    count = 0
    i = 0
    while i < len(num):
        count += 1
        i += 1
    print("Total digits:", count)
else:
    print("Invalid input. Please enter a valid integer.")
