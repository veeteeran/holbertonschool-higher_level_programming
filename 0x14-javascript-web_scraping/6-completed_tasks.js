#!/usr/bin/node
const request = require('request');
const args = process.argv.splice(2);
const returnDict = {};
request(args[0], function (error, response, body) {
  if (error) {
    console.log('code: %d', response.statusCode);
  } else {
    const obj = JSON.parse(body);
    let count = 0;
    let userId = 1;
    for (let i = 0; i < obj.length; i++) {
      if (obj[i].completed) {
        count++;
        returnDict[obj[i].userId] = count;
      }
      if (obj[i].userId !== userId) {
        count = 0;
        userId++;
      }
    }
  }
  console.log(returnDict);
});
