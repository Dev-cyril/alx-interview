#!/usr/bin/node
const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
    if (res.statusCode === 200) {
        for (let char of JSON.parse(body).characters){
            request.get(char, function (err, res, body){
                if (res.statusCode === 200){
                    console.log(JSON.parse(body).name)
                } else if (err) {
                    console.log(err);
                }
            })
        }
        console.log(JSON.parse(body).title);
    } else if (err) {
        console.log(err);
    }
});