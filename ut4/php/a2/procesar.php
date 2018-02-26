<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Probando PHP!!</title>
    </head>
    <body>
        <?php
            $nombre = $_POST["nombre"];
            $apellidos = $_POST["apellidos"];
            $salario = (float)$_POST["salario"];
            $edad = (int)$_POST["edad"];
            if ($salario > 2000) {
                echo(" Yo $nombre $apellidos tengo $edad años y mi salario($salario) es superior a 2000");
            }
            else if ($salario > 1000 and $salario < 2000) {
                if ($edad > 45) {
                    $sube = $salario * 1.03;
                    echo("Yo $nombre $apellidos. Tengo $edad años es mayor a 45 años, mi salario es $sube");
                }
                else {
                    $sube = $salario * 1.10;
                    echo("Yo $nombre $apellidos. Tengo $edad años y es menor a 45 años, mi salario es $sube");
                }
            }

            else {
                if ($edad < 30) {
                    $salario = 1100;
                    echo("Yo $nombre $apellidos. Tengo $edad años es menor a 30 años, mi salario es $salario");
                }
                else if ($edad > 30 and $edad < 45){
                    $sube = $salario * 1.03;
                    echo("Yo $nombre $apellidos. Tengo $edad años es entre 30 años y 45 años, mi salario es $sube");
                }
                else {
                    $sube = $salario * 1.15;
                    echo(" Yo $nombre $apellidos. Tengo $edad años es mayor a 45 años mi salario es $sube");
                }
            }

        ?>
    </body>
</html>
