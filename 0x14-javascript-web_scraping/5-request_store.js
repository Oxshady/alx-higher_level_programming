#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fname = process.argv[3];
request.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(fname, body, { encoding: 'utf-8' }, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
