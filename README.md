# Dating_App
To design a feature that helps users find potential matches based on hobbies, we can use a simple algorithm that calculates the compatibility score between users based on their shared hobbies.
Lets say we have 3 other users in the app with following hobbies:
[
  {
    "id": 2,
    "name": "Pari Singh",
    "hobbies": [
      "Music",
      "Cooking",
      "Reading"
    ]
  },
  {
    "id": 3,
    "name": "Naina Patel",
    "hobbies": [
      "Music",
      "Chess",
      "Dance"
    ]
  },
{
    "id": 4,
    "name": "Amy Bhatt",
    "hobbies": [
      "Cooking"
    ]
  }
]
### API Request


`GET /match/{user_id}`

Then response shoul be
[
  {
    "id": 3,
    "name": "Naina Patel",
    "hobbies": [
      "Music",
      "Chess",
      "Dance"
    ]
  },
  {
    "id": 2,
    "name": "Pari Singh",
    "hobbies": [
      "Music",
      "Cooking",
      "Reading"
    ]
  }
]

Explanation:

Meet (`id = 1`) has total 3 hobbies:

1. Music
2. Chess
3. Drawing

`Naina` is the first member, since she has 2 hobbies in common with `Meet`.

`Pari` is at second index, since she has 1 hobby in common with `Meet`.

`Amy` has no hobbies matching, hence she is excluded from the response.

You can use any language, framework, and any backend DB to store the data. Frontend is not required to develop, just backend service is enough.

1.Set up the Flask application and define the endpoint for the match API:
from flask import Flask, jsonify

app = Flask(__name__)

# Define endpoint for match API
@app.route('/match/<int:user_id>')
def get_potential_matches(user_id):
    # Get the user's hobbies from the database
    user_hobbies = get_user_hobbies(user_id)
    
    # Get all other users from the database
    all_users = get_all_users()
    
    # Calculate the compatibility score for each user
    matches = []
    for user in all_users:
        if user['id'] != user_id:  # Exclude the current user
            compatibility_score = calculate_compatibility(user_hobbies, user['hobbies'])
            matches.append({
                'id': user['id'],
                'name': user['name'],
                'hobbies': user['hobbies'],
                'compatibility_score': compatibility_score
            })
    
    # Sort the matches based on compatibility score in descending order
    matches = sorted(matches, key=lambda x: x['compatibility_score'], reverse=True)
    
    # Return the potential matches
    return jsonify(matches[:10])  # Return top 10 matches

# Run the Flask application
if __name__ == '__main__':
    app.run()
2.Implement the helper functions to retrieve data from the database:
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




