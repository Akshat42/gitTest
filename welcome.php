<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <?php if($_SERVER['GET_METHOD']=="POST"){
      $name=$_POST['fname'];
      $email=$_POST['email'];
      if(empty($name)){
        echo "field empty";
      }
      else {
      echo "hello".$name."<br>";
      }
      if(empty($email)){
        echo "field empty";
      }
      else{
      echo "hello".$email."<br>";
      }
    } ?>
  </body>
</html>
