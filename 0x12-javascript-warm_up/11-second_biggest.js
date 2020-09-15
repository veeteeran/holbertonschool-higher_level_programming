#!/usr/bin/node

const array = [];
const length = process.argv.length;
if (length > 3) {
  for (let i = 2; i < length; i++) {
    array.push(Number(process.argv[i]));
  }
  array.sort();
  array.pop();
  console.log(array.pop());
} else {
  console.log(0);
}
