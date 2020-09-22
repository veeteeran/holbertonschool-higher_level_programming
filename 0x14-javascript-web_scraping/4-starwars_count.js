#!/usr/bin/node
const request = require('request');
const args = process.argv.splice(2);
let count = 0;
const wedge = 'https://swapi-api.hbtn.io/api/people/18/';
request(args[0], function (error, response, body) {
  if (error) {
    console.log('code: %d', response.statusCode);
  } else {
    const swapi = JSON.parse(body);
    for (let i = 0; i < swapi.results.length; i++) {
      if (swapi.results[i].characters.includes(wedge)) {
        count++;
      }
    }
  }
  console.log(count);
});
