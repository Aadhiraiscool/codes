#take input for the student that he can attend the exam or not 
medical_cause=input ("did yopu have a medical cause Y or N: ")
#take input of the attendance
atten=int(input("enter the attendance of the student:"))

#checking the user iput predecting output accordingly

if medical_cause == 'Y' or 'y': 
    print("you are allowed")
else:
    if atten>=75:
         print("allowed")
    else:
        print("not allowed")



