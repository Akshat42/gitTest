 <!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <form action="/php2.php" method="post">
Name:<input type="text" name="fname">
<input type="SUBMIT">
</form>
  <?php if($_SERVER["REQUEST_METHOD"]=="post"){
  $name="fname";
  if(empty($name)){
    echo "field is empty";
  }
  else{
    echo $name;
  }
}
 ?>
  </body>
</html>
