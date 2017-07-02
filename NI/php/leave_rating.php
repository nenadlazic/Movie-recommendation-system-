<?php
	include_once("connect_to_mysql.php");
	$args = json_decode(file_get_contents("php://input"));

	$email = $args->email;

	$sql = "SELECT users.id FROM `users` WHERE email LIKE '$email'";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));
	$row=mysqli_fetch_array($query);

	$u = (int)$row['id'];

	$a1 = $args->actor1;
	$a2 = $args->actor2;
	$a3 = $args->actor3;
	$d = $args->director;
	$g = $args->genres;
	$k = $args->hashtags;
	$t = $args->title;
	$r = $args->rating;



	$sql = "INSERT INTO `movies`(`actor1`, `actor2`, `actor3`, `director`, `keywords`, `genres`, `title`) VALUES ('$a1','$a2','$a3','$d','$k','$g','$t')";
	$res = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));



	$sql = "SELECT movies.movie_id FROM `movies` WHERE title LIKE '$t'";
	$query = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));
	$row=mysqli_fetch_array($query);

	$id = (int)$row['movie_id'];

	$sql = "INSERT INTO `users_ratings`(`user_id`, `movie_id`, `rating`) VALUES ('$u','$id','$r')";
	$res = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));


	echo $u;

?>