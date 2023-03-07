#!/usr/bin/node
const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], async (err, res, body) => {
  err && console.log(err);
  for (const chr of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(chr, (err, res, body) => {
        err && console.log(err);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
