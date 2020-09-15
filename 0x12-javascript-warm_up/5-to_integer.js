#!/usr/bin/node

if (process.argv.length < 3 || !Number(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: %s', Math.floor(Number(process.argv[2])));
}
