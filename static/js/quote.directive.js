(function(){
    'use strict';

    angular.module('quotemod')
        .directive('quotedriverQuote', QuoteDirective);

    function QuoteDirective() {
        return {
            templateUrl: '/static/html/quote.html',
            //restrict: 'E',
            controller: ['$scope', '$http', function($scope, $http) {
                var url = '/quotedriver/quotes/' + $scope.quote.id + '/';
                $scope.destAuthor = $scope.author;
                // $scope.update = function() {
                //     return $http.put(
                //         url,
                //         $scope.quote
                //     );
                // };

                function removeQuoteFromAuthor(quote, author) {
                    var quotes = author.quotes;
                    quotes.splice(
                        quotes.indexOf(quote),
                        1
                    );
                }

                $scope.delete = function() {
                    $http.delete(url).then(
                        function(){
                            removeQuoteFromAuthor($scope.quote, $scope.author);
                        }
                    );
                };

                $scope.modelOptions = {
                    debounce: 500
                };

                $scope.move = function() {
                    if ($scope.destAuthor === undefined) {
                        return;
                    }
                    $scope.quote.author = $scope.destAuthor.id;
                    $scope.update().then(function() {
                        {
                            removeQuoteFromAuthor($scope.quote, $scope.author);
                            $scope.destAuthor.quotes.push($scope.quote);
                        }
                    });
                }
            }]
        };
    }
})();
