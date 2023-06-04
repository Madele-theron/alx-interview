#!/usr/bin/node
/* Script that prints all characters of a Star Wars movie */

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const filmId = process.argv[2];

// if (filmId === undefined) {
//   exit();
// }

// Query the api
request(url + filmId, (error, response, body) => {
  if (!error) {
    const people = JSON.parse(body).characters;
    printPeople(people, 0);
  } else {
    console.log(error);
  }
});

// Print people in order to console
function printPeople (people, i) {
  if (i === people.length) return;
  request(people[i], (error, reponse, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      printPeople(people, i++);
    } else {
      console.log('error', error);
    }
  });
}
