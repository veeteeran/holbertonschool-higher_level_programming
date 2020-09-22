#!/usr/bin/node
const request = require('request');
const args = process.argv.splice(2);
const returnDict = {};
request(args[0], function (error, response, body) {
  if (error) {
    console.log('code: %d', response.statusCode);
  } else {
    const obj = JSON.parse(body);
    for (let i = 0; i < obj.length; i++) {
      if (!returnDict[obj[i].userId] && obj[i].completed) {
        returnDict[obj[i].userId] = 0;
      }
      if (obj[i].completed) {
        returnDict[obj[i].userId]++;
      }
    }
    console.log(returnDict);
  }
});
