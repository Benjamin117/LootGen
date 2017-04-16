'use strict'

/* Services */

angular.module('myApp.services', [])

.factory('lootGenAPIservice', function($http) {
    
    var lootGenAPI = {};
    
    var url = 'http://'+window.location.hostname;
    var port = ':33002';
    var endpoint = null;
    console.log(url+port);
    lootGenAPI.rollforLoot = function(rolltpye,difficulty,item_count) {

     switch(rolltpye) {
    case 'Weapon':
        endpoint = '/rollweapon';
        break;
    case 'Armour':
        endpoint='/rollarmour';
        break;
    default:
        if(Math.floor(Math.random() * 2)>0.5){
        endpoint='/rollweapon'
      }else{endpoint='/rollarmour'}
}

switch(difficulty) {
    case 'Easy':
        difficulty = 'easy';
        break;
    case 'Medium':
        difficulty='medium';
        break;
    case 'Hard':
        difficulty='hard';
        break;
    case 'Deadly':
        difficulty='deadly';
        break;
    default:
        difficulty = 'easy';
        
}


     
      return $http({
        method: 'GET', 
        url: url+port+endpoint,
        params: {difficulty: difficulty,
            item_count:item_count}
      })
    }

    return lootGenAPI;
  });