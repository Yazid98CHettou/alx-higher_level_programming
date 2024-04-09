#!/usr/bin/node
const arg = process.argv;
let i = 0;
let j = 0;
let str = '';
const mynum = parseInt(Number(arg[2]));
if (mynum) {
  while (i < mynum) {
    while (j < mynum) {
      str = str + 'X';
      j++;
    }
    console.log(str);
    i++;
  }
} else {
  console.log('Missing size');
}
