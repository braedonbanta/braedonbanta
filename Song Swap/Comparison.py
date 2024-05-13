import sqlite3
import json
import Algorithm

def connect_to_database(database_name):
    '''Connects to the sqlite database and returns the connection object and cursor object'''
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print("Error connecting to the database:", e)
        return None, None

def get_current_user(username, cursor):
    '''Gets the genre and mood_values associated with the current user interacting with the app'''
    cursor.execute("SELECT genres, mood_values FROM User where username = ?", (username,))
    current_user = cursor.fetchone()
    return current_user

def get_users_data_except_current(username, cursor):
    '''Fetches all user data except the current user'''
    cursor.execute("SELECT username, genres, mood_values FROM User WHERE username != ?", (username,))
    return cursor.fetchall()

def main(username):
    """Performs the comparison of the current user against all users in the database, returning which users match with current user
    :param username: The username of the current user interacting with the app
    :return: List of users the current user matches with
    """
    database_name = 'songSwap.db'
    conn, cursor = connect_to_database(database_name)

    try:
        current_user = get_current_user(username, cursor)
        if current_user:
            genres1 = json.loads(current_user[0])
            mood1 = json.loads(current_user[1])
            # fetch the data of all users in the database EXCEPT current user
            all_users_data = get_users_data_except_current(username, cursor)
            if all_users_data:
                matched_users = []
                for user_data in all_users_data:
                    # this obtains the genres and mood of user 2 and converts it to appropriate data type
                    genres2 = json.loads(user_data[1])
                    mood2 = json.loads(user_data[2])
                    # compares the genres and mood values of the current user and other user in the database
                    if Algorithm.genre_comparison(genres1, genres2) and Algorithm.audio_feature_comparison(mood1, mood2):
                        matched_username = user_data[0]
                        matched_users.append(matched_username)  # Append username to matched_users if they match
                return matched_users
            else:
                return []
    finally:
        conn.close()

if __name__ == "__main__":
    main()