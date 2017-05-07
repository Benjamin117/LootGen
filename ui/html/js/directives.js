
'use strict'

/* Directives */

angular.module('myApp.directives', [])

  .directive('weaponRow', function () {

    return {
    	restrict: 'E',
    	templateUrl: '/partials/weapon-row.html',
      scope: {'result':'=result'}
    	
    	
    	
  };
  })
  .directive('armourRow', function () {

    return {
    	restrict: 'E',
    	templateUrl: '/partials/armour-row.html',
      scope: {'result':'=result'}
      
    	
    	
    	
  };
  })

 