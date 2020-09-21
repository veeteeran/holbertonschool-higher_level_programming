#!/usr/bin/node
const fs = require('fs');
const args = process.argv.splice(2);
fs.readFile(args[0], 'utf8', (err, data) => fs.writeFileSync(args[2], data));
fs.readFile(args[1], 'utf8', (err, data) => fs.writeFileSync(args[2], data, { flag: 'a+' }));
