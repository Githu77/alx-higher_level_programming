#!/usr/bin/node
const { argv } = require('process');
const size = Number(argv[2]);
const repeat = 'X'.repeat(size);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < size; x++) {
    console.log(repeat);
  }
}
