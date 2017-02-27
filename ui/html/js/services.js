'use strict'

/* Services */

angular.module('myApp.services', [])

.factory('lootGenAPIservice', function($http) {
    
    var lootGenAPI = {};
    
    var url = 'http://'+window.location.hostname;
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