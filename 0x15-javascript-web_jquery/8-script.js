#!/usr/bin/node
/*
fetches and lists all movies title by using SWAPI
*/
$(document).ready(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json',
    data => data.results.forEach(result =>
      $('UL#list_movies').append('<li>' + result.title + '</li>')));
});
