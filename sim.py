stuff = 0
print("Type in the length of your password:")
passwordlength = input()
stuff = 70 ** float(passwordlength)
print("It would take ", str(stuff), " combinations to crack that password!")
