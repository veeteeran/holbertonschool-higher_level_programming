#!/usr/bin/node
// class Rectangle that defines a rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (w < 0 || w === undefined || h < 0 || h === undefined) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  // prints the rectangle using the character X
  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }

  // exchanges the width and the height of the rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // multiples the width and the height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
