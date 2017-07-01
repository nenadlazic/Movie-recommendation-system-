<?php
	$myfile = fopen("C:/Users/nlazic/Desktop/final_final/NI_final/TMP/inputdata.txt", "w") or die("Unable to open file!");
	$txt = "John Doe\n";
	fwrite($myfile, $txt);
	$txt = "Jane Doe\n";
	fwrite($myfile, $txt);
	fclose($myfile);
	echo "alohahahahahahah"
?>