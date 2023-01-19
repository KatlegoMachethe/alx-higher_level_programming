#!/usr/bin/node
/**
 * Prints a square with character "X" where the input
 * argument is the size of the square. For instance if the
 * input is 2, we'll have:
 * XX
 * XX
 */

const process = require('process');
const size = process.argv[2];

if (parseInt(size)) {
  let mark = '';
  for (let i = 0; i < size; i++) {
    mark += 'X';
  }
  for (let j = 0; j < size; j++) {
    console.log(mark);
  }
} else {
  console.log('Missing size');
}
