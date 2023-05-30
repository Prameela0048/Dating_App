# Example data in memory, you can replace this with database queries

# Get the user's hobbies from the database
def get_user_hobbies(user_id):
    users_data = {
        1: {
            "id": 1,
            "name": "Meet",
            "hobbies": [
                "Music",
                "Chess",
                "Drawing"
            ]
        },
        2: {
            "id": 2,
            "name": "Pari Singh",
            "hobbies": [
                "Music",
                "Cooking",
                "Reading"
            ]
        },
        3: {
            "id": 3,
            "name": "Naina Patel",
            "hobbies": [
                "Music",
                "Chess",
                "Dance"
            ]
        },
        4: {
            "id": 4,
            "name": "Amy Bhatt",
            "hobbies": [
                "Cooking"
            ]
        }
    }
    return users_data[user_id]['hobbies']

# Get all other users from the database
def get_all_users():
    users_data = {
        2: {
            "id": 2,
            "name": "Pari Singh",
            "hobbies": [
                "Music",
                "Cooking",
                "Reading"
            ]
        },
        3: {
            "id": 3,
            "name": "Naina Patel",
            "hobbies": [
                "Music",
                "Chess",
                "Dance"
            ]
        },
        4: {
            "id": 4,
            "name": "Amy Bhatt",
            "hobbies": [
                "Cooking"
            ]
        }
    }
    return list(users_data.values())

# Calculate the compatibility score between two users based on shared hobbies
def calculate_compatibility(user1_hobbies, user2_hobbies):
    shared_hobbies = set(user1_hobbies) & set(user2_hobbies)
    return len(shared_hobbies)
