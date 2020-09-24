#!/usr/bin/node
/*
Fetches and prints how to say “Hello” depending of the language
when user clicks on INPUT#btn_translate OR presses ENTER
*/
$(document).ready(() => {
  $('#btn_translate').click(() => {
    const language = $('#language_code').val();
    const url = `https://fourtonfish.com/hellosalut/?lang=${language}`;
    $.get(url, data => $('#hello').text(data.hello));
  });
  $('#language_code').keypress(e => {
    if (e.which === 13) {
      $('#btn_translate').click();
    }
  });
});
