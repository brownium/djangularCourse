(function(){
    'use strict';

    angular.module('quotemod', ['ngRoute'])
        .controller('QuoteDriverController',
            [ '$scope', '$http', '$routeParams', 'Login', QuoteDriverController]);

    function QuoteDriverController($scope, $http, $routeParams, Login) {
        $scope.add = function (author, title) {
            var quote = {
                author: author.id,
                title: title
            };
            $http.post('/quotedriver/quotes/', quote)
                .then(function(response){
                    author.quotes.push(response.data);
                },
                function(){
                    alert('Could not create quote');
                });
        };

        //Login.redirectIfNotLoggedIn();
        $scope.isLoggedIn = Login.isLoggedIn();
        $scope.data = [];
        $scope.logout = Login.logout;
        $scope.sortBy="category";
        $scope.reverse=false;
        $scope.showFilters=false;

        $http.get('/quotedriver/authors/')
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
