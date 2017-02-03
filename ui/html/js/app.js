'use strict';


// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'myApp.controllers',
  'myApp.services'
])

.config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  
  $routeProvider.otherwise({redirectTo: '/'});
}]);

