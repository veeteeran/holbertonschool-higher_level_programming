#!/usr/bin/node
/* toggles the class of the HTML tag HEADER to red (#FF0000)
when the user clicks on the tag DIV#toggle_header
*/
$(document).ready(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
