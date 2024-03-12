#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = []; // The empty list to be used using the push
  for (let n = list.length - 1; n >= 0; n--) {
    reversedList.push(list[n]);
  }

  return (reversedList);
};
