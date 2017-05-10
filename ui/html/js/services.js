'use strict'

/* Services */

angular.module('myApp.services', [])

    .factory('lootGenAPIservice', function($http) {

        function generateUID() {
            var firstPart = (Math.random() * 46656) | 0;
            var secondPart = (Math.random() * 46656) | 0;
            firstPart = ("000" + firstPart.toString(36)).slice(-3);
            secondPart = ("000" + secondPart.toString(36)).slice(-3);
            return firstPart + secondPart;
        }

        var lootGenAPI = {};

        var url = 'http://' + window.location.hostname;
        var port = ':7000';
        var endpoint = null;
        console.log(url + port);
        lootGenAPI.rollforLoot = function(rolltpye, difficulty, item_count) {

            switch (rolltpye) {
                case 'Weapon':
                    endpoint = '/rollweapon';
                    break;
                case 'Armour':
                    endpoint = '/rollarmour';
                    break;
                default:
                    if (Math.floor(Math.random() * 2) > 0.5) {
                        endpoint = '/rollweapon'
                    } else {
                        endpoint = '/rollarmour'
                    }
            }

            switch (difficulty) {
                case 'Easy':
                    difficulty = 'easy';
                    break;
                case 'Medium':
                    difficulty = 'medium';
                    break;
                case 'Hard':
                    difficulty = 'hard';
                    break;
                case 'Deadly':
                    difficulty = 'deadly';
                    break;
                default:
                    difficulty = 'easy';

            }



            return $http({
                method: 'GET',
                url: url + port + endpoint,
                params: {
                    difficulty: difficulty,
                    item_count: item_count
                }
            })
        }

        lootGenAPI.downloadInventory = function() {
            var ext = '?uid=' + generateUID()
            endpoint = '/downloadinventory'
            return $http({
                method: 'GET',
                responseType: 'arraybuffer',
                url: url + port + endpoint + ext

            })
        }

        lootGenAPI.clearInventory = function() {

            endpoint = '/clearinventory'
            return $http({
                method: 'GET',
                url: url + port + endpoint

            })
        }

        lootGenAPI.getPersisitentInventory = function() {

            endpoint = '/getinventory'
            return $http({
                method: 'GET',
                url: url + port + endpoint

            })
        }

        lootGenAPI.updateInventory = function(result) {

            endpoint = '/updateinventory'
            return $http({
                method: 'GET',
                url: url + port + endpoint,
                params: {
                    item: result
                }

            })
        }

        return lootGenAPI;
    });