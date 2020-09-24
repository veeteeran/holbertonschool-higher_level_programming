#!/usr/bin/node
/*
adds a LI element to a list when the user clicks on the tag DIV#add_item
*/
$(document).ready(function () {
  $('#add_item').click(function () {
    const item = '<li>Item</li>';
    $('UL.my_list').append(item);
  });
});
