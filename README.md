# Servidor Django de API musical

Este proyecto es una API RESTful creada con Django que integra la API de Spotify. 

El servidor permite gestionar usuarios, canciones y sus preferencias musicales, posibilitando marcar canciones como favoritas.

&nbsp;

## Instalación y config

1. Clona el repositorio.
4. Crea un entorno virtual (si no lo tienes ya). Recomiendo Anaconda:

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

6. Aplica las migraciones de la base de datos: `python manage.py migrate`
7. Crea un superusuario para poder acceder al panel de administración de Django: `python manage.py createsuperuser`
8. Inicia el servidor: `python manage.py runserver`
9. Diviértete probando los endpoints usando la interfaz de Django, Postman, Bruno o Insomnia. Si no quieres salir del IDE también recomiendo la extensión RapidAPI.

&nbsp;

> Nota: Para poder interactuar con la mayoría de los endpoints es necesario estar autenticado ya que habrás de añadir un **token** en tus solicitudes al servidor.

&nbsp;

## Endpoints principales

La API expone los siguientes endpoints para gestionar usuarios, canciones y preferencias musicales

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

Imagen

_Eliminamos una canción_

Imagen

_Buscamos una canción en Spotify API_

Imagen

_Importación y exportación de datos para comunicación entre cliente y servidor_

Imagen

_Usuario marca y desmarca una canción como favorita_

Imagen
