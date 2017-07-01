<?php include_once("php/connect_to_mysql.php"); 
	/*if(!isset($_SESSION['email']))
		header('Location: exploreserbia.php');
	*/
?>

<!DOCTYPE>
<!DOCTYPE html>
<html ng-app="MovieRecommendation">
<head>
	<title>Movie Recommendation</title>

	<!--Meta data-->
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"></meta>	
	<meta http-equiv="Content-Script-Type" content="text/javascript"></meta>
	<meta name='author' content='Nenad Lazić'></meta>
	<meta name='generator' content='Sublime Text 2'></meta>
	<meta name='description' content='Seminarski rad studenta 1092/2015 iz predmeta Naucno izracunavanje na temu MovieRecommendation'></meta>
	<meta name='keywords' content='Nenad Lazić,NI,seminarski,2017,matf, movie, recommendation,neural,network,tensorflow,clustering'></meta>
	<meta name='language' content='EN'></meta>
	
	<!-- load bootstrap and fontawesome via CDN -->
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" />
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/font-awesome/4.0.0/css/font-awesome.css" />
	<link rel="stylesheet" href="//netdna.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css">

	<!--JS-->
	<title>Movie Recommendation</title>
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.4/angular.min.js"></script>
	<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/angularjs/1.6.4/angular-route.js"</script>
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.4/angular-resource.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

	<!--JavaScript za rute i ostale konfiguracije angular aplikacije-->
	<script type="text/javascript" src="index.js"></script>

	<!--Ukljucujemo controllere-->
	<script type="text/javascript" src="controller/homeController.js"></script>
	<script type="text/javascript" src="controller/aboutController.js"></script>
	<script type="text/javascript" src="controller/contactController.js"></script>
	<script type="text/javascript" src="controller/loginController.js"></script>
	<script type="text/javascript" src="controller/signupController.js"></script>
	<script type="text/javascript" src="controller/chooseController.js"></script>
	<script type="text/javascript" src="controller/profileController.js"></script>
	<script type="text/javascript" src="controller/leaveRatingsController.js"></script>
	<script type="text/javascript" src="controller/getRecommendationController.js"></script>
	<script type="text/javascript" src="controller/recommendationsController.js"></script>

	<!--Ukljucujemo stil-->
	<link rel="stylesheet" type="text/css" href="view/styles.css">

</head>
<body class="Site">

	<!--HEADER-->

	<header>
		<!--mozes da dodas da pripada dvema klasama pri cemu je druga klasa redefinisana u style.css promena boje -->
        <nav class="navbar navbar-default navbar-custom">
	        <div class="container">
	        	<div class="navbar-header">
	        		<a class="navbar-brand" style = "color:white" href="#/">
                	<img src = "images/logo.png" width = "150" height = "45" style = "margin-top:-10px">
                </a>
	            </div>

				<ul class="nav navbar-nav navbar-right">
	            	<li><a href="#" id="txt_color"><i class="fa fa-home ch_t_color"></i> <span id="howerprop">Home</span></a></li>
	                <li><a href="#about" id="txt_color"><i class="fa fa-shield ch_t_color"></i><span id="howerprop"> About</span></a></li>
	                <li><a href="#contact" id="txt_color"><i class="fa fa-comment ch_t_color"></i><span id="howerprop"> Contact</span></a></li>
	                <li ng-show="stateLog === undefined"><a href="#login" id="txt_color"><i class="fa fa-sign-in ch_t_color"></i><span id="howerprop" > LogIn</span></a></li>
					<li ng-show="stateLog == 'LogOut'"><a href="#profile" id="txt_color"><i class="glyphicon glyphicon-user ch_t_color"></i><span id="howerprop"> Profile</span></a></li>
	                <li ng-show="stateLog === undefined"><a href="#signup" id="txt_color"><i class="glyphicon glyphicon-registration-mark ch_t_color"></i><span id="howerprop"> SignUp</span></a></li>
	                <li ng-show="stateLog != undefined"><a href="#login" id="txt_color"><i class="glyphicon glyphicon-log-out ch_t_color"></i><span id="howerprop"> {{stateLog}}</span></a></li>
	                <li ng-show="stateLog != 'LogOut' && stateLog != undefined"><a href="#signup" id="txt_color"><i class="glyphicon glyphicon-registration-mark ch_t_color"></i><span id="howerprop"> SignUp</span></a></li>				
				</ul>	
			</div>
		</nav>
	</header>


	<!--CONTENT-->

	<div ng-view id="content" class="Site-content"> <!--U ovoj div ce se dodavati vievi odn templatei kako se izvrsava nasa aplikacija, zna koji view da loaduje zavisno od rute na kojoj se nalazi-->
			
	</div> 



	<!--FOOTER-->

	<footer id="footerid">
  		<p>Posted by: Nenad Lazic</p>
  		<p>Contact information: <a href="mailto:nenadlazic13@gmail.com">nenadlazic13@gmail.com</a>.</p>
	</footer>

</body>
</html>