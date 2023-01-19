#!/usr/bin/node
/**
 * Prints the addition of two integer input arguments
 */

const process = require('process');

function add (a, b) {
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);
  console.log(a + b);
}

add();
