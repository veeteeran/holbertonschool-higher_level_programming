#!/usr/bin/node
// prints the number of arguments already printed and the new argument value
var printed = 0;
exports.logMe = function (item) {
  console.log(printed + ': ' + item);
  printed++;
};
