/**
 * Created by markel on 16.08.16.
 */

app.controller('ArticlesController', function($scope, $http) {
    $scope.items = [];


    $http.get('./scripts/json/item-example.json')
        .success(function(responce) {
            $scope.items = responce;
        }
    );

});