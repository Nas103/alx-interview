#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;
  const characterNames = [];

  characters.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      const character = JSON.parse(body);
      characterNames[index] = character.name;

      if (characterNames.filter(name => name).length === characters.length) {
        characterNames.forEach(name => console.log(name));
      }
    });
  });
});
