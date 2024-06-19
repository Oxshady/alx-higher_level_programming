#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let sym = '', leng = 0;
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
