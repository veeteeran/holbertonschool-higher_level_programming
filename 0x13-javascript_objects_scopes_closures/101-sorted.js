#!/usr/bin/node
/*
imports a dictionary of occurrences by user id and computes
a dictionary of user ids by occurrence
*/
const dict = require('./101-data').dict;
let newDict = {};
const list1 = [];
const list2 = [];
const list3 = [];
for (const key in dict) {
  const value = dict[key];
  if (value === 1) {
    list1.push(key);
  } else if (value === 2) {
    list2.push(key);
  } else {
    list3.push(key);
  }
}

newDict = {
  1: list1,
  2: list2,
  3: list3
};
console.log(newDict);
