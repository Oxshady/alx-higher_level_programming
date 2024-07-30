#!/usr/bin/node
const fs = require('fs');
const fname = process.argv[2];
const data = process.argv[3];
try {
  fs.writeFile(fname, data, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.log(err);
    }
  });
} catch (err) {
  console.log(err);
}
