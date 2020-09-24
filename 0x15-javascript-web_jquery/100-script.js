#!/usr/bin/node
/*
updates the text color of the HTML tag HEADER to red (#FF0000)
script must be imported from the HEAD tag, not at the end of the HTML
*/
document.addEventListener('DOMContentLoaded', () =>
  document.querySelector('header').style.color = '#FF0000'
);
