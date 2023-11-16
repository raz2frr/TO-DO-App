categories = [
    ["School", [ "Do your math homework", "Study for your quiz" ] ],
    ["Health", [ "Do a 5 minute exeercise", "Do 50 jumping jacks. Damn Razia" ] ]
]

# This function display a congrats message
def displayCongrats():
    print("You won 10 points for completing the quest")





userAge = int(input("What is your age?: "))

if userAge < 10:
   print("Razia says: Sorry you're too young. Bye!!!!!!!")
else:
    print("Your account has been created successfully")
    print("Here are all the categories")
   
    index = 0
    for currentCategory in categories:
        print( f"{index + 1}. {currentCategory[0]}" )
        index += 1

    userCategory = int( input("Choose your category: "))
    userCategory = userCategory - 1

    print( f"{categories[ userCategory ][1][0]}" )

    userResponse = int(input("Your response?"))

    if userResponse == 1:
        displayCongrats()
    else:
        print("You won no points unfortunately for not completing the quest")




   

