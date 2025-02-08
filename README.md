# Servidor Django de API musical

Este proyecto es una API RESTful creada con Django que integra la API de Spotify. El servidor permite gestionar usuarios, canciones y sus preferencias musicales, posibilitando marcar canciones como favoritas.

&nbsp;

## Instalación y config

1. Clona el repositorio.
2. Crea un entorno virtual (si no lo tienes ya). Recomiendo Anaconda:

```
conda create --name django-spotify-api python=3.9
conda activate django-spotify-api
```

3. Instala las dependencias `pip install -r requirements.txt`
4. Crea un fichero `.env` y agrega tus credenciales de Spotify:

```
SPOTIFY_CLIENT_ID=tu_client_id
SPOTIFY_CLIENT_SECRET=tu_client_secret

```

5. Aplica las migraciones de la base de datos: `python manage.py migrate`
6. Crea un superusuario para poder acceder al panel de administración de Django: `python manage.py createsuperuser`
7. Inicia el servidor: `python manage.py runserver`
8. Diviértete probando los endpoints usando la interfaz de Django, Postman, Bruno o Insomnia. Si no quieres salir del IDE también recomiendo la extensión RapidAPI.

&nbsp;

> Nota: Para poder interactuar con la mayoría de los endpoints es necesario estar autenticado ya que habrás de añadir un **token** en tus solicitudes al servidor.

&nbsp;

## Endpoints principales

La API expone los siguientes endpoints para gestionar usuarios, canciones y preferencias musicales. Una vez levantado el servidor podrás probarlos desde `http://127.0.0.1:8000/api`

| Ruta                      | Descripción                                                                     |
| :------------------------ | :------------------------------------------------------------------------------ |
| `GET /songs/`             | Obtiene la lista de todas las canciones disponibles en la BD.                   |
| `POST /songs/`            | Crea una nueva canción en la base de datos.                                     |
| `GET /songs/<int:pk>/`    | Obtiene los detalles de una canción específica mediante su ID.                  |
| `PUT /songs/<int:pk>/`    | Actualiza los detalles de una canción existente.                                |
| `DELETE /songs/<int:pk>/` | Elimina una canción específica de la base de datos.                             |
| `GET /songs/export/`      | Exporta todas las canciones en formato JSON.                                    |
| `POST /songs/import/`     | Importa canciones desde un archivo JSON al la base de datos del servidor.       |
| `POST /songs/favorite/`   | Marca o desmarca una canción como favorita de un usuario.                       |
| `GET /songs/favorites/`   | Obtiene todas las canciones marcadas como favoritas por el usuario autenticado. |
| `GET /users/`             | Obtiene la lista de todos los usuarios registrados en el sistema.               |
| `POST /users/`            | Crea un nuevo usuario.                                                          |
| `GET /users/<int:pk>/`    | Obtiene los detalles de un usuario específico mediante su ID.                   |
| `PUT /users/<int:pk>/`    | Actualiza los detalles de un usuario existente.                                 |
| `DELETE /users/<int:pk>/` | Elimina un usuario específico del sistema.                                      |
| `GET /spotify/search/`    | Realiza una búsqueda en la API de Spotify para encontrar canciones              |

&nbsp;

## Ejemplos de uso

_Obtenemos la lista de usuarios_

![image](https://github.com/user-attachments/assets/cf32682b-9873-42d9-973c-32c402413483)

_Eliminamos una canción_

![image](https://github.com/user-attachments/assets/7e0e33c6-7086-413d-b0da-f3b00e05fe53)
![image](https://github.com/user-attachments/assets/b4c6e779-c29c-49a2-ac3b-7b51661fcdab)

_Buscamos una canción conectando con la API de Spotify_

![image](https://github.com/user-attachments/assets/f673e88f-a913-49f5-95c8-75244978ac7e)

_Importación de datos en formato JSON_

![image](https://github.com/user-attachments/assets/913a0362-57ca-45aa-9b92-f48e06812a63)
![image](https://github.com/user-attachments/assets/e120bc15-6993-4c13-909b-f3d515f943be)
![image](https://github.com/user-attachments/assets/2ae35a4e-fdee-4041-84cf-eadf4561ef2d)

_Exportación de datos en formato JSON_

![image](https://github.com/user-attachments/assets/1d61c438-35fd-40f4-b739-4b218bdc3df3)

_Usuario desmarca una canción como favorita_

![image](https://github.com/user-attachments/assets/681336c3-2476-40c0-a192-917486820eec)
![image](https://github.com/user-attachments/assets/3a4c371b-0931-4efb-98c2-dc21ac8eefcd)
![image](https://github.com/user-attachments/assets/f2601324-1244-4fad-bdb9-8fcce3d0c424)


