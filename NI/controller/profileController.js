MovieRecommendations.controller("profileController", ["$scope", "$rootScope", "$location", "$http", function($scope, $rootScope, $location, $http) {
    console.log(5 + 2);
    console.log("Debug5 + 2");


    $rootScope.leaveratings = function() {
	 	console.log("poziva se leaveratings komanda");
		$location.path("/leave_ratings");
	}

	 $rootScope.getrecommendation = function() {
	 	console.log("poziva se getrecommendation komanda");
		$location.path("/get_recommendation");
	}
}]);


