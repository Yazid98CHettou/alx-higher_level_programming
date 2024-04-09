#!/usr/bin/node
const arg = process.argv;
function add (a, b) {
  const result = mynum1 + mynum2;
  return result;
}
var mynum1 = parseInt(Number(arg[2]));
var mynum2 = parseInt(Number(arg[3]));
console.log(add(mynum1, mynum2));
