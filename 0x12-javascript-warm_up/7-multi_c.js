#!/usr/bin/node
const x = process.argv[2]; // let x be the first argument of the script

if (!parseInt(x)) {
console.log('Missing number of occurrences');
} else {
for (let i = 0; i < x; i++) {
console.log('C is fun');
  }
}
