#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (response && response.statusCode) {
    console.log(`code: ${response.statusCode}`);
  } else {
    console.error('Error:', error);
  }
});
