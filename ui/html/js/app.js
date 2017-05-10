'use strict';


// Declare app level module which depends on views, and components
angular.module('myApp', [
        'ngRoute',
        'myApp.controllers',
        'myApp.services',
        'myApp.directives'
    ])

    .config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {

        $routeProvider.otherwise({
            redirectTo: '/'
        });
    }]);