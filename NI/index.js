var MovieRecommendationConfig = function($routeProvider){
	$routeProvider
	.when('/',{
		controller: 'homeController',
		templateUrl: 'view/homeView.html'
	})
	.when('/about',{
		controller: 'aboutController',
		templateUrl: 'view/aboutView.html'
	})	
	.when('/contact',{
		controller: 'contactController',
		templateUrl: 'view/contactView.html'
	})
	.when('/login',{
		controller: 'loginController',
		templateUrl: 'view/loginView.html'
	})
	.when('/signup',{
		controller: 'signupController',
		templateUrl: 'view/signupView.html'
	})
	.when('/terms',{
		controller: 'signupController',
		templateUrl: 'view/terms.html'
	})
	.when('/choose',{
		controller: 'chooseController',
		templateUrl: 'view/chooseView.html'
	})
	.when('/profile',{
		controller: 'profileController',
		templateUrl: 'view/profileView.html'
	})
	.when('/leave_ratings',{
		controller: 'leaveRatingsController',
		templateUrl: 'view/leaveRatingsView.html'
	})
	.when('/get_recommendation',{
		controller: 'getRecommendationController',
		templateUrl: 'view/getRecommendationView.html'
	})
	.when('/recommendations',{
		controller: 'recommendationsController',
		templateUrl: 'view/recommendationsView.html'
	})
}

//ovime definisemo namespace prakticno modul koji predstavlja namespace za ovu aplikaciju pa druga aplikacija moze koristiti ista imena kao ovde
var MovieRecommendations = angular.module('MovieRecommendation', ['ngRoute']).config(MovieRecommendationConfig);

//ovime podesavamo da u rutu ne ubacvuje #! itd i ne prepoznaje rute
MovieRecommendations.config(['$locationProvider', function($locationProvider) {
  	$locationProvider.hashPrefix('');
}]);

MovieRecommendations.constant('stateLog', "login");