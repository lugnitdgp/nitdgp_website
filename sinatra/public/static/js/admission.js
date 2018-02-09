$(document).ready(function() {
  $( "#header" ).load( "../nitdgp_website/static/layout/header.html");
  $( "#footer" ).load( "../nitdgp_website/static/layout/footer.html");
});

$(function() {
    $('.card-header').on('click', function() {
        if ($(this).siblings('.card-body').hasClass('hidden')) {
            $(this).siblings('.card-body').addClass('show').removeClass('hidden');
        } else {
            $(this).siblings('.card-body').removeClass('show').addClass('hidden');
        }
    })
});
