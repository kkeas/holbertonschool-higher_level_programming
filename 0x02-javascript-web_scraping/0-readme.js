#!/usr/bin/node

const fs = require('fs');

fs.readFile('/path/to/file', 'utf8', function(err, data) {
  if (err) throw err;
  console.log(data);
});
