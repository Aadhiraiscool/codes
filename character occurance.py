#take input of a word
string=input("please enter your own word: ")

#take input of character
char=input("Please enter your own character: ")
i=0
count=0
#loop will to find the occurance of character
while(i<len(string)): #string opuration

    if (string[i]==char):
        i=i+1

#display the result
print("Total number of times", char,"has occured = ", count)