from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

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
["States", "Michigan"]]


@app.route('/')
def home():
    if session.get('default_players') is not None:
        return render_template('index.html', default_players=session.get('default_players'), default_imposters=session.get('default_imposters'))
    else:
        return render_template('index.html')


@app.route('/select_game_mode', methods=['POST'])
def select_game_mode():
    num_players = int(request.form['num_players'])
    num_imposters = int(request.form['num_imposters'])
    session['default_players'] = num_players
    session['default_imposters'] = num_imposters

    session['roles'] = ([1] * num_imposters) + ([0] * (num_players - num_imposters))

    return redirect(url_for('normal_round'))

@app.route("/select_player_count", methods=['POST'])
def select_player_count():
    num_players = int(request.form['num_players'])
    num_imposters = int(request.form['num_imposters'])

    session['roles'] = ([1] * num_imposters) + ([0] * (num_players - num_imposters))

    category = request.form['category']
    word = request.form['word']
    session['current_category'] = category
    session['current_group'] = [category, word]
    return redirect(url_for('moderator_select'))


@app.route('/normal_round')
def normal_round():
    return render_template('normal_round.html')


@app.route('/pick_a_word', methods=['POST', 'GET'])
def pick_a_word():
    return render_template('pick_a_word.html')


@app.route('/select_category', methods=['POST'])
def select_category():
    category = request.form['category']
    available_words = [word for word in words if word[0].lower() == category.lower()]
    if not available_words:
        return "No words available for the selected category. Please select a different category."
    session['current_category'] = category
    session['current_group'] = random.choice(available_words)
    return redirect(url_for('get_role'))

@app.route('/moderator_select', methods=['POST', 'GET'])
def moderator_select():
    session['roles'] = session.get('roles')
    return redirect(url_for('get_role'))


@app.route('/get_role', methods=['POST', 'GET'])
def get_role():
    if 'roles' not in session or not session['roles']:
        return redirect(url_for('home'))

    current_group = session['current_group']
    roles = session['roles']
    current_role = random.choice(roles)
    roles.remove(current_role)
    session['roles'] = roles

    category, word = current_group
    roles_left = len(roles)
    return render_template('role.html', role=current_role, category=category, word=word, roles_left=roles_left)


@app.route('/reset_game', methods=['POST'])
def reset_game():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
