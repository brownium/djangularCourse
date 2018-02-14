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
                $scope.destList = $scope.list;
                // $scope.update = function() {
                //     return $http.put(
                //         url,
                //         $scope.quote
                //     );
                // };

                function removeQuoteFromList(quote, list) {
                    var quotes = list.quotes;
                    quotes.splice(
                        quotes.indexOf(quote),
                        1
                    );
                }

                $scope.delete = function() {
                    $http.delete(url).then(
                        function(){
                            removeQuoteFromList($scope.quote, $scope.list);
                        }
                    );
                };

                $scope.modelOptions = {
                    debounce: 500
                };

                $scope.move = function() {
                    if ($scope.destList === undefined) {
                        return;
                    }
                    $scope.quote.list = $scope.destList.id;
                    $scope.update().then(function() {
                        {
                            removeQuoteFromList($scope.quote, $scope.list);
                            $scope.destList.quotes.push($scope.quote);
                        }
                    });
                }
            }]
        };
    }
})();
