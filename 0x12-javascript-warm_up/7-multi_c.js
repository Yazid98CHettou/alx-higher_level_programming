#!/usr/bin/node
const arg = process.argv;
let index = 0;
const myNumber = parseInt(Number(arg[2]));
if (myNumber) {
  while (index < myNumber) {
    console.log('C is fun');
    index++;
  }
} else {
  console.log('Missing number of occurrences');
}
