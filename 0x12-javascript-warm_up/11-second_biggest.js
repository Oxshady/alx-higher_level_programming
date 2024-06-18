#!/usr/bin/node
const leng = process.argv.length;

if (leng < 4) {
  console.log(0);
} else {
  let largest = 0;
  let largest2 = 0;
  for (let i = 2; i < leng; i++) {
    if (largest < Number(process.argv[i])) {
      largest = Number(process.argv[i]);
    }
  }
  for (let i = 2; i < leng; i++) {
    if (largest2 < Number(process.argv[i])) {
      if (Number(process.argv[i]) < largest) {
        largest2 = Number(process.argv[i]);
      }
    }
  }
  console.log(largest2);
}
