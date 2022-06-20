<style>
   [data-tooltip] {
    position: relative; /* Относительное позиционирование */ 
   }
   [data-tooltip]::after {
    content: attr(data-tooltip); /* Выводим текст */
    position: absolute; /* Абсолютное позиционирование */
    width: 300px; /* Ширина подсказки */
    left: 0; top: 0; /* Положение подсказки */
    background: #404040; /* Синий цвет фона */
    color: #FFFFFF; /* Цвет текста */
    padding: 0.5em; /* Поля вокруг текста */
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3); /* Параметры тени */
    pointer-events: none; /* Подсказка */
    opacity: 0; /* Подсказка невидима */
    transition: 1s; /* Время появления подсказки */
   } 
   [data-tooltip]:hover::after {
    z-index: 2;
    opacity: 1; /* Показываем подсказку */
    top: 2em; /* Положение подсказки */
   }
</style>
<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$upload = 'upload/';

$tmp_name = $_FILES["file"]["tmp_name"];
$name = basename($_FILES["file"]["name"]);
move_uploaded_file($tmp_name, "$upload/$name");

//print_r($_FILES);

$out = shell_exec('/var/www/antiplagiat/copychecker/bin/python3 copychecker/main.py');

echo $out;
?>
