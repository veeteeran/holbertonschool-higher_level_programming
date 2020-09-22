#!/usr/bin/node
const request = require('request');
const args = process.argv.splice(2);
let count = 0;
request(args[0], function (error, response, body) {
  if (error) {
    console.log('code: %d', response.statusCode);
  } else {
    const swapi = JSON.parse(body);
    for (let i = 0; i < swapi.results.length; i++) {
      for (let j = 0; j < swapi.results[i].characters.length; j++) {
        if (swapi.results[i].characters[j].includes('18')) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
