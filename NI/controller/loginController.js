MovieRecommendations.controller("loginController", ["$scope", "$rootScope", "$location", "$http", function($scope, $rootScope, $location, $http) {
    console.log(5 + 8);
    console.log("Debug5 + 8");

    if($rootScope.stateLog == "LogOut"){
        $rootScope.stateLog = "LogIn";
    }
 	$rootScope.loggedIn = false;
    $rootScope.loggedOut = true;
	$scope.logout = function() {
		$rootScope.loggedIn = false;
		$rootScope.loggedOut = true;
	}

	function login() {
		$rootScope.loggedIn = true;
		$rootScope.loggedOut = false;
	}
	
	$scope.login = function() {
		$rootScope.loginUserEmail = $scope.email;
        var email = $scope.email;
        var password = $scope.password;
            
        console.log(password);
        console.log(email);
        $rootScope.logeduser = $scope.email;
        console.log("provera");
        console.log($scope.email);
        var remember = $scope.rememberMe;
        if (!(remember == true))
        	remember = false;
            var request = $http({
                method: "post",
                url: "php/login.php",
                data: {
                    email: $scope.email,
                    password: $scope.password,
                    remember_me: remember
                },
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }).then(function(result_resolved) {
                        console.log("uspesno ulogovan");

                console.log(result_resolved);
                if (result_resolved.data.loggedin == true) {
					$rootScope.currentUserId = result_resolved.data.id;
                    $rootScope.stateLog = "LogOut";



                    console.log($rootScope.stateLog)
                    $location.path("/profile");
                } else {
					console.log("prihvatio else");
                    alert("Email or password incorrect");
                }
            }, function(result_rejected) {
				console.log("nije prihvatio");                
				console.log(result_rejected);
            });
        }
    }]);
