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
      <ul class="nav classic-tabs" role="tablist">\
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
  return '<div class="tab-pane fade big-list '+state+'" id="li'+id+'" role="tabpanel" aria-labelledby="li1-list">\
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

function programme_tab_content(id,state,level) {
  var html = '<div class="tab-pane fade in '+state+'" id="panell'+id+'" role="tabpanel">\
                <div class="row" id="panell'+id+'-row1">'
  $.each(level,function(index,programme){
    // make an accordian in a div col
    html+= '<div class="col">\
              <h5><strong>Academic Courses and Syllabus for '+programme.programme_title+' Students</strong></h5>\
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
         programme_tab_content(1,"show active",programmes.UG)+programme_tab_content(2,"",programmes.PG)+'<div class="tab-pane fade in" id="panell3" role="tabpanel">'
}

function person_card(person,designation) {

  if(person.research_interest.length > 60) {
    var research = person.research_interest.slice(3,60);
  }
  else {
    var research = person.research_interest.slice(3,-4);
  }
  // console.log(person.image);
  research += '...'
  return '<div class="card testimonial-card">\
            <!--Background color-->\
            <div class="card-up">\
            </div>\
            <!--Avatar-->\
            <div class="avatar mx-auto">\
              <img src="'+person.image+'" class="rounded-circle img-responsive">\
            </div>\
            <div class="card-body-in">\
                <!--Name-->\
                <h4 class="card-title mt-1"><strong>'+person.name+'</strong></h4>\
                <h6 class="red-text">'+designation+'</h6>\
                <hr>\
                <p class="min-profile">\
                    <strong>-- Research Interest --</strong><br>\
                    '+research+'\
                      <a href="#">Read More</a><br/><i class="fa fa-envelope"></i><br/>\
                    <strong>'+person.email+'</strong><br>\
                    <i class="fa fa-address-book"></i><br>\
                    <strong>+91-9434788006</strong></br>\
                    <span class="grey-text">Joined the Institute in January, '+person.joining_year+'\
                    </span>\
                </p>\
            </div>\
          </div>'
}

function hod_pane(hod) {
  return pane_header("Head of Department",3,"")+'<div class="container">\
      <div class="row">\
          <!--Grid column-->\
          <div class="col-lg-12 col-md-12 mb-r">'+person_card(hod,"Professor and Head")+'\
          </div>\
          <!--Grid column-->\
      </div>'
}

function people_pills() {
  return '<ul class="nav md-pills nav-justified pills-secondary">\
          <li class="nav-item">\
              <a class="nav-link active" data-toggle="tab" href="#p4l1" role="tab">Faculty</a>\
          </li>\
          <li class="nav-item">\
              <a class="nav-link" data-toggle="tab" href="#p4l2" role="tab">Staff</a>\
          </li>\
          <li class="nav-item">\
              <a class="nav-link" data-toggle="tab" href="#p4l3" role="tab">Students</a>\
          </li>\
      </ul>'

}

function people_tab_content(id,state,people_group) {
  var html = '<div class="tab-pane fade in '+state+'" id="p4l'+id+'" role="tabpanel">\
                <div class="container">'

  var row=1;
  $.each(people_group,function(designation,persons) {
    var pages = Math.ceil(persons.length/5);
    html+='<div class="caros">\
            <div id="caro-p1-'+row+'" class="carousel slide carousel-multi-item" data-ride="carousel">\
              <span class="carousel-title">'+designation.toUpperCase()+'</span>'
    html+='<div class="controls-top">\
                <a class="btn-floating" href="#caro-p1-'+row+'" data-slide="prev"><i class="fa fa-chevron-left"></i></a>\
                <a class="btn-floating" href="#caro-p1-'+row+'" data-slide="next"><i class="fa fa-chevron-right"></i></a>\
              </div>'
    html+= '<ol class="carousel-indicators">'
    for (i=0; i<pages ;i++) {
      if(i==0){
        html+='<li data-target="#caro-p1-'+row+'" data-slide-to="0" class="active"></li>'
      }
      else {
        html+='<li data-target="#caro-p1-'+row+'" data-slide-to="'+i+'"></li>'
      }
    }
    html+= '</ol>'
    html+='<div class="carousel-inner" role="listbox">'
    for(i=0;i<pages;i++) {
      if(i==0) {
        html+='<div class="carousel-item active">'
      }
      else {
        html+='<div class="carousel-item">'
      }
      html+='<div class="row">'
      for(j=i*5; j<i+5&&j<persons.length; j++) {
        html+='<div class="col">'
        html+=person_card(persons[j],designation);
        html+="</div>"
      }
      html+='</div></div>'
    }
    html+='</div>'
    html+='</div></div>'
    row++;
  });

  html+='</div></div>'
  return html
}

function people_pane(people) {
  return pane_header("People",4,"")+people_pills()+'<div class="tab-content">'+
         people_tab_content(1,"show active",people.faculty)+'\
         <div class="tab-pane fade in" id="p4l2" role="tabpanel">Staff</div>\
         <div class="tab-pane fade in" id="p4l3" role="tabpanel">Student</div></div>'
}

function projectAndResearchTableRender(array) {
  html = '<div class="table-wrapper-2 table-bordered">\
            <table class="table table-responsive-md">\
              <thead class="mdb-color lighten-4">\
                <tr>\
                <th class="th-lg">Collaborating Institute</th>\
                <th class="th-lg">Area</th>\
                <th class="th-lg">Faculty Involved</th>\
                <th class="th-lg">Funding</th>\
                <th class="th-lg">Year Started</th>\
                </tr>\
              </thead>\
              <tbody>'
  $.each(array,function(index,entry){
    html += '<tr>\
                <td>'+entry.collab_inst+'</td>\
                <td>'+entry.area+'</td>\
                <td>'+entry.faculty_involved+'</td>\
                <td>'+entry.funding+'</td>\
                <td>'+entry.date+'</td>\
            </tr>'
  });
  html+='</tbody></table></div>'
  return html
}

function research_pane(research) {
  return pane_header("Research",5,"") + projectAndResearchTableRender(research)
}


function project_pane(projects) {
  return pane_header("Project",6,"") + projectAndResearchTableRender(projects)
}

function facilities_pills() {
  return '<ul class="nav md-pills nav-justified pills-secondary">\
      <li class="nav-item">\
          <a class="nav-link active" data-toggle="tab" href="#p7l1" role="tab">Labratories</a>\
      </li>\
      <li class="nav-item">\
          <a class="nav-link" data-toggle="tab" href="#p7l2" role="tab">Equipments</a>\
      </li>\
  </ul>'
}

function facility_tab_content(id,state,array) {

  var html = '<div class="tab-pane fade '+state+'" id="p7l'+id+'" role="tabpanel">\
              <div class="row">\
                <div class="col">\
                 <ul class="list-group">'
 $.each(array,function(index,entry) {
   html+='<li class="list-group-item">'+entry.name+'</li>'
 });
 html+='</ul></div></div></div>'
 return html
}

function facilities_pane(facilities) {
  return pane_header("Facilities",7,"")+facilities_pills()+'<div class="tab-content">'+
         facility_tab_content(1,"show active",facilities.Laboratory)+
         facility_tab_content(2,"",facilities.Equipment)
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
              $('#down_content').append(hod_pane(department_info.hod));
              $('#down_content').append(people_pane(department_info.people));
              $('#down_content').append(research_pane(department_info.research));
              $('#down_content').append(project_pane(department_info.projects));
              $('#down_content').append(facilities_pane(department_info.facilities));
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
