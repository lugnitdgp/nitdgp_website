$(document).ready(function() {
  $( "#header" ).load( "/static/layout/header.html");
  $( "#footer" ).load( "/static/layout/footer.html");

  function section_card(priority) {
    return '<div class="card card-cascade narrower l2-card" id=section_card'+priority+'>';
  }

  function section_header(title) {
    return '<div class="view gradient-card-header tile-title" >\
                <p class="tile-title-text">'+title+'</p>\
            </div>';
  };

function nav_menu(){
    return '<div class="tabs-wrapper up-content" >\
      <!-- Navigation -->\
      <ul class="nav classic-tabs tabs-cyan" role="tablist">\
        <li class="nav-item">\
          <a class="nav-link waves-light active" data-toggle="tab" href="#li1" role="tab" >About Us</a>\
        </li>\
        <li class="nav-item">\
          <a class="nav-link waves-light" data-toggle="tab" href="#li2" role="tab" >Programmes</a>\
        </li>\
        <li class="nav-item">\
          <a class="nav-link waves-light" data-toggle="tab" href="#li3" role="tab" >HOD</a>\
        </li>\
        <li class="nav-item">\
          <a class="nav-link waves-light" data-toggle="tab" href="#li4" role="tab" >People</a>\
        </li>\
        <li class="nav-item">\
          <a class="nav-link waves-light" data-toggle="tab" href="#li5" role="tab" >Research</a>\
        </li>\
        <li class="nav-item">\
          <a class="nav-link waves-light" data-toggle="tab" href="#li6" role="tab" >Projects</a>\
        </li>\
        <li class="nav-item">\
          <a class="nav-link waves-light" data-toggle="tab" href="#li7" role="tab" >Facilities</a>\
        </li>\
        <li class="nav-item">\
          <a class="nav-link waves-light" data-toggle="tab" href="#li8" role="tab" >Activities</a>\
        </li>\
        <li class="nav-item">\
          <a class="nav-link waves-light" data-toggle="tab" href="#li9" role="tab">Contact Us</a>\
        </li>\
        <li class="nav-item">\
          <a class="nav-link waves-light" data-toggle="tab" href="#li10" role="tab">Photo Gallery</a>\
        </li>\
      </ul>\
      <!-- Navigation -->\
    </div>'
};

function pane_header(header,id,state) {
  return '<div class="tab-pane fade '+state+'" id="li'+id+'" role="tabpanel" aria-labelledby="li1-list">\
    <h3 class="pane-title" align="left">'+header+'</h3>'
}

function about_pane(about_us) {
  return pane_header("About Us",1,"show active")+'<p class="pane-text" align="left">'+about_us+'</p>\
  </div>'
}

function programme_pills() {
  return '<ul class="nav md-pills nav-justified pills-secondary">\
          <li class="nav-item">\
              <a class="nav-link active" data-toggle="tab" href="#panell1" role="tab">UG</a>\
          </li>\
          <li class="nav-item">\
              <a class="nav-link" data-toggle="tab" href="#panell2" role="tab">PG</a>\
          </li>\
          <li class="nav-item">\
              <a class="nav-link" data-toggle="tab" href="#panell3" role="tab">PhD</a>\
          </li>\
      </ul>'

}

function tableRender(value) {
  html = '<div class="table-wrapper-2 table-bordered">\
            <table class="table table-responsive-md">\
              <thead class="mdb-color lighten-4">\
                <tr>\
                <th class="th-lg">CODE</th>\
                <th class="th-lg">COURSE TITLE</th>\
                <th class="th-lg">L</th>\
                <th class="th-lg">T</th>\
                <th class="th-lg">S</th>\
                <th class="th-lg">C</th>\
                </tr>\
              </thead>\
              <tbody>'
  $.each(value,function(index,course){
    html += '<tr>\
                <td>'+course.short_code+'</td>\
                <td>'+course.title+'</td>\
                <td>0</td>\
                <td>0</td>\
                <td>0</td>\
                <td>0</td>\
            </tr>'
  });
  html+='</tbody></table></div>'
return html
}

function tab_content(id,state,level) {
  var html = '<div class="tab-pane fade in '+state+'" id="panell'+id+'" role="tabpanel">\
                <div class="row" id="panell'+id+'-row1">'
  $.each(level,function(index,programme){
    // make an accordian in a div col
    html+= '<div class="col">\
              <h4><strong>Academic Courses and Syllabus for '+programme.programme_title+' Students</strong></h3>\
              <div class="card"><div class="accordion" id="accordionEx" role="tablist" aria-multiselectable="true">'

    //LOOP FOR SEMESTER
    $.each( programme, function( semester, value ) {
      if(semester!='programme_title') {
        // LOOP FOR COURSES
        html += ' <div class="card">\
                    <div class="card-header" role="tab">\
                      <a data-toggle="collapse" data-parent="#accordionEx" href="#collapse'+index+semester+'" aria-expanded="true">\
                        <h5 class="mb-0">Semester\
                          '+semester+' <i class="fa fa-angle-down rotate-icon"></i>\
                        </h5>\
                      </a>\
                    </div>\
                   <div id="collapse'+index+semester+'" class="collapse" role="tabpanel" >\
                    <div class="card-body">'+tableRender(value)+'\
                    </div>\
                   </div>\
                 </div>'
      }
    });
    html+='</div></div></div>'
  });
  html+='</div></div>'
  return html
}

function programme_pane(programmes) {
  return pane_header("Programme",2,"")+programme_pills()+'<div class="tab-content" id="programme-content">'+
         tab_content(1,"show active",programmes.UG)+tab_content(2,"",programmes.PG)+'<div class="tab-pane fade in" id="panell3" role="tabpanel">'
}

function hod_pane() {
  return pane_header("HOD",3,"")+''

}

  var dept = $('#dept').val();

  $.ajax({
    type: "GET",
    dataType: 'json',
    url: "http://172.16.20.3:8000/department/?format=json",
    success: function(data) {
      $.each(data.results, function(index, department) {
        if(department.short_code == dept.toUpperCase()) {


          // Render Department Here
          $.ajax({
            type: "GET",
            dataType: 'json',
            url: "http://172.16.20.3:8000/department/"+department.id+"/?format=json",
            success: function(department_info){
              console.log(department_info);
              $('#dynamic').append('<div class="row big-row" id=row_1>');
              $('#row_1').append('<div class="col big-col" id=col_1>');
              $('#col_1').append(section_card(1));
              $('#section_card1').append(section_header("Department of "+department_info.short_code.toUpperCase()));
              $('#section_card1').append('<div class="card-body text-center" id=card_1>');
              $('#card_1').append(nav_menu());
              $('#card_1').append('<div class="tab-content card down-content" id=down_content>');
              $('#down_content').append(about_pane(department_info.about_us));
              $('#down_content').append(programme_pane(department_info.programmes));
              $('down_content').append(hod_pane(department_info.hod));

            }

         });



























        }
      });
    },

    error: function(error) {
      console.log(error);
    }
  });

});
