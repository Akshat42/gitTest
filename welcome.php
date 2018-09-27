    <?php if($_SERVER["REQUEST_METHOD"]=="POST"){
      $name=$_POST['fname'];
      $email=$_POST['email'];
      if(empty($name)){
        echo "field empty<br>";
      }
      else {
      echo "hello ".$name."<br>";
      }
      if(empty($email)){
        echo "field empty<br>";
      }
      else{
      echo "your email id is :".$email."<br>";
      }
    } ?>
  </body>
</html>
