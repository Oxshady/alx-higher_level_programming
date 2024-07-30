#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url, { json: true }, (err, resp, body) => {
  let stars = 0;
  if (err) {
    console.log(err);
  }
  for (const film of body.results) {
    for (const character of film.characters) {
      if (character.search('18') === -1) {
        continue;
      } else {
        stars++;
      }
    }
  }
  console.log(stars);
});
