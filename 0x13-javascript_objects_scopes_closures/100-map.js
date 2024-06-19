#!/usr/bin/node
const list = require('./100-data').list;
const newl = list.map((val, ind) => val * ind);

console.log(list);
console.log(newl);
