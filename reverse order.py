#input of number greater than 1
n= int(input("Enter the value of n: "))

#printthe numbers from n to 1
print ("numbers from {0} to {1} are:".format(n,1))

# loop to print numbers
for i in range(n,0,-1):
    print(i)