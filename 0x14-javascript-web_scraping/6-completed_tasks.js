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
        if (obj[i].userId === userId) {
          count++;
          returnDict[obj[i].userId] = count;
        } else {
          count = 0;
          userId++;
          returnDict[obj[i].userId] = count;
        }
      }
    }
  }
  console.log(returnDict);
});
