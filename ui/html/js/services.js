
'use strict'

/* Services */

angular.module('myApp.services', [])

.factory('lootGenAPIservice', function($http) {
    
    var lootGenAPI = {};

    lootGenAPI.rollforLoot = function(difficulty,item_count) {
     
      return $http({
        method: 'GET', 
        url: 'http://192.168.1.2:81/roll',
        params: {difficulty: difficulty,
        		item_count:item_count}
      })
    }

    return lootGenAPI;
  });
