#!/usr/bin/node
/*
updates the text color of the HTML tag HEADER to red (#FF0000)
when the user clicks on the tag DIV#red_header
*/
$(document).ready(function () {
  $('#red_header').click(() => $('header').css('color', '#FF0000'));
});
