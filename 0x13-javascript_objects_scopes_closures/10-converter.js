#!/usr/bin/node

exports.converter = function (base) {
  function convertFunction (n) {
    return n.toString(base);
  }

  return convertFunction;
};
