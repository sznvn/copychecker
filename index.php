
<!DOCTYPE html>
<html>
<body>
<h2> Проверка документа на объем заимствований </h2>
<form action="upload.php" method="POST" enctype="multipart/form-data">
  Выбирете docs, pdf или txt...
  <br>
  <input type="hidden" name="MAX_FILE_SIZE" value="3000000" />
  <input type="file" name="file">
  <br><br><br>
  <input type="submit" value="Отправить" name="submit">
</form>

</body>
</html>

