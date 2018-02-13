(function () {
    'use strict';

    angular.module('quotemod')
        .config(['$routeProvider', config])
        .run(['$http', run]);

    function config($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '/static/html/thusSaith.html',
                controller: 'ScrumboardController',
            })
            .when('/edit', {
                templateUrl: '/static/html/edit.html',
                controller: 'ScrumboardController',
            })
            .when('/author/:authorID', {
                templateUrl: '/static/html/author.html',
                controller: 'ScrumboardController',
            })
            .when('/login', {
                templateUrl: '/static/html/login.html',
                controller: 'LoginController'
            })
            .otherwise('/');
    }

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }
})();
