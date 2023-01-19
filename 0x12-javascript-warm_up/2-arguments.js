#!/usr/bin/node
/*
 * Script prints a message based on the number
 * of arguments, if:
 * no arguments print: "No argument"
 * One argument print: "Argument found"
 * Otherwise print: "Arguments found"
 */

const myVar = ['No argument', 'Argument found', 'Arguments found'];
const process = require('process');
const l = process.argv.length;

if (l === 2) {
  console.log(myVar[0]);
} else if (l === 3) {
  console.log(myVar[1]);
} else {
  console.log(myVar[2]);
}
