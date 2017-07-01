<?php
// the message
$args = json_decode(file_get_contents("php://input"));
$name = $args->name;
$email = $args->email;
$phone = $args->phone;
$sub = $args->sub;
$msg = $args->msg;

// use wordwrap() if lines are longer than 70 characters
$msg = wordwrap($msg,70);

// send email
mail("nenadlazic13@gmail.com",$sub,$msg);
?>