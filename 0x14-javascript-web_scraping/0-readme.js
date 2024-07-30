#!/usr/bin/node
const arg = process.argv[2];
if (arg) {
  const fs = require('fs');
  fs.readFile(arg, { encoding: 'utf-8' }, (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
}
