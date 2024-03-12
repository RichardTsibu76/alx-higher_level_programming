#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let check = 0;

  for (let i = 0; i < list.length; i++) { // Using for loop to iterate through the list
    check = (list[i] === searchElement ? check + 1 : check);
  }

  return check;
};
