#!/usr/bin/node
/*
fetches from https://fourtonfish.com/hellosalut/?lang=fr
and displays the value of hello from that fetch in the
HTML’s tag DIV#hello
*/
$(document).ready(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr',
    data => $('#hello').text(data.hello));
});
