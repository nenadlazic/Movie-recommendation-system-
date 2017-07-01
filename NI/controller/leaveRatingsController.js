MovieRecommendations.controller("leaveRatingsController", ["$scope", "$rootScope", "$location", "$http", function($scope, $rootScope, $location, $http) {
    console.log(5 + 7);
    console.log("Debug5 + 7");

	$scope.subrating = function() {
		var email = $rootScope.logeduser;
    	var title = $scope.rat_title;
    	var actor1 = $scope.rat_actor1;
    	var actor2 = $scope.rat_actor2;
    	var actor3 = $scope.rat_actor3;
    	var director = $scope.rat_director;
    	var hashtags = $scope.rat_hash_tags;
    	var genres = $scope.rat_genres;

    	console.log(title);
    	console.log(actor1);
    	console.log(actor2);
    	console.log(actor3);
    	console.log(director);
    	console.log(hashtags);
    	console.log(genres);
            
    }
}]);
