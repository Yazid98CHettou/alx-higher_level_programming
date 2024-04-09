#!/usr/bin/node
const arg = process.argv;
const len = arg.length;
const arr = [];
let a, j;
if (len > 3) {
  /* create new array */
  j = 0;
  for (a = 2; a < len; a++) {
    arr[j] = arg[a];
    j++;
  }
  /* use sort function */
  console.log(arr.sort((a, b) => b - a)[1]);
} else {
  console.log(0);
}
