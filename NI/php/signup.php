<?php
	include_once("connect_to_mysql.php");
	$args = json_decode(file_get_contents("php://input"));
	$email = $args->email;
	$password = $args->pass;
	$phone = $args->phone;
	$fname = $args->first_name;
	$lname = $args->last_name;
	$userType = $args->profile_type;
	$country = $args->country;
	$gender = $args->gender;
		$sql = "INSERT INTO users (first_name, last_name, email, password, phone, country, gender) VALUES('$fname', '$lname', '$email', '$password', '$phone', '$country', '$gender')";
		$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));
?>