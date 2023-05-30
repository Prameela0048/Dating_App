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



