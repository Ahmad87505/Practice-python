x=int(input("Enter the Number: "))
match x:
    case 0:
        print("zero")
    case 4:
        print("Four")
    case _ if x!=90:
        print(x, "NOT 90")
    case _ if x!=80:
        print(x, "Not 80")
    case _:
        print(x)
        