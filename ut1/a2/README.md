# Listado de Directorios

## Se crea un listado al entrar en [alu5906.me/shared](http://alu5906.me/shared)

Primero tenemos que crear un directorio en la carpeta de /home/alu5906/shared

![imagen](img/007.jpg)

## Se debe crear un listado de ficheros

Accedemos a la ruta de /home/alu5906/shared y dentro creamos enlace simbólico de los siguientes ficheros.

    - /boot/initrd.img-4.4.0-9 (imagen del kernel)
    - /etc/resolv.conf (listado de DNS)
    - /etc/bash.bashrc (configuración global de bash)
    - /proc/cpuinfo (características de la máquina)


![imagen](img/001.jpg)

Se comprueba que se crearon los enlaces simbólicos.

![imagen](img/004.jpg)

## Se crea un fichero de host virtual en la ruta /etc/ngingx/sites-available/alu5906.me y creación del enlace simbólico

Creamos el fichero y escribimos los siguiente. Luego después de escribir todo lo que se muestra en cat /etc/nginx/sites-available/alu5906.me. Como se muestra en la imagen se crea un enlace simbolico a la ruta anterior /etc/nginx/sites-enabled/alu5906.me

![imagen](img/005.jpg)

Importante recargar el servicio nginx

    * sudo systemctl reload nginx.service

## Se comprueba que funciona correctamente y se muestra los ficheros en la carpeta shared

![imagen](img/006.jpg)
