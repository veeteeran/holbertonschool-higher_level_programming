#!/usr/bin/node
/*
adds, removes and clears LI elements from a list when the user clicks
*/
$(document).ready(() => {
  $('#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(() => {
    $('UL.my_list li').eq(-1).remove();
  });
  $('#clear_list').click(() => {
    $('UL.my_list').remove();
  });
});
