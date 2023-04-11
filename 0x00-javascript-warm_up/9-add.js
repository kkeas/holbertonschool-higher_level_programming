#!/usr/bin/node

function add (a, b) {
  a = parseInt(process.argv[2], 10);
  b = parseInt(process.argv[3], 10);
  const sum = a + b;
  return console.log(sum);
}

add();
