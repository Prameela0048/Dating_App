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
