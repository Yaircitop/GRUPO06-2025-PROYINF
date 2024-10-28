# GRUPO11

Este es el repositorio del *Grupo 11*, cuyos integrantes son:

* Bruno Decinti - 201911524-3
* Nicolás Muñoz - 202104641-0
* Yair Cárdenas - 202273579-1
* **Tutor**: Josefa Flores

## Wiki
Puede acceder a la Wiki mediante el siguiente [enlace](https://github.com/Yaircitop/GRUPO11-2024-PROYINF/wiki)

## Videos
* [Video Presentación Cliente](https://www.youtube.com/watch?v=abJau21SDIk&ab_channel=RicardoSalasLetelier)

## Pasos necesarios para levantar el proyecto

* Tener instalado el software base para el proyecto: Django y la base de datos PostgreSQL.
* Crear una base de datos que contendrá tanto el registros de los usuarios como los boletines que se irán subiendo.
* Clonar el repositorio "main".
* Crear un archivo .env en la carpeta donde se clone el repositorio, el cual siga el siguiente formato:
```.env
DB_NAME=nombre_base_de_datos // el nombre de la base de datos que se haya creado
DB_USER=nombre_usuario_BD // el nombre del usuario creador de la base de datos (por default es postgres)
DB_PASSWORD=contraseña_BD // la contraseña para acceder a postgreSQL
DB_HOST=host_de_su_BD // suele ser localhost
DB_PORT=puerto_BD// puerto donde se instaló postgreSQL
```
* Abrir una terminal donde se encuentre el archivo manage.py (este se encuentra en la carpeta backend).
* Instalar la libreria python-decouple y psycopg2 para el enlace de la base de datos local con Django: para ello, utilizar los comandos:
```python
..\GRUPO11-2024-PROYINF\pagina\backend> pip install python-decouple
..\GRUPO11-2024-PROYINF\pagina\backend> pip install python-decouple psycopg2
```
* Posteriormente realizar migraciones:
```python
..\GRUPO11-2024-PROYINF\pagina\backend> py manage.py makemigrations
..\GRUPO11-2024-PROYINF\pagina\backend> py manage.py migrate
```
* Y levantar el servidor:
```python
..\GRUPO11-2024-PROYINF\pagina\backend> py manage.py runserver
```
* Luego de esto, se podrá acceder a la página web, la cual inicialmente no tendrá boletines en su catálogo, ni tampoco registros de usuarios, puesto que al trabajar con bases de datos locales, no hay archivos compartidos a través de estas, por tanto utiliza las tablas de la base de datos recién creada. Para recorrer todas sus funcionalidades, recomendamos crear usuarios a gusto, uno de ellos con el rol de is_staff, para que este pueda subir boletines (subir_boletin.html) o archivos de ejemplo (se pueden observar en la carpeta media/pdfs algunos archivos que como grupo utilizamos de ejemplos para el debugging) al catálogo de la web (catalogo.html) y se pueda probar la página desde la visión de un usuario regular o un administrador.
