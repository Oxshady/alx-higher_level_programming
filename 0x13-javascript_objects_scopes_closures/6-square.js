#!/usr/bin/node
const Squaree = require('./5-square');
class Square extends Squaree {
  charPrint (c) {
    let sym = '';
    let leng = 0;
    if (c === undefined) {
      c = 'X';
    }
    while (leng < this.width) {
      sym += c;
      leng++;
    }
    leng = 0;
    while (leng < this.height) {
      console.log(sym);
      leng++;
    }
  }
}
module.exports = Square;
