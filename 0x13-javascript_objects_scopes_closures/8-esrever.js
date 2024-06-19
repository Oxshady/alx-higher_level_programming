#!/usr/bin/node
exports.esrever = function (list) {
  let length = list.length - 1; const tmp = [];
  while (length >= 0) {
    tmp.push(list[length]);
    length--;
  }
  return tmp;
};
