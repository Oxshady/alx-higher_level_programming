#!/usr/bin/node

function add (a, b) {
  let num1 = Number(a);
  let num2 = Number(b);
  if (isNaN(num1) || isNaN(num2)) {
    console.log('NaN');
  } else {
    console.log(num1 + num2);
  }
}
add(process.argv[2], process.argv[3]);
