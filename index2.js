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
      <a href="'+link+'">\
      <div align="center" class="tile-content"  ><i class="fa '+icon+' fa-2x"></i></br>\
                <p class="tile-small-text">'+name+'</p>\
      </div>\
      </a>\
    </div>';
};

  console.log("Hello");
  $.ajax({
    type: "GET",
    dataType: 'jsonp',
    url: "http://172.16.20.3:8000/dashboard/?format=json",
    success: function(data){
      console.log(data);

      // LOOP FOR SECTION
      $.each(data.tiles, function(index, element) {
        console.log(element.section_name);
        if (index%3==0)
        {
          $('#dynamic').append('<div class="row big-row" id=row_'+index+'>');
        }
        console.log(parseInt(index/3));
        $('#row_'+parseInt(index/3)).append('<div class="col big-col" id=col_'+index+'>');
        $('#col_'+index).append(section_card(index));
        $('#section_card'+index).append(section_header(element.section_name));
        $('#section_card'+index).append('<div class="card-body text-center" id=card_'+index+'>');


        var prev=0;
        $.each(element.contents,function(tile_index, tile) {
          if (prev != tile.row)
          {
            ++prev;
            $('#card_'+index).append('<div class="row" id=sec_ind'+index+'_tile_row'+prev+'>');
          }
          $('#sec_ind'+index+'_tile_row'+prev).append(small_tile(tile.link,tile.icon,tile.name));
        });
      });
    },
    error: function(error){
      console.log(error);
    }
  });
});
