
# NGINX/Ubuntu

- [Creación Carpeta Series](#id1)

- [Creación de la página Web](#id2)

- [Subir fichero con el comando scp por ssh cliente al servidor](#id3)

- [Mover fichero a la ruta /var/www/html/series](#id4)

- [Recargar el servicio de nginx](#id5)


- [Creación de un Virtual Host en el Servidor Ngnix](#id7)

- [Crear carpeta y fichero index.html](#id8)

- [Crear un enlace simbólico en /etc/nginx/sites-enabled](#id9)

- [Esctuctura final de la carpeta series](#id10)

- [Comprobación que la Página Web se pueda visualizar](#id6)

![imagen](img/ngnix.png)

# Creación carpeta de Series <a name="id1"></a>

Lo primero que tenemos que crear, es una carpeta en la siguiente ruta **/var/www/html.**

Como comprobamos la carpeta series no esta creada.

![imagen](img/047.png)

Dentro de la carpeta html creamos la carpeta series.

![imagen](img/048.png)


# Creación de la página Web.<a name="id2"></a>

En la carpeta de series creamos un fichero llamado index.html.
Abrimos el fichero index.html nano y creamos una página web.

Creo la estructura de las carpetas necesarias.

> series

> > css

> > img

> > index.html

![imagen](img/003.png)

Página Web diseñada con el nano.

![imagen](img/049.png)

Con el comando cat mostramos el fichero index.html

![imagen](img/001.png)


# Subir fichero con el comando scp por ssh cliente al servidor<a name="id3"></a>

El comando scp se utiliza para enviar ficheros al servidor o viceversa.

Ejemplo de como enviar un fichero del equipo local al servidor

![imagen](img/051.png)

# Mover fichero a la ruta /var/www/html/series<a name="id4"></a>

Tenemos que conectarnos al servidor cloud mediante ssh. Ejecutamos un ls -l en el usuario alu5906, encontramos los ficheros css, img, index.html. Con el comando mv movemos los ficheros a la ruta **/var/www/html/series.**

Ver la imagen.

![imagen](img/053.png)

El comando tree es útil para ver la estructura de los ficheros y carpetas.

# Recargar el servicio de nginx<a name="id5"></a>
Solo tenemos que escribir el siguiente comando para recargar los cambios.

**sudo systemctl reload nginx.service**

![imagen](img/002.png)


# Creación de un Virtual Host en el Servidor Ngnix <a name="id7"></a>

Tenemos que ir a la siguiente ruta /etc/nginx/sites-available.
Creamos con el nano un fichero nuevo y dentro escribimos lo siguiente.

![imagen](img/12.png)


# Crear carpeta y fichero index.html <a name="id8"></a>

En mi caso ya tenia creado toda la escructura de carpeta de series, con css, img y fichero index.html. Solo tengo que moverlo a la siguiente ruta:

![imagen](img/10.png)

#  Crear un enlace simbólico en /etc/nginx/sites-enabled <a name="id9"></a>

Tenemos que crear un enlace simbólico desde /etc/nginx/sites-available/series a la siguiente ruta /etc/nginx/sites-enabled/

![imagen](img/11.png)

# Estructura final de la carpeta series <a name="id10"></a>


![imagen](img/14.png)

Importante al final siempre recargar el servicio Ngnix


![imagen](img/13.png)

# Comprobación que la Página Web se pueda visualizar.<a name="id6"></a>

Solo tenemos que abrir un navegador y escribir la siguiente dirección.

[Página Web de mis series favoritas](http://alu5906.me/series)

![imagen](img/005.png)
