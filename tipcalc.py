
print("How much was the total? ")
bill = float(input())

print("What percentage tip will you leave? (%) ")
percentage = int(input())


if percentage <= 20:
    print("Total before tip - $" + str(bill))
    tip_amount = "{:.2f}".format((bill * (percentage / 100)))
    print("Tip Amount - $" + tip_amount)
    total_bill = float(bill + (bill * percentage / 100))
    print("The total bill including tip - $" + "{:.2f}".format(total_bill))
    print("Thank you for using #insert app name#, have a great day!")

else:
    print("Are you sure this is the right amount? (yes/no): ")
    user_input = input()
    yes_choices = ['yes', 'y']
    no_choices = ['no', 'n']

    if user_input.lower() in no_choices:
        print("What percentage tip will you leave? (%) ")
        percentage = int(float(input()))
        print("Total before tip - $" + str(bill))
        tip_amount = "{:.2f}".format((bill * (percentage / 100)))
        print("Tip Amount - $" + tip_amount)
        total_bill = float(bill + (bill * percentage / 100))
        print("The total bill including tip - $" + "{:.2f}".format(total_bill))
        print("Thank you for using TipJar!")

    elif user_input.lower() in yes_choices:
        print("Total before tip - $" + str(bill))
        tip_amount = "{:.2f}".format((bill * (percentage / 100)))
        print("Tip Amount - $" + tip_amount)
        total_bill = float(bill + (bill * percentage / 100))
        print("The total bill including tip - $" + "{:.2f}".format(total_bill))
        print("Thank you for using TipJar!")