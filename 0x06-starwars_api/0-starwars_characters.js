#!/usr/bin/node
/* 
 * Get all Casts of Star Wars movie
*/

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let people = [];
const names = [];

const queryCharacters = async () => {
  await new Promise(resolve => request(filmEndPoint, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const jsonBdy = JSON.parse(body);
      people = jsonBdy.characters;
      resolve();
    }
  }));
};

const queryNames = async () => {
  if (people.length > 0) {
    for (const p of people) {
      await new Promise(resolve => request(p, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
          const jsonBdy = JSON.parse(body);
          names.push(jsonBdy.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: Got no Characters for some reason');
  }
};

const getMovieCast = async () => {
  await queryCharacters();
  await queryNames();

  for (const nm of names) {
    if (nm === names[names.length - 1]) {
      process.stdout.write(nm);
    } else {
      process.stdout.write(nm + '\n');
    }
  }
};

getMovieCast();
