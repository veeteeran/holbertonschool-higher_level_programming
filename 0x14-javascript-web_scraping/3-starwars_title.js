#!/usr/bin/node
const request = require('request');
const args = process.argv.splice(2);
const url = 'https://swapi-api.hbtn.io/api/films/' + args[0];
request(url, function (error, response, body) {
  if (error) {
    console.log('code: %d', response.statusCode);
  } else {
    const obj = JSON.parse(body);
    console.log(obj.title);
  }
});
