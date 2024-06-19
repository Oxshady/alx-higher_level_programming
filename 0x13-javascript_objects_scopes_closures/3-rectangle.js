#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = 0; let sym = '';
    while (x < this.width) {
      sym += 'X';
      x++;
    }
    x = 0;
    while (x < this.height) {
      console.log(sym);
      x++;
    }
  }
}
module.exports = Rectangle;
