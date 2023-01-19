#!/usr/bin/node
/*
 * The script prints the first argument passed
 * to it, if no argument passed print "no argument"
 */

const process = require('process');
const args = process.argv;

if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
