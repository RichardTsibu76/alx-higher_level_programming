#!/usr/bin/node

const cal = 0;

exports.logMe = function count (item) {
  console.log(`${cal}: ${item}`);
  cal += 1;
};
