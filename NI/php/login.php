<?php
	include_once("connect_to_mysql.php");
	session_start();
	$args = json_decode(file_get_contents("php://input"));
	$email = $args->email;
	$password = $args->password;
	$json_response = "";
	$res=mysqli_query($myConnection, "SELECT id, password FROM users WHERE email='$email'");
	$row=mysqli_fetch_array($res);
	$count = mysqli_num_rows($res);
  if( $count == 1 && $row['password']==$password )
  {
  		$_SESSION['email'] = $email;
  		$json_response = '{"loggedin":true,"id":"' . $row[0] . '"}';
			echo $json_response;
			exit();
  }
  else {
  		$json_response = '{"loggedin":false,"id":"' . $row[0] . '"}';
  }
	$sql = "SELECT id, password FROM users WHERE email='$email'";
	$res = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));
	$row = mysqli_fetch_array($res);
	if($row[1]==$password)
  {
  		$_SESSION['email'] = $email;
  		$json_response = '{"loggedin":true,"id":"' . $row[0] . '"}';
  }
  else {
  		$json_response = '{"loggedin":false,"id":"' . $row[0] . '"}';
  }
	echo $json_response;
?>