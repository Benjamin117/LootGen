'use strict'

/* Controllers */

angular.module('myApp.controllers', [])

    .controller('LootGenController', function($scope, lootGenAPIservice) {


        $scope.clearInventory = function() {
            lootGenAPIservice.clearInventory($scope.result).success(function(response) {
                console.log(response)
            })

        }

        $scope.addItem = function() {
            $scope.notcollected = false;
            $scope.inventory.push($scope.result);
            var cookieString = "inventory=" + JSON.stringify($scope.inventory);
            document.cookie = cookieString;

            lootGenAPIservice.updateInventory($scope.result).success(function(response) {
                //console.log("called")
                console.log(response)

            })

        }

        $scope.getCookie = function(name) {
            var value = "; " + document.cookie;
            var parts = value.split("; " + name + "=");
            if (parts.length == 2) return parts.pop().split(";").shift();
        }

        $scope.rekCookie = function(name) {
            document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
        }

        $scope.showPersistentInventory = function() {

            lootGenAPIservice.getPersisitentInventory().success(function(response) {
                //console.log("called")
                console.log(response)
                $scope.inventory = response;

            })

            $scope.showInventory = true;
        }

        $scope.showSessionInventory = function() {
            if ($scope.getCookie('inventory') == undefined) {
                $scope.inventory = [];
            } else {
                $scope.inventory = JSON.parse($scope.getCookie('inventory'));
            }

            $scope.showInventory = true;
        }

        $scope.hideInventory = function() {
            $scope.showInventory = false;
        }

        $scope.diff = 'Difficulty'; //default
        $scope.rolltype = 'Roll Type'; //default
        var diff = null;
        if ($scope.getCookie('inventory') == undefined) {
            $scope.inventory = [];
        } else {
            $scope.inventory = JSON.parse($scope.getCookie('inventory'));
        }

        $scope.notcollected = true;
        $scope.showInventory = false;
        $scope.roll = function() {

            lootGenAPIservice.rollforLoot($scope.rolltype, $scope.diff, 1).success(function(response) {
                //console.log("called")
                console.log(response)
                $scope.result = response


                $scope.notcollected = true;




            })
        };




        $scope.decrypt = function(result) {

            result.propclass = 'Legendary-decrypted-prop';
            result.perkclass = 'Legendary-decrypted';
        }

        $scope.downloadInventory = function() {

            lootGenAPIservice.downloadInventory().then(function(response) {
                var today = new Date();
                var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
                var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
                var dateTime = date + ' ' + time;

                var fileName = 'Inventory_' + dateTime + '.xlsx'
                var blob = new Blob([response.data], {
                    type: 'application/vnd.openxmlformat-officedocument.spreadsheetml.sheet;'
                });
                saveAs(blob, fileName);

            })


        }




    })