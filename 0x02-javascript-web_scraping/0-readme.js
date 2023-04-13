#!/usr/bin/node

const fs = require('fs');

const filePath = 'cisfun'

fs.readFile(filePath, 'utf8', function(err, data) {
  if (err) throw err;
  console.log(data);
});
