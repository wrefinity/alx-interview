#!/usr/bin/node
/* 
 * Get all Casts of Star Wars movie
*/

const request = require('request');
const starWarsAPI = 'https://swapi-api.alx-tools.com/api/';
const endPoint = 'films/';
const movieId = process.argv[2].toString();

request(starWarsAPI + endPoint + movieId, function (error, _, body) {
  if (error) console.error(error);
  const objects = JSON.parse(body);
  const chars = objects.characters;
  PrintResult(chars);
});

/* iteratively request for each character */
function PrintResult (chars, inc = 0) {
  request(chars[counter], function (err, _, body) {
    if (err) console.error(err);
    console.log(JSON.parse(body).name);
    if (++inc < chars.length) {
      PrintResult(chars, inc++);
    }
  });
}
