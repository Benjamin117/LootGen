
'use strict'

/* Controllers */

angular.module('myApp.controllers', [])

.controller('LootGenController', function($scope, lootGenAPIservice) {

    $scope.diff='Difficulty'; //default
    $scope.rolltype='Roll Type'; //default
   var diff= null;
	$scope.roll=function(){
	               
		lootGenAPIservice.rollforLoot($scope.rolltype,$scope.diff,1).success(function (response) {
        //console.log("called")
        console.log(response)
        $scope.result = response
        if($scope.result['Special Properties'] =='none'){
        	 $scope.specialprop = false;

        }else {$scope.specialprop = $scope.result['Special Properties']}
        $scope.pperkr = 'none';
        $scope.sperkr = 'none';
        if($scope.result.pperkrarity!=='none'){
        	$scope.isperk = true;
        	$scope.pperkr = $scope.result.pperkrarity;
        	$scope.sperkr = $scope.result.sperkrarity;
        	if($scope.result.secondaryperk!=='none'){
        	$scope.secperk = true;

        }else{
        	$scope.secperk = false;

        }
        }else{
        	$scope.isperk = false;
        	
        }
        
        
        
        $scope.propclass='none'
        $scope.perkclass = 'none'

    if($scope.pperkr=='none'||$scope.sperkr=='none'){$scope.perkclass='none'}; //Black
	if($scope.pperkr=='Common perks'||$scope.sperkr=='Common perks'){$scope.perkclass='Common'}; // Green
	if($scope.pperkr=='Uncommon perks'||$scope.sperkr=='Uncommon perks'){$scope.perkclass='Uncommon'}; // Blue
	if($scope.pperkr=='Rare perks'||$scope.sperkr=='Rare perks'){$scope.perkclass='Rare'}; // Red
	if($scope.pperkr=='Very rare perks'||$scope.sperkr=='Very rare perks'){$scope.perkclass='Vrare'}; // Purple
	if($scope.pperkr=='Legendary perks'||$scope.sperkr=='Legendary perks'){$scope.perkclass='Legendary'
										 $scope.propclass='Legendary'}; // Gold

	$scope.pperkname = $scope.result.primaryperk+","+" "+$scope.result.pperkrarity.substring(0, $scope.result.pperkrarity.length - 1)+": "
	$scope.sperkname = $scope.result.secondaryperk+","+" "+$scope.result.sperkrarity.substring(0, $scope.result.sperkrarity.length - 1)+": "
	
	
      
    })};
		$scope.decrypt = function(){

			$scope.propclass='Legendary-decrypted-prop';
			$scope.perkclass='Legendary-decrypted';
		}

		
 

  })






  