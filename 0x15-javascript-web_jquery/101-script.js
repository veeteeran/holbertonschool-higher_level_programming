#!/usr/bin/node
/*
adds, removes and clears LI elements from a list when the user clicks
*/
$(document).ready(function () {
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $('UL.my_list li').eq(-1).remove();
  });
  $('#clear_list').click(function () {
    $('UL.my_list').remove();
  });
});
