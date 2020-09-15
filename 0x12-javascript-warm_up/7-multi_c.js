#!/usr/bin/node

const index = process.argv[2];

if (!Number(index)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < index; i++) {
    console.log('C is fun');
  }
}
