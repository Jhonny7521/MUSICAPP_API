## MUSICAPP API

#### Descripción 

__MUSICAPP__ es una API que sigue los principios REST. Una vez autenticado, podrás registrar artistas, canciones, álbumes y crear playlists de canciones.

#### Autenticación

Para utilizar la API, debes estar autenticado. La autenticación se realiza mediante JSON Web Tokens (JWT), que se deben incluir en la cabecera de cada solicitud que hagas a la API.

#### Documentación

La documentación de la API se encuentra disponible en Swagger. Puedes acceder a ella a través de la URL `http://127.0.0.1:8000/swagger/docs/` una vez que hayas iniciado sesión en la API. En Swagger, encontrarás toda la información necesaria para utilizar la API, incluyendo los endpoints, los parámetros requeridos y las respuestas esperadas.

#### Endpoints
La API cuenta con los siguientes endpoints:

`/artists` : Este endpoint permite registrar nuevos artistas.

`/songs` : Este endpoint permite registrar nuevas canciones.

`/albums` : Este endpoint permite registrar nuevos álbumes.

`/playlists` : Este endpoint permite crear nuevas playlists de canciones.


#### Pruebas Unitarias
La API cuenta con pruebas unitarias implementadas para garantizar su correcto funcionamiento. Puedes ejecutar las pruebas ejecutando el comando npm test.

#### Requisitos
Para utilizar la API, debes tener instalado Node.js en tu sistema. También debes instalar las dependencias del proyecto ejecutando el comando:
```sh
$ python manage.py test
```

#### Uso
- Clona el repositorio:

```sh
$ git clone https://github.com/tu-usuario/musicapp-api.git
```

- Dirígete a la carpeta donde se ha clonado el proyecto

```sh
$ cd ProyectFolder
```

- Crea y activa un ambiente virtual:

> crea el ambiente virtual

```sh
$ python venv venv
```
> Activa el ambiente virtual
```sh
$ source venv/Scripts/activate    --> Windows
$ source venv/bin/activate        --> Linux
```

- Instala las dependencias:

```sh
$ pip install -r requirements.txt
```

- Inicia la API:

```sh
$ python manage.py runserver
```

- Accede a la documentación de la API a través de la URL /docs.

¡Listo! Ahora puedes utilizar la API MUSICAPP para registrar artistas, canciones, álbumes y crear playlists de canciones.

### Sobre el proyecto

- Lenguaje de programación: Python
- Versión de lenguaje: Python 3.9.7pip
- Framework utilizado: Django Rest Framework
- Motor de base de datos: MySQL / Postgre / Sqlite
