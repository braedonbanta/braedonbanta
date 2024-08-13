import random
# Imposter game guess the word
words = [["animals", "lion"], ["foods", "tacos"], ["celebrities", "zendaya"], ["places", "island"], ["animals", "seal"], ["animals", "dog"], ["animals", "elephant"], ["celebrities", "miley cyrus"], ["celebrities", "billie eilish"], ["celebrities", "johnny depp"], ["celebrities", "the rock"], ["celebrities", "robert downey jr."], ["celebrities", "barack obama"], ["celebrities", "jennifer lawrence"], ["celebrities", "leonardo dicaprio"], ["celebrities", "olivia rodriguez"], ["celebrities", "dolly parton"], ["foods", "pizza"], ["foods", "steak"], ["foods", "potato"], ["foods", "cheeseburger"], ["foods", "mac n cheese"], ["foods", "cake"], ["foods", "oreos"], ["foods", "pie"], ["foods", "ice cream"], ["foods", "goldfish"], ["animals", "cow"], ["animals", "pig"], ["animals", "peacock"], ["animals", "flamingo"], ["animals", "giraffe"], ["animals", "gorilla"], ["animals", "zebra"], ["animals", "fish"], ["places", "mountains"], ["places", "disney world"], ["places", "beach"], ["places", "swamp"], ["places", "africa"], ["places", "egypt"], ["places", "barnes n noble"], ["places", "america"], ["places", "canada"], ["places", "forest"], ["places", "river"], ["movies", "the lion king"], ["movies", "madea"], ["movies", "little mermaid"], ["movies", "finding nemo"], ["movies", "toy story"], ["movies", "the conjuring"], ["movies", "it"], ["movies", "the hunger games"], ["movies", "twilight"], ["movies", "the fault in our stars"], ["movies", "despicable me"], ["movies", "dune"], ["characters", "winnie the pooh"], ["characters", "nemo"], ["characters", "ariel"], ["characters", "cinderella"], ["characters", "mickey mouse"], ["characters", "spongebob"], ["characters", "patrick"], ["characters", "fishstick"], ["characters", "garfield"], ["characters", "cat in the hat"], ["characters", "peely"], ["characters", "meowscles"], ["characters", "mufasa"], ["characters", "the joker"], ["characters", "indiana jones"], ["characters", "yoda"], ["characters", "batman"], ["characters", "iron man"], ["characters", "optimus prime"], ["characters", "buzz lightyear"], ["characters", "woody"], ["characters", "bumblebee (transformers)"], ["foods", ""], ["foods", "doritos"], ["foods", "burger"], ["foods", "milkshake"], ["foods", "coffee"], ["foods", "poop (shit)"], ["animals", "worm"], ["animals", "ant"], ["animals", "human"], ["animals", "me"], ["celebrities", "Wendy Coble"], ["celebrities", "Logan Sawyer"], ["celebrities", "Braedon Banta"], ["celebrities", "Lebron James"], ["celebrities", "Kendrick Lamar"], ["celebrities", "Drake"], ["Companies", "Apple"],["Companies", "Microsoft"],
["Companies", "Google"],
["Companies", "Amazon"],
["Companies", "Facebook"],
["Companies", "Coca-Cola"],
["Companies", "Pepsi"],
["Companies", "Nike"],
["Companies", "Adidas"],
["Companies", "McDonald's"],
["Companies", "Starbucks"],
["Companies", "Disney"],
["Companies", "Walmart"],
["Companies", "Samsung"],
["Companies", "Toyota"],
["Companies", "Ford"],
["Companies", "Honda"],
["Companies", "Sony"],
["Companies", "Intel"],
["Companies", "IBM"],
["Hobbies", "Reading"],
["Hobbies", "Gardening"],
["Hobbies", "Painting"],
["Hobbies", "Cooking"],
["Hobbies", "Fishing"],
["Hobbies", "Hiking"],
["Hobbies", "Dancing"],
["Hobbies", "Photography"],
["Hobbies", "Writing"],
["Hobbies", "Knitting"],
["Hobbies", "Cycling"],
["Hobbies", "Running"],
["Hobbies", "Swimming"],
["Hobbies", "Singing"],
["Hobbies", "Drawing"],
["Hobbies", "Sewing"],
["Hobbies", "Yoga"],
["Hobbies", "Camping"],
["Hobbies", "Surfing"],
["Hobbies", "Skating"],
["Household Items", "Chair"],
["Household Items", "Table"],
["Household Items", "Sofa"],
["Household Items", "Bed"],
["Household Items", "Lamp"],
["Household Items", "Refrigerator"],
["Household Items", "Oven"],
["Household Items", "Microwave"],
["Household Items", "Toaster"],
["Household Items", "Television"],
["Household Items", "Vacuum"],
["Household Items", "Broom"],
["Household Items", "Clock"],
["Household Items", "Mirror"],
["Household Items", "Shower"],
["Household Items", "Toilet"],
["Household Items", "Sink"],
["Household Items", "Bathtub"],
["Household Items", "Desk"],
["Household Items", "Fan"],
["Vehicles", "Car"],
["Vehicles", "Bicycle"],
["Vehicles", "Motorcycle"],
["Vehicles", "Bus"],
["Vehicles", "Train"],
["Vehicles", "Airplane"],
["Vehicles", "Boat"],
["Vehicles", "Truck"],
["Vehicles", "Scooter"],
["Vehicles", "Tractor"],
["Vehicles", "Taxi"],
["Vehicles", "Ambulance"],
["Vehicles", "Helicopter"],
["Vehicles", "Submarine"],
["Vehicles", "Skateboard"],
["Vehicles", "RV"],
["Vehicles", "Convertible"],
["Vehicles", "Minivan"],
["Vehicles", "SUV"],
["Types of Clothing", "Shirt"],
["Types of Clothing", "Pants"],
["Types of Clothing", "Skirt"],
["Types of Clothing", "Dress"],
["Types of Clothing", "Shoes"],
["Types of Clothing", "Hat"],
["Types of Clothing", "Gloves"],
["Types of Clothing", "Scarf"],
["Types of Clothing", "Jacket"],
["Types of Clothing", "Socks"],
["Types of Clothing", "Coat"],
["Types of Clothing", "Sweater"],
["Types of Clothing", "T-shirt"],
["Types of Clothing", "Shorts"],
["Types of Clothing", "Underwear"],
["Types of Clothing", "Belt"],
["Types of Clothing", "Blouse"],
["Types of Clothing", "Jeans"],
["Types of Clothing", "Boots"],
["Types of Clothing", "Tie"],
["States", "California"],
["States", "Texas"],
["States", "Florida"],
["States", "New York"],
["States", "Illinois"],
["States", "Pennsylvania"],
["States", "Ohio"],
["States", "Georgia"],
["States", "North Carolina"],
["States", "Michigan"]
]

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("starting game!")
while True:
    currentGroup = random.randint(0, len(words)-1)
    currentGroup = words[currentGroup]
    roles = [1, 0, 0]
    while roles is not None:
        input("Press enter to get your role and word") 
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        currentRole = random.randint(0, len(roles)-1)
        if roles[currentRole] == 1:
            print("You ARE "
                  "the imposter")
            print("The category is", currentGroup[0])
            print("You do not know the word")
            input("Press enter when you are ready to reset for next person")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            roles.pop(currentRole)
        else:
            print("You are NOT the imposter")
            print("The category is", currentGroup[0])
            print("The word is", currentGroup[1])
            input("Press enter to clear for the next person")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            roles.pop(currentRole)
    