var app = angular.module('myApp', []);

app.controller('feedlist', ['$scope', '$http', function ($scope, $http ) {
	$http.get('./rss.json')
		.success(function (data, status, headers, config) {
			$scope.articles = data.map(function (item) {
				item.date = new Date(item.date);
				return item;
			});
			$scope.predicate = '-date';
			$scope.authorList = $scope.articles.reduce(function (prev, curr) {
				console.log(curr);
				if (!(prev[curr.author])) {
					prev[curr.author] = true;
				}
				return prev;
			}, {})
		})
}])
