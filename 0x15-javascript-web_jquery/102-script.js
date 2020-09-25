#!/usr/bin/node
/*
fetches and prints how to say “Hello” depending of the language
*/
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const language = $('#language_code').val();
    const url = `https://fourtonfish.com/hellosalut/?lang=${language}`;
    $.get(url, data => $('#hello').text(data.hello));
  });
});
