#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  // Loop over character URLs in order
  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.log('Error:', error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
