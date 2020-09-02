print("ATM Game")
pin=int(input("Please Create Your PIN : "))
a=int(input("Please Enter Your PIN : "))
if (a==pin):
    print("Welcome to MFB")
    amount=int(input("Please Enter Your Amount : "))
    print("Select Your Option : ")
    print("1.Balance Enquiry")
    print("2.Cash Withdrawal")
    print("3.Cash Deposit")
    print("4.Cash Transfer")
    print("5.Cancel")
    option=int(input())
    if (option == 1):
        print(f"Your Avl Bal is {amount}")
        print("Thank You For Choosing MFB ")
    if (option == 2):
        amwth=int(input("Amount You Want To WithDraw : "))
        if (amwth>=amount):
            print("Sorry, Your Running With Low BAL  ")
        else:
            print("Please Collect The Cash")
            b=int(amount)-int(amwth)
            print(f"Your Avl Bal is {b}")
            print("Thank You For Choosing MFB")
    if (option==3):
        amd=int(input("Amount You Want To Deposit : "))
        c=int(amount) + int(amd)
        print(f"Your Current Avl Bal is {c}")
        print("Thank You For Choosing MFB")
    if (option==4):
        name=input("Enter ACC Holder Name : ")
        numb=input("Enter ACC Number : ")
        e=len(numb)
        d='X'*e
        print(f"Amount You Want To Transfer to Mr.{name} Acc no {d}")
        amtt=int(input())
        if (amtt>=amount):
            print("Sorry, Your Running With Low BAL ")
        else:
            print(f"Transaction Successful Cash Transferred To Mr.{name} Acc no {d}")
            f=int(amount)-int(amtt)
            print(f"Your Avl Bal Is {f}")
            print("Thank You For Choosing MFB")
    if (option==5):
        print("Thanks For Fucking My time MFB.")

else:
    print("oops,your PIN is wrong")
