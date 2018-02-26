<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Creador de Tablas</title>
    </head>
    <body>
      <form action="ejercicio4.php" method="get">
          <label for="filas">Número de filas:</label>
          <input type="text" name="filas"/><br>
          <label for="columnas">Número de columnas:</label>
          <input type="text" name="columnas"/><br>
          <input type="submit" value="enviar"/>
      </form>
      <br>
      <?php
            if (isset($_GET["filas"]) and isset($_GET["columnas"])) {
                $filas = (int)$_GET["filas"];
                $columnas = (int)$_GET["columnas"];
                if ($filas < 1 or $columnas < 1) {
                  echo("<p>Debe poner como mínimo 1 columna y 1 fila.</p>");
                }
                else {
                  echo("<table border='1'>");
                  for($i=1; $i<=$filas; $i++){
                    echo("<tr>");
                    for($j=1; $j<=$columnas; $j++){
                      echo("<td>$i-$j</td>");
                    }
                    echo("</tr>");
                  }
                  echo("</table>");
                }
            }
        ?>
    </body>
</html>
