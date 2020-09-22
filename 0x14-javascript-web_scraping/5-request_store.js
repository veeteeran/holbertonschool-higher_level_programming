#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const args = process.argv.splice(2);
request(args[0], function (error, response, body) {
  if (error) {
    console.log('code: %d', response.statusCode);
  } else {
    fs.writeFileSync(args[1], body);
  }
});
