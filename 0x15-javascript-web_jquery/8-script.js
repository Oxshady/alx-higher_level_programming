$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
	data.results.forEach(function(title) {
		$('#list_movies').append('<li>' + title.title + '</li>');
	});
})