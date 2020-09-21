#!/usr/bin/node
// prints the number of arguments already printed and the new argument value
let printed = 0;
exports.logMe = function (item) {
  console.log(printed + ': ' + item);
  printed++;
};
