#!/usr/bin/node
const fs = require('fs');
const args = process.argv.splice(2);
fs.readFile(args[0], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(`${data}`);
  }
});
