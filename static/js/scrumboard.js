(function(){
    'use strict';

    angular.module('scrumboard.demo', ['ngRoute'])
        .controller('ScrumboardController',
            [ '$scope', '$http', '$routeParams', 'Login', ScrumboardController]);

    function ScrumboardController($scope, $http, $routeParams, Login) {
        $scope.add = function (list, title) {
            var card = {
                list: list.id,
                title: title
            };
            $http.post('/scrumboard/cards/', card)
                .then(function(response){
                    list.cards.push(response.data);
                },
                function(){
                    alert('Could not create card');
                });
        };

        //Login.redirectIfNotLoggedIn();
        $scope.isLoggedIn = Login.isLoggedIn();
        $scope.data = [];
        $scope.logout = Login.logout;
        $scope.sortBy="title";
        $scope.reverse=false;
        $scope.showFilters=false;

        $http.get('/scrumboard/lists/')
            .then(function(response){
                $scope.data = response.data;
                if ($routeParams.authorID) {
                    for (var i = 0; i < $scope.data.length; i++) {
                        if ($scope.data[i].id == $routeParams.authorID) {
                            $scope.data=$scope.data[i];
                        }
                    }
                }
            }
        );
    }
}());
