/**
 * Created by sofi on 30.05.16.
 */
var app = angular.module("bulavkaApp", ['ngRoute']);

app.config(function($routeProvider, $locationProvider){

        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');

        $routeProvider
            .when('/', {
                templateUrl: '/template/home.html',
                controller: 'MainController',
            })
            .when('/about_us', {
                templateUrl: '/template/about_us.html',
                controller: 'AboutController'
            })
            .when('/articles', {
                templateUrl: '/template/articles.html',
                controller: 'ArticlesController'
            })
            .when('/contacts', {
                templateUrl: '/template/contacts.html',
                controller: 'ContactsController'
            })
            .otherwise({
                redirectTo: '/'
            }
        )
    }
);

app.run(['$rootScope', '$route', function ($rootScope, $route) {
    $rootScope.mainPageOnLoad = function () {
        $route.reload()
    };
}]);
