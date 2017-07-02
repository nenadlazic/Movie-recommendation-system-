<?php 

	/*Potrebno je da se iscitaju podaci za usera ciji je mail postavljen u rootscope-u i da za njega pronajdmeo najbolje ocenjne filmove sortirano iz tog fajla ce python skripte da citaju  i izlaz upisu u fajl koji zaprvo predstavlja html koji treba prikazati tako da prakticno treba samo prekopirati taj fajl u fajl koji predstavlja view*/

	include_once("connect_to_mysql.php");
	$args = json_decode(file_get_contents("php://input"));
	$email = $args->email;

	$res=mysqli_query($myConnection, "SELECT m.actor1, m.actor2, m.actor3, m.director,m.keywords,m.title,m.genres FROM users u INNER JOIN users_ratings ur on u.id=ur.user_id INNER JOIN movies m on ur.movie_id=m.movie_id WHERE u.email LIKE '$email' ORDER BY ur.rating DESC limit 10");
	$count = mysqli_num_rows($res);
	$i = 0;
	$returnvalue = "";
	while($i < $count){
			$row=mysqli_fetch_array($res);
			$returnvalue = $returnvalue.$row['actor1']." , ".$row['actor2']." , ".$row['actor3']." , ".$row['director']." , ".$row['title']." , ".$row['keywords']." , ".$row['genres']."\n";
			$i = $i + 1;
	}


	$myfile = fopen("inputforpython.txt", "w") or die("Unable to open file!");
	fwrite($myfile, $returnvalue);
	fclose($myfile);

	echo $count;

?>