#!/usr/bin/node
const fs = require('fs');
const args = process.argv.splice(2);
fs.writeFileSync(args[0], args[1]);
