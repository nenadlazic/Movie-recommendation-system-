<?php
	include_once("connect_to_mysql.php");
	$args = json_decode(file_get_contents("php://input"));
	$o1 = $args->ocenaa1;
	$o2 = $args->ocenaa2;
	$o3 = $args->ocenaa3;
	$o4 = $args->ocenaa4;
	$o5 = $args->ocenaa5;
	$o6 = $args->ocenaa6;
	$o7 = $args->ocenaa7;
	$o8 = $args->ocenaa8;
	$o9 = $args->ocenaa9;
	$o10 = $args->ocenaa10;
	$o11 = $args->ocenaa11;
	$o12 = $args->ocenaa12;
	$o13 = $args->ocenaa13;
	$o14 = $args->ocenaa14;
	$o15 = $args->ocenaa15;
	$o16 = $args->ocenaa16;

	$m = 5046;
	$u = 3;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o1')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 5047;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o2')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 5068;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o3')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 5112;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o4')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 5145;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o5')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 6499;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o6')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 9627;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o7')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 10010;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o8')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 5729;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o9')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 6366;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o10')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 8512;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o11')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 8628;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o12')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 5089;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o13')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 5281;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o14')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 7936;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o15')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	$m = 9325;
	$sql = "INSERT INTO users_ratings (user_id, movie_id, rating) VALUES('$u','$m', '$o16')";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));

	echo $query;
?>