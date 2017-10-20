# UT1-A4: Sirviendo aplicaciones Php y Python



## Sitio Web 1

El objetivo de la práctica es que al escribir la siguiente dirección [http://php.alu5906.me](http://php.alu5906.me) y que muestre la aplicación demo_php.zip


### 1.1 Subir fichero demo_php al Cloud

Utilizamos el comando `scp -r "Descargas/demo_php" "cloud:"`

![imagen](img/001.png)

Comprobación del fichero está subido en el cloud.

![imagen](img/002.png)

Cambiamos el nombre del demo_php a php.

~~~
alu5906@cloud:~$ mv demo_php/ php
alu5906@cloud:~$ ls -l
total 1588
-rw-rw-r-- 1 alu5906 alu5906 1595408 oct 16 12:44 get-pip.py
drwxrwxr-x 3 alu5906 alu5906    4096 oct 20 11:36 hellopython
-rw-rw-r-- 1 alu5906 alu5906      66 sep 25 15:34 index.html
drwxr-xr-x 3 alu5906 alu5906    4096 oct 20 12:39 php
drwxr-xr-x 4 alu5906 alu5906    4096 sep 25 15:30 series
drwxr-xr-x 2 alu5906 alu5906    4096 oct  2 12:03 shared
-rw-rw-r-- 1 alu5906 alu5906      23 oct 16 11:23 test.php
drwxrwxr-x 8 alu5906 alu5906    4096 oct  8 13:14 webapps
alu5906@cloud:~$

~~~
### 1.2 Creamos un fichero de Virtual Host

Solo tenemos que crear un fichero nuevo llamado `php` en la ruta `/etc/nginx/sities-available`

~~~
alu5906@cloud:~$ sudo nano /etc/nginx/sites-available/php
[sudo] password for alu5906:
alu5906@cloud:~$ cat /etc/nginx/sites-available/php
server {
	server_name php.alu5906.me;
	index index.php;
	root /home/alu5906/php;
	location ~ \.php$ {
		include snippets/fastcgi-php.conf;
		fastcgi_pass unix:/run/php/php7.0-fpm.sock;
	}
}
alu5906@cloud:~$ sudo ln -s /etc/nginx/sites-available/php /etc/nginx/sites-enabled/
~~~
![img](img/004.png)

- Necesitamos reiniciar el servicio

~~~
alu5906@cloud:~$ sudo systemctl reload nginx.service alu5906@cloud:~$ sudo systemctl status nginx.service
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: en
   Active: active (running) (Result: exit-code) since lun 2017-09-25 11:31:01 UT
  Process: 4998 ExecReload=/usr/sbin/nginx -g daemon on; master_process on; -s r
 Main PID: 19141 (nginx)
    Tasks: 2
   Memory: 5.6M
      CPU: 4.262s
   CGroup: /system.slice/nginx.service
           ├─ 5002 nginx: worker process                           
           └─19141 nginx: master process /usr/sbin/nginx -g daemon on; master_pr

oct 20 12:48:42 cloud systemd[1]: Reloading A high performance web server and a
oct 20 12:48:42 cloud systemd[1]: Reloaded A high performance web server and a r
oct 20 14:29:21 cloud systemd[1]: Reloading A high performance web server and a
oct 20 14:29:21 cloud systemd[1]: Reloaded A high performance web server and a r
Warning: Journal has been rotated since unit was started. Log output is incomple
lines 1-17

~~~

### 1.3 Comprobación de la Página Web [http://php.alu5906.me](http://php.alu5906.me)

[![img](img/005.png)](http://php.alu5906.me)

## Sitio Web 2
