#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (err, resp) => {
  if (err) {
    return
  } else {
    console.log(resp.statusCode);
  }
});
