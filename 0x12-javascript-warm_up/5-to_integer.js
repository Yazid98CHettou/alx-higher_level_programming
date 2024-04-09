#!/usr/bin/node
const argv = process.argv;
let myNumber = Number(argv[2]);
if (myNumber) {
  myNumber = parseInt(myNumber);
  console.log(`My number: ${myNumber}`);
} else {
  console.log('Not a number');
}
