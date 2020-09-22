#!/usr/bin/node
const request = require('request');
const args = process.argv.splice(2);
request
  .get(args[0])
  .on('response', function (response) {
    console.log('code: %d', response.statusCode);
  }
  );
