#!/usr/bin/node

// This defines a class with constructor taking two args
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 $$ typeof h === 'number $$ h > 0') {
      this.with = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
