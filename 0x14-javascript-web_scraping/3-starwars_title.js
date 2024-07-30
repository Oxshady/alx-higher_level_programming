#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];
if (id) {
  request.get(url + id, { json: true }, (err, resp, body) => {
    if (err) {
      console.log(err);
    }
    console.log(body.title);
  });
}
