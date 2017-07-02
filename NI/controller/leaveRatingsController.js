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
        var rating = $scope.rat_rating;

    	console.log(title);
    	console.log(actor1);
    	console.log(actor2);
    	console.log(actor3);
    	console.log(director);
    	console.log(hashtags);
    	console.log(genres);
        console.log(rating);

        var request = $http({
            method: "post",
            url: "php/leave_rating.php",
            data: {
                email: $rootScope.logeduser,
                title: title,
                actor1: actor1,
                actor2: actor2,
                actor3: actor3,
                director: director,
                hashtags:hashtags,
                genres:genres,
                rating: rating
            },
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        }).then(function(result_resolved) {
            console.log("uspesno upisana ocena");

            console.log(result_resolved);
            $location.path("/leave_ratings");
            alert("Uspesno upisana ocena. Hvala na oceni filma");
        }, function(result_rejected) {
            console.log("nije upisano");                
            console.log(result_rejected);
        });
        }        
    }]);
