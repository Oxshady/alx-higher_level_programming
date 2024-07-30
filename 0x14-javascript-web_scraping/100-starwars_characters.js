#!/usr/bin/node
const moveid = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const request = require('request');
request.get(url + moveid, { json: true }, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = body.characters;
    for (const i in characters) {
      request.get(characters[i], { json: true }, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(body.name);
        }
      });
    }
  }
});
