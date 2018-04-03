import sys
import time
import random


account_balance = 1200000

def my_bkash():
    global account_balance
    global PIN
    print("bKash\n"
          "1. Check Balance\n"
          "2. request statement\n" 
          "3. Change Mobile Menu Pin\n" 
          "0. Main Menu")

    choice_input = int(input("Enter Your Choice\n"))
    if choice_input == 1:
        pin_input = int(input("Enter Your Pin\n"))
        if pin_input == PIN:
            print("Your account balance is {} tk.\n".format(account_balance))

    elif choice_input == 2:
        print("You will get a sms very soon. If failed, then call 16247.")

    elif choice_input == 3:
        pin_input = int(input("Enter Existing Pin Number\n"))
        if pin_input ==  PIN:
            new_pin_input = int(input("Enter Your New Pin\n"))
            PIN = new_pin_input
        else:
            print("Sorry Try Again Later\n")

    else:
        main_menu()
        choices()


# The main menu
def main_menu():
    print("1. Send money\n"
          "2. Buy airtime\n"
          "3. Payment\n"
          "4. Cash out\n"
          "5. Remitance\n"
          "6. My bkash\n"
          "7. Helpline\n")


print("Dial 247")
inp = input()
print("You have to set your PIN first.")
PIN = int(input())
if inp != '247':
    sys.exit("You don't dial the right number...")
else:
    main_menu()


# Choices for main menu
def choices():
    global PIN
    global account_balance

    choice_input = int(input("Enter your choice.\n"))
    if choice_input == 1:
        print("Enter reciver bkash account\n")
        acc_input = input()
        print("Enter amount to send")
        money_input = int(input())
        print("Enter reference")
        # Reference used for send money that is not used in code
        ref_input = int(input())
        print("Enter your PIN")
        pin_input = int(input())
        if pin_input == PIN:
            print("Send money {} successfullt to {} at {}, Referene is {}. \nYour current acchount balane is {}"
                  .format(money_input, acc_input, time.ctime(), ref_input, account_balance-money_input))
        else:
            sys.exit("PIN Number not matched.\nTry again later..")

    elif choice_input == 2:
        print("Select Operator\n")
        print("1. Grameenphone\n"
              "2. Banglalink\n"
              "3. Airtel\n"
              "4. Robi\n"
              "5. Teletalk\n"
              "0. Main Menu")
        operator_select = int(input())
        if operator_select == 1:
            print("Enter your number")
            number_input = input()
            if number_input[:3] != "017":
                sys.exit("Invalid operator.")
            else:
                print("Enter airtime amount.")
                amount_input = int(input())
                print("Enter PIN")
                pin_input = int(input())
                if pin_input != PIN:
                    sys.exit("Pin Number not matched.")
                else:
                    print("Airtime {} tk send to {} at {}, Your current account balance is {}"
                          .format(amount_input, number_input, time.ctime(), account_balance-amount_input))

        elif operator_select == 2:
            print("Enter your number")
            number_input = input()
            if number_input[:3] != "019":
                sys.exit("Invalid Operator")
            else:
                print("Enter airtime amount.")
                amount_input = int(input())
                print("Enter PIN")
                pin_input = int(input())
                if pin_input != PIN:
                    sys.exit("Pin Number not matched.")
                else:
                    print("Airtime {} tk send to {} at {}. Your current account balance is {}"
                          .format(amount_input, number_input, time.ctime(), account_balance-amount_input))

        elif operator_select == 3:
            number_input = input("Enter your number\n")
            if number_input[:3] != "016":
                sys.exit("Invalid Operator")
            else:
                amount_input = int(input("Enter airtime amount\n"))
                pin_input = int(input("Enter PIN"))
                if pin_input != PIN:
                    sys.exit("Pin number not matched.")
                else:
                    print("Airtime {} tk send to {} at {}. Your current account balance is {}"
                          .format(amount_input, number_input, time.ctime(), account_balance-amount_input))

        elif operator_select == 4:
            number_input = input("Enter your number\n")
            if number_input[:3] != "018":
                sys.exit("Invalid Operator")
            else:
                amount_input = int(input("Enter airtime amount\n"))
                pin_input = int(input("Enter PIN"))
                if pin_input != PIN:
                    sys.exit("Pin number not matched.")
                else:
                    print("Airtime {} tk sent to {} at {}. Your currentt account balance is {}"
                          .format(amount_input, number_input, time.ctime(), account_balance-amount_input))

        elif operator_select == 5:
            number_input = input("Enter your number\n")
            if number_input[:3] != "015":
                sys.exit("Invalid Operator")
            else:
                amount_input = int(input("Enter airtime amount\n"))
                pin_input = int(input("Enter PIN\n"))
                if pin_input != PIN:
                    sys.exit("Pin number not matched.")
                else:
                    print("Airtime {} tk send to {} at {}. Your current account balance is {}"
                          .format(amount_input, number_input, time.ctime(), account_balance-amount_input))
        else:
            main_menu()
            choices()

    elif choice_input == 3:
        print("Enter Marchant bKash Account No")
        number_input = input()
        money_input = int(input("Enter Amount\n"))
        print("Total amount {} tk payment has been done to {} at {}. Your current account balance is"
              .format(money_input, number_input, time.ctime(), account_balance-money_input))

    elif choice_input == 4:
        print("Cash out\n"
              "1. From agent\n"
              "2. From ATM\n"
              "0. Main menu")
        _inp = int(input("Enter your choice:\n"))
        if _inp == 1:
            number_input = input("Enter bKash agent number\n")
            money_input = int(input("Enter amount\n"))
            pin_input = int(input("Enter PIN\n"))
            if pin_input != PIN:
                sys.exit("Pin number not matched.")
            else:
                print("Cash out tk {} sucessfully to {} at {}.Your current account balance is {}.\nFor help call 16247."
                      .format(money_input, number_input, time.ctime(), account_balance-money_input))

        elif _inp == 2:
            atm_pin = random.randint(00000, 99999)
            print("Your ATM Pin is {}".format(atm_pin))
            pin = int(input("Enter Menu PIN to request ATM Cash Out:\n"))
            if pin != atm_pin:
                sys.exit("Pin Number Not Valid.")
            else:
                money_input = int(input("Enter Amount to Cash Out.\n"))
                print("Cash Out Sucessfull tk {} at {}. Your current account balance is {}"
                      .format(money_input, time.ctime(), account_balance-money_input))

    elif choice_input == 5:
        print("Remitance service not available right now....\n"
              "Thanks for being with us.\nCall 16247 for more information.\n")
        main_menu()

    elif choice_input == 6:
        my_bkash()

    elif choice_input == 7:
        print("Hlepline is 16247\n"
              "Do you want to call?\n"
              "1. Yes\n"
              "2. No\n"
              "0. Main Menu")
        help_input = int(input("Enter Your choice.\n"))
        if help_input == 1:
            print("Calling 16247....")
            time.sleep(2)
            print("Please wait...")
            for i in range(5):
                print("Connecting......")
                time.sleep(1)
            sys.exit("Can't connect the call. \nSystem is exiting.\nTry again later.")
        elif help_input == 2:
            sys.exit("The system is exiting....")
        else:
            main_menu()
    else:
        main_menu()


def cash_in():
    number_input = input("Enter account number\n")
    amount_input = int(input("Enter amount to cash in.\n"))
    global account_balance
    account_balance += amount_input
    print("Cash in {} tk from {}. Your current account balance is {}"
          .format(amount_input, number_input, account_balance))


choices()


if account_balance < 100000:
    cash_in()
else:
    choices()