n = int(input("How many students in your class: "))  
for i in range(1, n + 1):
    print(f"\nEntering marks for Student {i}")
    subject1 = int(input("Enter Subject 1 marks: "))
    subject2 = int(input("Enter Subject 2 marks: "))
    subject3 = int(input("Enter Subject 3 marks: "))
    subject4 = int(input("Enter Subject 4 marks: "))
    subject5 = int(input("Enter Subject 5 marks: "))

    average = (subject1 + subject2 + subject3 + subject4 + subject5) / 5

    if average >= 75:
        print("Your grade is A")
    elif average >= 60:
        print("Your grade is B")
    elif average >= 45:
        print("Your grade is C")
    elif average >= 35:
        print("Your grade is S")
    else:
        print("You are fail.Better Luck Next Time")
    
        
