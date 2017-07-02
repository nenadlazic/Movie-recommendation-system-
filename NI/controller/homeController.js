MovieRecommendations.controller("homeController", ["$scope", "$rootScope", "$location", "$http", function($scope, $rootScope, $location, $http) {
    console.log(5 + 6);
    console.log($rootScope.stateLog);
    $rootScope.logeduser = "some@dom.com";
    if($rootScope.stateLog === undefined){
    	console.log("stanje undefined");

    } else {
    	console.log("stanje je defined");
    	document.getElementById("howerprop").style.text == "block";
    }
}]);


