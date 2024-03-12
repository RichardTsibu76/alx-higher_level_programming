#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = []; // The empty list to be used using the push
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  return (reversedList);
};
