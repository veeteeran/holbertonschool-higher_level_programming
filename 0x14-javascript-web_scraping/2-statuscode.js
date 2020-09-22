#!/usr/bin/node
const request = require('request');
const args = process.argv.splice(2);
request(args[0], function (error, response, body) {
  if (error) {
    console.log('code: %d', response.statusCode);
  } else {
    console.log('code: %d', response.statusCode);
  }
});
