#!/usr/bin/node
/*
 * Script converts string to integer
 * If string has no number print "Not a number"
 */

const process = require('process');
const arg = parseInt(process.argv[2], 10);

if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log(arg);
}
