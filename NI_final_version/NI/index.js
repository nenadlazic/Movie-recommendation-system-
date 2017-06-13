var movieRecommendation = function($routeProvider){
	$routeProvider
	.when('/',{
		controller: 'controller/homeController',
		templateUrl: 'view/homeView.html'
	})
	
}