
'use strict'

/* Services */

angular.module('myApp.services', [])

.factory('lootGenAPIservice', function($http) {
    
    var lootGenAPI = {};
    var loc = window.location.href
    var url = loc.substring(0, loc.length - 1);
    var port = ':33002';
    console.log(url+port);
    lootGenAPI.rollforLoot = function(difficulty,item_count) {
     
      return $http({
        method: 'GET', 
        url: url+port+'/roll',
        params: {difficulty: difficulty,
        		item_count:item_count}
      })
    }

    return lootGenAPI;
  });
