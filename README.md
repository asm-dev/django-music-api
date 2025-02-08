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

La API expone los siguientes endpoints para gestionar usuarios, canciones y preferencias musicales.

| Ruta                      | Descripción                                                                     |
| :------------------------ | :------------------------------------------------------------------------------ |
| `GET /api/songs/`             | Obtiene la lista de todas las canciones disponibles en la BD.                   |
| `POST /api/songs/`            | Crea una nueva canción en la base de datos.                                     |
| `GET /api/songs/<int:pk>/`    | Obtiene los detalles de una canción específica mediante su ID.                  |
| `PUT /api/songs/<int:pk>/`    | Actualiza los detalles de una canción existente.                                |
| `DELETE /api/songs/<int:pk>/` | Elimina una canción específica de la base de datos.                             |
| `GET /api/songs/export/`      | Exporta todas las canciones en formato JSON.                                    |
| `POST /api/songs/import/`     | Importa canciones desde un archivo JSON al la base de datos del servidor.       |
| `POST /api/songs/favorite/`   | Marca o desmarca una canción como favorita de un usuario.                       |
| `GET /api/songs/favorites/`   | Obtiene todas las canciones marcadas como favoritas por el usuario autenticado. |
| `GET /api/users/`             | Obtiene la lista de todos los usuarios registrados en el sistema.               |
| `POST /api/users/`            | Crea un nuevo usuario.                                                          |
| `GET /api/users/<int:pk>/`    | Obtiene los detalles de un usuario específico mediante su ID.                   |
| `PUT /api/users/<int:pk>/`    | Actualiza los detalles de un usuario existente.                                 |
| `DELETE /api/users/<int:pk>/` | Elimina un usuario específico del sistema.                                      |
| `GET /api/spotify/search/`    | Realiza una búsqueda en la API de Spotify para encontrar canciones              |

&nbsp;

## Ejemplos de uso

_Obtenemos la lista de usuarios_

![image](https://github.com/user-attachments/assets/cf32682b-9873-42d9-973c-32c402413483)

_Eliminamos una canción_

Imagen

_Buscamos una canción conectando con la API de Spotify_

![image](https://github.com/user-attachments/assets/f673e88f-a913-49f5-95c8-75244978ac7e)


_Importación y exportación de datos para comunicación entre cliente y servidor_

Imagen

_Usuario marca y desmarca una canción como favorita_

Imagen
