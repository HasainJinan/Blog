#Question
print("Do you like apples or bananas?")

#Answer field.
choice = input("Enter preference: ")

#Function to evaluate choice.
def choice_eval():

    #If choice is "Banana," print "Banana."
    if choice == "Banana":
        print("Banana")

    #If choice is "Apple," print "Apple."
    elif choice == "Apple":
        print("Apple")

    #If choice is neither "Banana" nor "Apple," print "Boring."
    else:
        print("Boring")

#Calling eval function.
choice_eval()