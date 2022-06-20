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
