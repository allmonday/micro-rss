var app = angular.module('myApp', []);

app.controller('feedlist', ['$scope', '$http', function ($scope, $http ) {
	$http.get('./rss.json')
		.success(function (data, status, headers, config) {
			$scope.items = data;
		})
}])