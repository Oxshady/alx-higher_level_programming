#!/usr/bin/node
const moveid = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const request = require('request');
request.get(url + moveid, { json: true }, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    for (const i in body.characters) {
      request.get(body.characters[i], { json: true }, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(body.name);
        }
      });
    }
  }
});
