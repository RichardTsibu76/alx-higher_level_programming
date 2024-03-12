#!/usr/bin/node

let cal = 0;

exports.logMe = function cal (item) {
  console.log(`${cal}: ${item}`);
  cal += 1;
};
