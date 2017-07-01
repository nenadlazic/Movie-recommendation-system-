MovieRecommendations.controller("chooseController", ["$scope", "$rootScope", "$location", "$http", function($scope, $rootScope, $location, $http) {
    console.log(5 + 2);
        console.log("Debug5 + 2");

	 $rootScope.submit = function() {
	 	console.log("poziva se submit komanda");


		rates1 = document.querySelector('input[name="star1"]:checked');
	 	rates2 = document.querySelector('input[name="star2"]:checked');
	 	rates3 = document.querySelector('input[name="star3"]:checked');
	 	rates4 = document.querySelector('input[name="star4"]:checked');
	 	rates5 = document.querySelector('input[name="star5"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena1 = rating;





	 	rates1 = document.querySelector('input[name="star6"]:checked');
	 	rates2 = document.querySelector('input[name="star7"]:checked');
	 	rates3 = document.querySelector('input[name="star8"]:checked');
	 	rates4 = document.querySelector('input[name="star9"]:checked');
	 	rates5 = document.querySelector('input[name="star10"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena2 = rating;


	 	rates1 = document.querySelector('input[name="star11"]:checked');
	 	rates2 = document.querySelector('input[name="star12"]:checked');
	 	rates3 = document.querySelector('input[name="star13"]:checked');
	 	rates4 = document.querySelector('input[name="star14"]:checked');
	 	rates5 = document.querySelector('input[name="star15"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena3 = rating;




	 	rates1 = document.querySelector('input[name="star16"]:checked');
	 	rates2 = document.querySelector('input[name="star17"]:checked');
	 	rates3 = document.querySelector('input[name="star18"]:checked');
	 	rates4 = document.querySelector('input[name="star19"]:checked');
	 	rates5 = document.querySelector('input[name="star20"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena4 = rating;



	 	rates1 = document.querySelector('input[name="star21"]:checked');
	 	rates2 = document.querySelector('input[name="star22"]:checked');
	 	rates3 = document.querySelector('input[name="star23"]:checked');
	 	rates4 = document.querySelector('input[name="star24"]:checked');
	 	rates5 = document.querySelector('input[name="star25"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena5 = rating;


	 	rates1 = document.querySelector('input[name="star26"]:checked');
	 	rates2 = document.querySelector('input[name="star27"]:checked');
	 	rates3 = document.querySelector('input[name="star28"]:checked');
	 	rates4 = document.querySelector('input[name="star29"]:checked');
	 	rates5 = document.querySelector('input[name="star30"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena6 = rating;



	 	rates1 = document.querySelector('input[name="star31"]:checked');
	 	rates2 = document.querySelector('input[name="star32"]:checked');
	 	rates3 = document.querySelector('input[name="star33"]:checked');
	 	rates4 = document.querySelector('input[name="star34"]:checked');
	 	rates5 = document.querySelector('input[name="star35"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena7 = rating;



	 	rates1 = document.querySelector('input[name="star36"]:checked');
	 	rates2 = document.querySelector('input[name="star37"]:checked');
	 	rates3 = document.querySelector('input[name="star38"]:checked');
	 	rates4 = document.querySelector('input[name="star39"]:checked');
	 	rates5 = document.querySelector('input[name="star40"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena8 = rating;

	 	rates1 = document.querySelector('input[name="star41"]:checked');
	 	rates2 = document.querySelector('input[name="star42"]:checked');
	 	rates3 = document.querySelector('input[name="star43"]:checked');
	 	rates4 = document.querySelector('input[name="star44"]:checked');
	 	rates5 = document.querySelector('input[name="star45"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena9 = rating;


	 	rates1 = document.querySelector('input[name="star46"]:checked');
	 	rates2 = document.querySelector('input[name="star47"]:checked');
	 	rates3 = document.querySelector('input[name="star48"]:checked');
	 	rates4 = document.querySelector('input[name="star49"]:checked');
	 	rates5 = document.querySelector('input[name="star50"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena10 = rating;



	 	rates1 = document.querySelector('input[name="star51"]:checked');
	 	rates2 = document.querySelector('input[name="star52"]:checked');
	 	rates3 = document.querySelector('input[name="star53"]:checked');
	 	rates4 = document.querySelector('input[name="star54"]:checked');
	 	rates5 = document.querySelector('input[name="star55"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena11 = rating;



	 	rates1 = document.querySelector('input[name="star56"]:checked');
	 	rates2 = document.querySelector('input[name="star57"]:checked');
	 	rates3 = document.querySelector('input[name="star58"]:checked');
	 	rates4 = document.querySelector('input[name="star59"]:checked');
	 	rates5 = document.querySelector('input[name="star60"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena12 = rating;




	 	rates1 = document.querySelector('input[name="star61"]:checked');
	 	rates2 = document.querySelector('input[name="star62"]:checked');
	 	rates3 = document.querySelector('input[name="star63"]:checked');
	 	rates4 = document.querySelector('input[name="star64"]:checked');
	 	rates5 = document.querySelector('input[name="star65"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena13 = rating;



	 	rates1 = document.querySelector('input[name="star66"]:checked');
	 	rates2 = document.querySelector('input[name="star67"]:checked');
	 	rates3 = document.querySelector('input[name="star68"]:checked');
	 	rates4 = document.querySelector('input[name="star69"]:checked');
	 	rates5 = document.querySelector('input[name="star70"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena14 = rating;


	 	rates1 = document.querySelector('input[name="star71"]:checked');
	 	rates2 = document.querySelector('input[name="star72"]:checked');
	 	rates3 = document.querySelector('input[name="star73"]:checked');
	 	rates4 = document.querySelector('input[name="star74"]:checked');
	 	rates5 = document.querySelector('input[name="star75"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);
	 	ocena15 = rating;




	 	rates1 = document.querySelector('input[name="star76"]:checked');
	 	rates2 = document.querySelector('input[name="star77"]:checked');
	 	rates3 = document.querySelector('input[name="star78"]:checked');
	 	rates4 = document.querySelector('input[name="star79"]:checked');
	 	rates5 = document.querySelector('input[name="star80"]:checked');

	 	rating = 0;
	 	if(rates1 != null){
	 		rating = 5;
	 	} else if(rates2 != null){
	 		rating = 4;
	 	} else if(rates3 != null){
	 		rating = 3;
	 	} else if(rates4 != null){
	 		rating = 2;
	 	} else if(rates5 != null){
	 		rating = 1;
	 	}

	 	console.log(rates1);
		console.log(rates2);
	 	console.log(rates3);
	 	console.log(rates4);
	 	console.log(rates5);

	 	console.log("vasa ocena za film je");
	 	console.log(rating);

	 	ocena16 = rating;


		console.log("ocene:");
	 	console.log(ocena1);
	 	console.log(ocena2);
	 	console.log(ocena3);
	 	console.log(ocena4);
	 	console.log(ocena5);
	 	console.log(ocena6);
	 	console.log(ocena7);
	 	console.log(ocena8);
	 	console.log(ocena9);
	 	console.log(ocena10);
	 	console.log(ocena11);
	 	console.log(ocena12);
	 	console.log(ocena13);
	 	console.log(ocena14);
	 	console.log(ocena15);
	 	console.log(ocena16);


		var request = $http({
		method: "post",
        url:  "php/save_ratings_init.php",
        data: {
        	ocenaa1: ocena1,
        	ocenaa2: ocena2,
        	ocenaa3: ocena3,
        	ocenaa4: ocena4,
        	ocenaa5: ocena5,
        	ocenaa6: ocena6,
        	ocenaa7: ocena7,
        	ocenaa8: ocena8,
        	ocenaa9: ocena9,
        	ocenaa10: ocena10,
        	ocenaa11: ocena11,
        	ocenaa12: ocena12,
        	ocenaa13: ocena13,
        	ocenaa14: ocena14,
        	ocenaa15: ocena15,
        	ocenaa16: ocena16
        	},
		headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
		});


		request.then(function (data) {
        		console.log("Uspesno sacuvani podaci");
        		console.log(data);
        		setTimeout(
				    function() {
				    	alert("Ocene su upisane u bazu.")
						
					}, 1000);
        		$location.path("/profile");
            });



	 }
}]);


