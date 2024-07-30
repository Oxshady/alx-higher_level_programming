#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], { json: true }, (error, response, body) => {
  if (error) console.log(error);
  else {
    names(body.characters, 0);
  }
});

function names (character, i) {
  if (i >= character.length) {
    return;
  }
  request(character[i], { json: true }, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(body.name);
      return names(character, ++i);
    }
  });
}
