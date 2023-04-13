#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

const buffer = Buffer.from(content, 'utf-8');

fs.writeFile(filePath, buffer, content, (err) => {
  if (err) throw err;
  console.log(content);
});
