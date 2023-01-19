#!/usr/bin/node
/*
 * Script prints "C is fine" x amount of times
 */

const process = require('process');
const arg = parseInt(process.argv[2], 10);

if (!isNaN(arg)) {
  if (arg > 0) {
    for (let i = 0; i < arg; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
