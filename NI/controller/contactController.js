MovieRecommendations.controller("contactController", ["$scope", "$rootScope", "$location", "$http", function($scope, $rootScope, $location, $http) {
    console.log(5 + 3);
	console.log("Debug5 + 3");

	$scope.sendemail = function() {
		console.log("poziva se");

		var name1 = $scope.namec;
		var email1 = $scope.emailc;
		var mobile1 = $scope.mobilec;
		var sub1 = $scope.subc;
		var msg1 = $scope.msgc;

		console.log(name1);
		console.log(email1);
		console.log(mobile1);
		console.log(sub1);
		console.log(msg1);

		var request = $http({
                method: "post",
                url: "php/send_email.php",
                data: {
					name:name1,
					email:email1,
					phone:mobile1,
					sub:sub1,
					msg:msg1
                },
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }).then(function(result_resolved) {
                    console.log("uspesno poslata");
	                console.log(result_resolved);
                    $location.path("/profile");
            }, function(result_rejected) {
				console.log("nije prihvatio");                
				console.log(result_rejected);
            });


	}



}]);


