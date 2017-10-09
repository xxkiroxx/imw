# UT1-A3: Trabajo con Virtual Host

- [Sitio Web 1](#id1)

    - [http://imw.alu5906.me](#id2)

        - [Debe mostrar una página con la imagen de "Diagrama de unidades de trabajo" de IMW (ver moodle de la asignatura)](#id3)

        - [La imagen no debe ser enlazada en remoto, sino se debe descargar al directorio de trabajo en la máquina de producción, y luego usar un tag <img> apuntando a la ruta local.](#id4)

    - [http://imw.alu5906.me/mec/](#id5)

        - [Debe mostrar una página con un enlace al Real decreto del título de Administración de Sistemas Informáticos en Red - MEC (ver moodle de la asignatura)](#id6)

- [Sitio Web 2](#id7)

    - [http://varlib.alu5906.me:9000](#id8)

    - [Debe mostrar el listado de ficheros y directorios de /var/lib de la máquina de producción.](#id9)

- [Sitio Web 3](#id10)

    - [https://ssl.alu5906.me/students/ (ojo, es https!)](#id11)

    - [Debe pedir usuario/clave. Los datos son:](#id12)

        - [USUARIO: usuario1](#id13)

        - [CLAVE: aula108](#id14)

    - [Debe mostrar una página web con el nombre de todo el alumnado de clase.](#id15)

    - [Se debe prohibir explícitamente el acceso al fichero .htpasswd](#id16)

- [Sitio Web 4](#id17)

    - [http://redirect.alu5906.me](#id18)

        - [Se debe redirigir cualquier petición de este dominio a http://target.alu5906.me](#id19)


        - [Al acceder a http://target.alu5906.me se debe mostrar la página web siguiente initializr-verekia-4.0.zip.](#id23)

            - [Para copiar y descomprimir el fichero initializr.zip se recomienda usar alguna de las siguientes herramientas: curl, wget, scp, unzip.](#id24)

        - [Los logfiles deben ser:](#id25)

            - [/var/log/nginx/redirect/access.log](#id26)

            - [/var/log/nginx/redirect/error.log](#id27)




## Sitio web 1 <a name="id1"></a>

### http://imw.alu5906.me <a name="id2"></a>

![imagen](img/013.png)

#### Debe mostrar una página con la imagen de "Diagrama de unidades de trabajo" de IMW (ver moodle de la asignatura).<a name="id3"></a>

Primero tenemos que crear una carpeta en la siguiente ruta /home/alu5906/webapps/imw

![imagen](img/008.png)

Copiamos otro fichero index.html para tener toda la estructura y modificamos con los datos que nos indica la práctica.

![imagen](img/007.png)

#### La imagen no debe ser enlazada en remoto, sino se debe descargar al directorio de trabajo en la máquina de producción, y luego usar un tag <img> apuntando a la ruta local.<a name="id4"></a>

El siguiente paso es descargar la imagen de diagrama de unidades de trabajo y subirlo al servidor cloud.

    Utilizamos el comando scp

![imagen](img/001.png)

Solo tenemos que mover la imagen 001.png a la ruta correspondiente. Coma ya muestra en la imagen anterior.

Realizamos un tree para comprobar como está su estructura.

![imagen](img/008.png)

## Crear Fichero Virtual Host

Ya tenemos creado las carpetas, el fichero index.html, solo nos falta crear el virtual host.

Por lo tanto tenemos que ir a la siguiente ruta:

    cd /etc/nginx/sities-available

En esá ruta solo tenemos que crear un fichero llamado imw y escribimos dentro el siguiente contenido.

![imagen](img/004.png)

![imagen](img/003.png)

El siguiente paso es crear un enlace simbólico.

![imagen](img/005.png)

Solo nos falta reiniciar el servicio.

    sudo systemctl reload nginx



### http://imw.alu5906.me/mec/<a name="id5"></a>

![imagen](img/014.png)

#### Debe mostrar una página con un enlace al Real decreto del título de Administración de Sistemas Informáticos en Red - MEC (ver moodle de la asignatura).<a name="id6"></a>

Lo primero que tenemos que realizar son las carpetas en la siguiente ruta.

    /home/alu5906/webapps/mec

![imagen](img/008.png)

copiamos el index.html de imw y lo metemos en un nuevo index.html y lo modificamos como nos indica la práctica.

![imagen](img/011.png)

Ya tenemos la estructura de la carpeta y el index.html.

El fichero pdf está en el moodle, voy a realizar dos enlaces, uno con la dirección del moodle y la otra descargo el pdf y lo subo en el cloud. Con su enlace local.

Primero tenemos subir el fichero con el comando scp.

![imagen](img/038.png)

y modificamos el html para la ruta del pdf.

![imagen](img/040.png)

## Crear Virtual Host

Tenemos que ir a la ruta siguiente para crear un virtual host.

![imagen](img/010.png)

Solo necesitamos recargar las modificaciones en el servicio.

    sudo systemctl reload nginx

## Sitio web 2<a name="id7"></a>

### http://varlib.alu5906.me:9000<a name="id8"></a>

Accedemos como varlib.alu5906.me

![imagen](img/016.png)

El resultado correcto especificando el puerto 9000

![imagen](img/017.png)

### Debe mostrar el listado de ficheros y directorios de /var/lib de la máquina de producción.<a name="id9"></a>

Tenemos que ir a la ruta de /etc/nginx/sities-available.

Debemos crear un nuevo virtual host llamado varlib.

Abrimos el fichero y escribimos los siguiente.

![imagen](img/012.png)

Com muestra en la imagen anterior, también debemos crear un enlace simbólico de sities-available/varlib a sities-enabled

Solo falta agregar en el fichero que salga por el puerto 9000, debemos abrir el fichero varlib y escribir

    listen 9000;

![imagen](img/015.png)

Por último solo debemos reiniciar el Servicio nginx

    sudo systemctl reload nginx

Tenemos otra opción a la hora de colocar la ruta de /var/lib en el fichero de virtual host.

Primero creamos una carpeta en webapps/varlib.

Luego solo tenemos que crear un enlace simbólico de la ruta /var/lib a la carpeta creada en /home/alu5906/webapps/varlib.

 ![imagen](img/041.png)

Modificamos el fichero de virtual host

 ![imagen](img/042.png)

## Sitio web 3<a name="id10"></a>

### https://ssl.alu5906.me/students/ (ojo, es https!)<a name="id11"></a>

![imagen](img/036.png)

Se muestra los alumnos

![imagen](img/037.png)

### Debe pedir usuario/clave. Los datos son:<a name="id12"></a>

Lo primero que tenemos que crear es la siguiente carpeta.

![imagen](img/018.png)

También debemos crear un index.html

![imagen](img/019.png)

La muestra del html

![imagen](img/020.png)


#### USUARIO: usuario1<a name="id13"></a>

Para crear el usuario solo tenemos que crear un fichero llamado .htpasswd y escribimos dentro usuario:"aqui sería la contraseña".


![imagen](img/022.png)


#### CLAVE: aula108<a name="id14"></a>

Tenemos que crear con el siguiente comando una contraseña cifrada.

![imagen](img/021.png)

Realizamos un ls -la para ver si se creo correctamente le fichero.

![imagen](img/023.png)

### Modificamos un virtual Host existente.

Solo tenemos que abrir el fichero con un edit y escribimos los siguientes parámetros.

![imagen](img/024.png)

Luego tenemos que crear un enlace simbólico, pero en este caso nosotros ya lo teniamos creado.

![imagen](img/025.png)

Solo debemos ejecutar el comando.

    sudo systemctl reload nginx


### Debe mostrar una página web con el nombre de todo el alumnado de clase.<a name="id15"></a>

Abrimos un navegador escribimos la página y debe salir una autenticación para usuarios.

![imagen](img/036.png)

### Se debe prohibir explícitamente el acceso al fichero .htpasswd<a name="id16"></a>

Para prohibir el acceso al fichero .htpasswd debemos escribir los siguientes parámetros en el fichero de virtual host llamado ssl

![imagen](img/026.png)

Por lo tanto al acceder desde el navegador.

![imagen](img/048.png)

## Sitio web 4

### http://redirect.alu5906.me<a name="id17"></a>

Lo primero que tenemos que crear son las carpetas.

![imagen](img/027.png)

### Se debe redirigir cualquier petición de este dominio a http://target.alu5906.me<a name="id18"></a>

 [http://redirect.alu5906.me/test/](http://redirect.alu5906.me/test/) -> [http://target.alu5906.me](http://target.alu5906.me)

 [http://www.redirect.alu5906.me/probando/](http://www.redirect.alu5906.me/probando/) -> [http://target.alu5906.me](http://target.alu5906.me)

 [http://www.redirect.alu5906.me/hola/](http://www.redirect.alu5906.me/hola/) -> [http://target.alu5906.me](http://target.alu5906.me)


### Al acceder a http://target.alu5906.me se debe mostrar la página web siguiente initializr-verekia-4.0.zip.<a name="id22"></a>

Copiamos la url del fichero para descargar y escribimos el siguiente comando.

![imagen](img/028.png)

La página debe quedar de la siguiente manera:

![imagen](img/34.png)


#### Para copiar y descomprimir el fichero initializr.zip se recomienda usar alguna de las siguientes herramientas: curl, wget, scp, unzip.<a name="id23"></a>

Utilizamos el comando unzip para descomprimir el fichero.

![imagen](img/029.png)

Con el comando scp subimos la carpeta completa al servidor cloud.

![imagen](img/030.png)

Comprobamos que se subio correctamente la carpeta

![imagen](img/031.png)

Ya tenemos las carpetas creada y el fichero subido al servidor. Solo falta crear un virtual host.

En este caso nosotros ya tenemos varios virtual host creado y lo que realizó es copiar un fichero de virtual host con un nombre diferente y lo abro para modificar los nuevos parámetros.

![imagen](img/032.png)

Parámetros que debemos modificar tanto en el redirect.

![imagen](img/35.png)

Parámetros que debemos modificar tanto en el target.

![imagen](img/035.png)

Solo nos falta crear los enlace simbólico de cada uno.

![imagen](img/033.png)


### Los log files deben ser:<a name="id24"></a>

#### /var/log/nginx/redirect/access.log<a name="id25"></a>

Lo primero tenemos que crear una carpeta.

![imagen](img/043.png)

Luego solo tenemos que crear el fichero.

![imagen](img/044.png)

#### /var/log/nginx/redirect/error.log<a name="id26"></a>

Creamos el fichero para el error.log

![imagen](img/044.png)


Por último solo tenemos que modificar el fichero de virtual host, en la siguiente ruta.

    /etc/nginx/sities-available/redirect

Escribimos los siguientes parámetros.

![imagen](img/045.png)

Cambiar permisos de la carpeta y fichero log

![imagen](img/046.png)

Comprobamos que el fichero access.log funciona.

![imagen](img/047.png)
