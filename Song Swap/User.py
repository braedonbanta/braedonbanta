class User: 
    # class made by Logan Mebane
    """Class representing a user, storing their individual information"""
    def __init__(self, username: str, email: str, password: str, spotify: str, genres: list, mood_values: dict):
        self.username = username
        self.email = email
        self.password = password
        self.spotify = spotify
        self.genres = genres
        self.mood_values = mood_values

    def genre_update(self, genre):
        """Updates the genres associated with a User"""
        self.genres = genre

    def mood_update(self, mood):
        """Update the genres associated with a User"""
        self.mood_values = mood

    def print_user_details(user):
        # Method made by Griffin
        """Prints the details of a user"""
        print(f"Username:", user.username, f"email:", user.email, f"password:", user.password, f"spotify:",
              user.spotify, f"genres:", user.genres, f"mood values:", user.mood_values)







# Sample code done by: Griffin Kudla
# userList = []
# user1 = User(username="john_doe", email="john@example.com", password="password123", spotify="john_spotify", genres=[], mood_values=[])
# user2 = User(username="jane_smith", email="jane@example.com", password="securepass", spotify="jane_spotify", taste_value=8)
# user3 = User(username="bob_ross", email="bob@example.com", password="happytrees", spotify="bob_spotify", taste_value=5)
#
# userList.append(user1)
# userList.append(user2)
# userList.append(user3)
#
# # Adding additional users to test done by: Carson Spitler
# user4 = User(username="testuser4", email="testuser4@ex.com", password="testpassword4", spotify="testuser4", taste_value=2)
# user5 = User(username="testuser5", email="testuser5@ex.com", password="testpassword5", spotify="testuser5", taste_value=4)
# user6 = User(username="testuser6", email="testuser6@ex.com", password="testpassword6", spotify="testuser6", taste_value=0)
#
# userList.append(user4)
# userList.append(user5)
# userList.append(user6)
#
#
# # Accessing and printing the attributes of the created instances
# for user in userList:
#     user.print_user_details()

