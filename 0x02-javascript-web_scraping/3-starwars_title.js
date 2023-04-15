#!/usr/bin/node

const request = require('request');
const episode = parseInt(process.argv[2]);

const url = `https://swapi-api.hbtn.io/api/films/${episode}`;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(`${data.title}`);
  } else {
    console.error('Error:', error);
  }
});
