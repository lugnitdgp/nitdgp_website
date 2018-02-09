$(document).ready(function() {

function section_card(priority) {
  return '<div class="card card-cascade narrower card-'+eval(priority+1)+'" id=section_card'+priority+'>';
}

function section_header(title) {
  return '<div class="view gradient-card-header tile-title" >\
              <p class="tile-title-text">'+title+'</p>\
          </div>';
};


function small_tile(link,icon,name) {
  return '<div class="col tile-small">\
            <a href="/nitdgp_website/department/?id='+link+'">\
            <div align="center" class="tile-content"><i class="fa fa-2x">'+icon+'</i><br>\
              <p class="tile-small-text">'+name+'</p>\
            </div>\
            </a>\
          </div>'
};

$( "#header" ).load( "static/layout/header.html");
$( "#footer" ).load( "static/layout/footer.html");

  console.log("Hello");
  $.ajax({
    type: "GET",
    dataType: 'json',
    url: "http://172.16.20.3:8000/department/?format=json",
    success: function(data){

      console.log(data);

      $('#dynamic').append('<div class="row big-row" id=row_1>');
      $('#row_1').append('<div class="col big-col" id=col_1>');
      $('#col_1').append(section_card(1));
      $('#section_card1').append(section_header("Departments and Centers"));
      $('#section_card1').append('<div class="card-body text-center" id=card_1>');

      // LOOP FOR SECTION
      var n = data.results.length;
      if (n%4==0) {
        // each row has 4 elements
        $.each(data.results, function(index, tile) {
          if (index % 4 == 0) {
            $('#card_1').append('<div class="row" id=tile_row'+parseInt(index/4)+'>');
          }
          $('#tile_row'+parseInt(index/4)).append(small_tile(tile.id,tile.short_code,tile.name));
        });
      }
      else if (n%4==1) {
        // first 3 rows have 3 elements then rest each row has 4
        var row_no=0;
        $.each(data.results, function(index, tile) {

            if (index<=9) {
              if (index%3==0) {
                $('#card_1').append('<div class="row" id=tile_row'+eval(row_no)+'>');
                ++row_no;
              }
            }
            else {
              if (index%4==1) {
                $('#card_1').append('<div class="row" id=tile_row'+eval(row_no)+'>');
                ++row_no;
              }
            }
            $('#tile_row'+eval(row_no-1)).append(small_tile(tile.id,tile.short_code,tile.name))
        });
      }
      else if (n%4==2) {
        // first 2 rows have 3 elements then rest each row has 4
        var row_no=0;
        $.each(data.results, function(index, tile) {

            if (index<=6) {
              if(index%3==0){
                $('#card_1').append('<div class="row" id=tile_row'+eval(row_no)+'>');
                ++row_no;
              }
            }
            else {
              if (index%4==2) {
                $('#card_1').append('<div class="row" id=tile_row'+eval(row_no)+'>');
                ++row_no;
              }
            }
            $('#tile_row'+eval(row_no-1)).append(small_tile(tile.id,tile.short_code,tile.name))
        });
      }
      else {
        // first row have 3 elements then rest each row has 4
        var row_no=0;
        $.each(data.results, function(index, tile) {

            if (index%3==0 && index<=3) {
              $('#card_1').append('<div class="row" id=tile_row'+eval(row_no)+'>');
              ++row_no;
            }
            else if (index%4==3) {
              $('#card_1').append('<div class="row" id=tile_row'+eval(row_no)+'>');
              ++row_no;
            }
            $('#tile_row'+eval(row_no-1)).append(small_tile(tile.id,tile.short_code,tile.name))
        });
      }
    },
    error: function(error){
      console.log(error);
    }
  });
});
