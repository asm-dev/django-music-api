# Django Music API Server

This project is a RESTful API built with Django that integrates the Spotify API. The server lets you manage users, songs and their music preferences, making it possible to mark songs as favorites.

&nbsp;

## Installation and setup

1. Clone the repository.
2. Create a virtual environment (if you don't have one yet). I recommend Anaconda:

```
conda create --name django-spotify-api python=3.9
conda activate django-spotify-api
```

3. Install the dependencies `pip install -r requirements.txt`
4. Create a `.env` file and add your Spotify credentials:

```
SPOTIFY_CLIENT_ID=tu_client_id
SPOTIFY_CLIENT_SECRET=tu_client_secret

```

5. Apply the database migrations: `python manage.py migrate`
6. Create a superuser to access the Django admin panel: `python manage.py createsuperuser`
7. Start the server: `python manage.py runserver`
8. Have fun trying out the endpoints using the Django interface, Postman, Bruno or Insomnia. If you don't want to leave your IDE, I also recommend the RapidAPI extension.

&nbsp;

> Note: To interact with most of the endpoints you must be authenticated, since you will need to add a **token** to your requests to the server.

&nbsp;

## Main endpoints

The API exposes the following endpoints to manage users, songs and music preferences. Once the server is running you can try them at `http://127.0.0.1:8000/api`

| Route                     | Description                                                                     |
| :------------------------ | :------------------------------------------------------------------------------ |
| `GET /songs/`             | Gets the list of all songs available in the DB.                                 |
| `POST /songs/`            | Creates a new song in the database.                                             |
| `GET /songs/<int:pk>/`    | Gets the details of a specific song by its ID.                                  |
| `PUT /songs/<int:pk>/`    | Updates the details of an existing song.                                        |
| `DELETE /songs/<int:pk>/` | Deletes a specific song from the database.                                      |
| `GET /songs/export/`      | Exports all songs in JSON format.                                               |
| `POST /songs/import/`     | Imports songs from a JSON file into the server's database.                      |
| `POST /songs/favorite/`   | Marks or unmarks a song as a user's favorite.                                   |
| `GET /songs/favorites/`   | Gets all songs marked as favorites by the authenticated user.                   |
| `GET /users/`             | Gets the list of all users registered in the system.                            |
| `POST /users/`            | Creates a new user.                                                             |
| `GET /users/<int:pk>/`    | Gets the details of a specific user by their ID.                                |
| `PUT /users/<int:pk>/`    | Updates the details of an existing user.                                        |
| `DELETE /users/<int:pk>/` | Deletes a specific user from the system.                                        |
| `GET /spotify/search/`    | Performs a search on the Spotify API to find songs                              |

&nbsp;

## Usage examples

_We get the list of users_

![image](https://github.com/user-attachments/assets/cf32682b-9873-42d9-973c-32c402413483)

_We delete a song_

![image](https://github.com/user-attachments/assets/7e0e33c6-7086-413d-b0da-f3b00e05fe53)
![image](https://github.com/user-attachments/assets/b4c6e779-c29c-49a2-ac3b-7b51661fcdab)

_We search for a song by connecting to the Spotify API_

![image](https://github.com/user-attachments/assets/f673e88f-a913-49f5-95c8-75244978ac7e)

_Importing data in JSON format_

![image](https://github.com/user-attachments/assets/913a0362-57ca-45aa-9b92-f48e06812a63)
![image](https://github.com/user-attachments/assets/e120bc15-6993-4c13-909b-f3d515f943be)
![image](https://github.com/user-attachments/assets/2ae35a4e-fdee-4041-84cf-eadf4561ef2d)

_Exporting data in JSON format_

![image](https://github.com/user-attachments/assets/1d61c438-35fd-40f4-b739-4b218bdc3df3)

_A user unmarks a song as a favorite_

![image](https://github.com/user-attachments/assets/681336c3-2476-40c0-a192-917486820eec)
![image](https://github.com/user-attachments/assets/3a4c371b-0931-4efb-98c2-dc21ac8eefcd)
![image](https://github.com/user-attachments/assets/f2601324-1244-4fad-bdb9-8fcce3d0c424)


