#!/usr/bin/node
/*
imports a dictionary of occurrences by user id and computes
a dictionary of user ids by occurrence
*/
const dict = require('./101-data').dict;
let newDict = {};
for (let key in dict) {
	let newKey = dict[key];
	if (newKey in newDict) {
		newDict[newKey].push(key)
	} else {
		newDict[newKey] = [key];
	}
}
console.log(newDict);
