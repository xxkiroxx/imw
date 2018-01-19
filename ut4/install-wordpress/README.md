# WordPress

![](img/000.png)


- [1. Configuración Base de datos MySQL para WordPress](#1)
- [2. Descargar WordPress desde su página Web](#2)
    - [2.1 Mover el directorio WordPress a `/usr/share`](#4)
    - [2.2 Permisos para el directorio WordPress](#5)
    - [2.3 Configurar fichero de configuración `wp-config.php`](#6)
- [3. Creación de Virtual Host con el Nginx](#7)
- [4. Configuración del sitio WordPress vía Web](#8)
- [5. Acceder a WordPress](#3)
- [6. Personalizar el Tema de WordPress](#9)
- [7. Ajustar los permalinks a "Día y Nombre"](#10)
- [8. Escribir un post con las estadísticas de uso de "WordPress"](#11)


## 1. Configuración Base de datos MySQL para WordPress <a name=1></a>

Tenemos que abrir una terminal nueva y debemos escribir el siguiente comando para acceder a nuestra base de datos `MySQL`

- `mysql -u root -p`

![](img/001.png)

- Tenemos que crear una base de datos en este caso la llamamos `wpdatabase`.

![](img/002.png)

- Creamos un usuario llamado `wpuser`

![](img/003.png)

- Al usuario creado `wpuser` le damos permiso con control total para la base de datos creada `wpdatabase`

![](img/004.png)

## 2. Descargar WordPress desde su página Web <a name=2></a>

Podemos acceder a la página de [`WordPress`](https://es.wordpress.org/txt-download/) y podemos descargar la aplicación.


Primero vamos al directorio de archivos temporales de `Ubuntu -> /tmp`

![](img/005.png)

En nuestro caso vamos a utilizar el comando `curl -O`.

![](img/006.png)

Descomprimimos el fichero descargado `latest.zip` en `/tmp`

![](img/007.png)


### 2.1 Mover el directorio WordPress a `/usr/share` <a name=4></a>

Copiamos el fichero descomprimido `WordPress` y a la siguiente ruta `/usr/share`

![](img/008.png)

Comprobamos que el directorio está copiado en la ruta `/usr/share`

![](img/009.png)

### 2.2 Permisos para el directorio WordPress <a name=5></a>

Si nos fijamos el directorio está con permisos de `root` tanto de usuario como de grupo.

- Tenemos que cambiar el permiso de usuario y grupo de `root` a `www-data`

![](img/010.png)

Comprobamos que se cambio correctamente los permisos para el usuario y grupo `www-data`

![](img/011.png)


### 2.3 Configurar fichero de configuración `wp-config.php` <a name=6></a>

Tenemos que modificar el fichero que esta dentro del directorio de `wordpress` por lo tanto tenemos que ir a su ruta `/usr/share/wordpress`.

![](img/012.png)

Realizamos una copia del fichero de configuración `wp-config-sample.php` a `wp-config.php`

![](img/013.png)

Modificamos el fichero y tenemos que buscar las líneas:

- DB_NAME: `Nombre Base de Datos de WordPress`
- DB_USER: `Usuario de la Base Datos para WordPress`
- DB_PASSWORD: `Contraseña del usuario`
- DB_CHARSET: `utf8m4`

![](img/014.png)

## 3. Creación de Virtual Host con el Nginx <a name=7></a>

Tenemos que crear un nuevo virtual host en `nginx` para la instalación de nuestro `wordpress`.

- Vamos a la siguiente ruta `/etc/nginx/sites-available`.
- Creamos el virtual host con el nombre de `wordpress`

![](img/015.png)

- Solo nos faltas crear un enlace simbólico en la siguiente ruta `/etc/nginx/sites-enabled`

![](img/016.png)

- Comprobamos que está creado el enlace simbólico.

![](img/017.png)

- Tenemos que reiniciar o recargar el servicio de `nginx.service`

![](img/018.png)

## 4. Configuración del sitio WordPress vía Web <a name=8></a>

Solo tenemos que ir a nuestro navegador y escribimos en el url [`wordpress.alu5906.me`](http://wordpress.alu5906.me).

Nos saldrá qué tenemos que seleccionar el idioma, en nuestro caso el `español`, le damos continuar.

![](img/019.png)

Tenemos un formulario con la siguiente información.

- Título del sitio: `Establecer el nombre que nosotros queramos`.
- Nombre de Usuario: `Establecemos el nombre para el administrador de WordPress`
- Contraseña: `Contraseña para el usuario administrador`
- Correo: `Escribir nuestro correo electrónico`

![](img/020.png)

Ya tenemos instalado y configurado nuestro `WordPress` en nuestro servidor `Ubuntu`.

![](img/021.png)

## 5. Acceder a WordPress <a name=3></a>

Solo tenemos que escribir en nuestro navegador la siguiente url [`wordpress.alu5906.me/wp-login.php`](http://wordpress.alu5906.me/wp-login.php)

- Solo escribimos el usuario `admin` con su contraseña.

![](img/022.png)

Accedemos a nuestro `WordPress` aquí podemos modificar todo.

![](img/023.png)

## 6. Personalizar el Tema de WordPress <a name=9></a>

Solo tenemos que ir a cambiar tu tema por completo.

![](img/023.png)

- Seleccionamos un tema en mi caso es el siguiente.

![](img/024.png)

- Vamos a `Temas` y Seleccionamos el tema descargado

![](img/031.png)

## 7. Ajustar los permalinks a "Día y Nombre" <a name=10></a>

Tenemos que ir a `Ajustes -> enlaces permanentes`

![](img/029.png)

- Seleccionamos el `día y nombre`

![](img/030.png)

## 8. Escribir un post con las estadísticas de uso de "WordPress" <a name=11></a>


![](img/026.png)
![](img/027.png)
![](img/028.png)
