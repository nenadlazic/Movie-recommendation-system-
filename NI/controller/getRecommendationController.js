MovieRecommendations.controller("getRecommendationController", ["$scope", "$rootScope", "$location","$timeout", "$http", function($scope, $rootScope, $location,$timeout, $http) {
    console.log(5 + 7);
    console.log("Debug5 + 7");

	$timeout(function() {
	    console.log("poziva se");
		$location.path("/recommendations");

	}, 5000);



	console.log("DEBUG_N:");
	console.log($rootScope.logeduser);
	
	var request = $http({
		method: "post",
		url: "php/getrecommendation.php",
        data: {
        		email:$rootScope.logeduser
			},
        headers: {
			'Content-Type': 'application/x-www-form-urlencoded'
	        }
        }).then(function(result_resolved) {
			console.log("uspesno date preporuke");
			console.log(result_resolved);
        }, function(result_rejected) {
				console.log("nisu date preporuke");                
				console.log(result_rejected);
            });
}]);
