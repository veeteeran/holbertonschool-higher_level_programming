#!/usr/bin/node

const length = process.argv.length;
process.argv.splice(0, 2);
if (length > 3) {
  process.argv.sort(function (a, b) { return b - a; });
  console.log(process.argv[1]);
} else {
  console.log(0);
}
