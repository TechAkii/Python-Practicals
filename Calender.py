print("Calendar 2025")
m = int(input("Enter a Month (1-12): "))


if m in (1, 3, 5, 7, 8, 10, 12):
    for i in range(1,32):
        print(f"{i:2}" , end=" ")
        if i%7==0:
            print("\n")

elif m==2:
    for i in range(1,29):
        print(f"{i:2}" , end=" ")
        if i%7==0:
            print("\n")

elif  m in (4, 6, 9, 11):
    for i in range(1,31):
        print(f"{i:2}" , end=" ")
        if i%7==0:
            print("\n")

else:
    print("Invaild Month")
    