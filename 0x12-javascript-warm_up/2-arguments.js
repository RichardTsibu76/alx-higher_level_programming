#!/usr/bin/node
const ARGC = process.argv.length; // Note: ARGC means constant

if (ARGC > 2) {
  console.log('Argument' + (ARGC > 3 ? 's' : '') + ' found');
} else {
  console.log('No argument');
}
