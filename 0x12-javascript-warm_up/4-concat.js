#!/usr/bin/node
/*
 * Script prints two arguments passed to it:
 * must join the argument with "is"
 */

const process = require('process');
const arg1 = process.argv[2];
const arg2 = process.argv[3];

console.log(arg1, 'is', arg2);
