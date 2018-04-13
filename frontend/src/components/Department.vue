<template>
  <div class="page-content-container l2-idep">
    <div v-if="dept" class="card card-cascade narrower l2-card">
      <div class="view gradient-card-header tile-title" >
        <p class="tile-title-text">Department of {{ dept.short_code }}</p>
      </div>
      <div class="card-body text-center">
        <div class="tabs-wrapper up-content mx-auto">
          <ul class="nav classic-tabs" role="tablist">
            <li class="nav-item">
              <a class="nav-link waves-light active" data-toggle="tab" href="#li1" role="tab" >About Us</a>
            </li>
            <li class="nav-item">
              <a class="nav-link waves-light" data-toggle="tab" href="#li2" role="tab" >Programmes</a>
            </li>
            <li class="nav-item">
              <a class="nav-link waves-light" data-toggle="tab" href="#li3" role="tab" >HOD</a>
            </li>
            <li class="nav-item">
              <a class="nav-link waves-light" data-toggle="tab" href="#li4" role="tab" >People</a>
            </li>
            <li class="nav-item">
              <a class="nav-link waves-light" data-toggle="tab" href="#li5" role="tab" >Research</a>
            </li>
            <li class="nav-item">
              <a class="nav-link waves-light" data-toggle="tab" href="#li6" role="tab" >Projects</a>
            </li>
            <li class="nav-item">
              <a class="nav-link waves-light" data-toggle="tab" href="#li7" role="tab" >Facilities</a>
            </li>
            <li class="nav-item">
              <a class="nav-link waves-light" data-toggle="tab" href="#li8" role="tab" >Activities</a>
            </li>
            <li class="nav-item">
              <a class="nav-link waves-light" data-toggle="tab" href="#li9" role="tab">Contact Us</a>
            </li>
            <li class="nav-item">
              <a class="nav-link waves-light" data-toggle="tab" href="#li10" role="tab">Photo Gallery</a>
            </li>
          </ul>
        </div>
        <div class="tab-content card down-content">
          <div class="tab-pane fade show active big-list" id="li1" role="tabpanel" aria-labelledby="li1-list">
            <h3 class="pane-title" align="left">About Us</h3>
            <p class="pane-text" align="left" v-html="dept.about_us">
            </p>
          </div>

          <div class="tab-pane fade big-list" id="li2" role="tabpanel" aria-labelledby="li2-list">
            <h3 class="pane-title" align="left">Programmes</h3>
            <ul class="nav md-pills nav-justified pills-secondary">
              <li class="nav-item">
                <a class="nav-link active" data-toggle="tab" href="#panell1" role="tab">UG</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-toggle="tab" href="#panell2" role="tab">PG</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-toggle="tab" href="#panell3" role="tab">PhD</a>
              </li>
            </ul>
            <div class="tab-content">
              <div class="tab-pane fade in show active" id="panell1" role="tabpanel">
                <div class="row">
                  <div class="col" v-for="programme,index in dept.programmes.UG">
                    <h5><strong>Academic Courses and Syllabus for {{ programme.programme_title }} Students</strong></h5>
                    <div class="accordion" id="accordionEx" role="tablist" aria-multiselectable="true">
                      <div class="card" v-for="syllabus,sem in programme">
                        <card-collapse v-if="sem!='programme_title'" :title="'Semester '+sem">
                          <table-renderer :table="syllabus" :theader="['CODE','COURSE TITLE','L','T','S','C']"></table-renderer>
                        </card-collapse>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="panell2" role="tabpanel">
                PG details
              </div>
              <div class="tab-pane fade" id="panell3" role="tabpanel">
                PhD details
              </div>
            </div>
          </div>

          <div class="tab-pane fade  big-list" id="li3" role="tabpanel" aria-labelledby="li3-list">
            <h3 class="pane-title" align="left">Head Of Department</h3>
            <div class="container">
              <div class="row">
                <div class="col">
                  <card-testimonial :name="dept.hod.name" :image="dept.hod.image" desig="Head of Department">
                    <strong>-- Research Interest --</strong><br>
                    <span v-html="dept.hod.research_interest.slice(3,-4)"></span><br>
                    <i class="fa fa-envelope"></i><br>
                    <strong>{{ dept.hod.email }}</strong><br>
                    <i class="fa fa-address-book"></i><br>
                    <strong>+91-{{ dept.hod.mobile }}</strong></br>
                    <span class="grey-text">Joined the Institute in {{ dept.hod.joining_year }}
                    </span>
                  </card-testimonial>
                </div>
              </div>
            </div>
          </div>

          <div class="tab-pane fade big-list" id="li4" role="tabpanel" aria-labelledby="li4-list">
            <h3 class="pane-title" align="left">People</h3>
            <ul class="nav md-pills nav-justified pills-secondary">
              <li class="nav-item">
                <a class="nav-link active" data-toggle="tab" href="#p4l1" role="tab">Faculty</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-toggle="tab" href="#p4l2" role="tab">Staff</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-toggle="tab" href="#p4l3" role="tab">Students</a>
              </li>
            </ul>
            <div class="tab-content">
              <div class="tab-pane fade in show active" id="p4l1" role="tabpanel">
                <div class="container-fluid">

                  <div class="caros">
                    <div id="caro-p1-1" class="carousel slide carousel-multi-item" data-ride="carousel">
                      <span class="carousel-title">FACULTIES</span>
                      <div class="controls-top">
                        <a class="btn-floating" href="#caro-p1-1" data-slide="prev"><i class="fa fa-chevron-left"></i></a>
                        <a class="btn-floating" href="#caro-p1-1" data-slide="next"><i class="fa fa-chevron-right"></i></a>
                      </div>
                      <ol class="carousel-indicators">
                        <li data-target="#caro-p1-1" data-slide-to="0" class="active"></li>
                        <li data-target="#caro-p1-1" data-slide-to="1"></li>
                        <li data-target="#caro-p1-1" data-slide-to="2"></li>
                      </ol>
                      <div class="carousel-inner person-list" role="listbox">
                        <div class="carousel-item active">
                          <div class="row">

                            <div class="col" v-for="person in dept.people.faculty">
                              <card-testimonial :name="person.name" :image="person.image" desig="Faculty">
                                <strong>-- Research Interest --</strong><br>
                                <span v-html="stripDesc(person.research_interest)"></span><br>
                                <i class="fa fa-envelope"></i><br>
                                <strong>{{ person.email }}</strong><br>
                                <i class="fa fa-address-book"></i><br>
                                <strong>+91-{{ person.mobile }}</strong></br>
                                <span class="grey-text">Joined the Institute in {{ person.joining_year }}
                                </span>
                              </card-testimonial>
                            </div>
                          </div>
                        </div>
                      </div>

                    </div>
                  </div>

                </div>
              </div>
              <div class="tab-pane fade" id="p4l2" role="tabpanel">
                <div class="container-fluid">
                    <h1>Same as faculty</h1>
                </div>
              </div>
              <div class="tab-pane fade" id="p4l3" role="tabpanel">
                <h1>List of students year wise (just names)</h1>
              </div>
            </div>
          </div>

          <div class="tab-pane fade big-list" id="li5" role="tabpanel" aria-labelledby="li5-list">
            <h3 class="pane-title" align="left">Research</h3>
            <h4 class="white-text"><strong>Collaboration with Academic and Research Institutions in recent times</strong></h4>
            <div class="card">
              <div class="card-body">
                <table-renderer :theader="research_header" :table="dept.research"></table-renderer>
              </div>
            </div>
          </div>

          <div class="tab-pane fade big-list" id="li6" role="tabpanel" aria-labelledby="li5-list">
            <h3 class="pane-title" align="left">Projects</h3>
            <h4 class="white-text"><strong>Ongoing Sponsored Projects</strong></h4>
            <div class="card">
              <div class="card-body">
                <table-renderer :theader="project_header" :table="dept.projects"></table-renderer>
              </div>
            </div>
          </div>

          <div class="tab-pane fade big-list" id="li7" role="tabpanel" aria-labelledby="li7-list">
            <h3 class="pane-title" align="left">Facilities</h3>
            <ul class="nav md-pills nav-justified pills-secondary">
              <li class="nav-item">
                <a class="nav-link active" data-toggle="tab" href="#p7l1" role="tab">Labratories</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-toggle="tab" href="#p7l2" role="tab">Equipments</a>
              </li>
            </ul>
            <div class="tab-content">
              <div class="tab-pane fade in show active" id="p7l1" role="tabpanel">
                <div class="row">
                  <div class="col">
                    <ul class="list-group">
                      <li v-for="lab in dept.facilities.Laboratory" class="list-group-item">{{ lab.name }}</li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="p7l2" role="tabpanel">
                <div class="row">
                  <div class="col">
                    <ul class="list-group">
                      <li v-for="equip in dept.facilities.Equipment" class="list-group-item">{{ equip.name }}</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="tab-pane fade big-list" id="li9" role="tabpanel" aria-labelledby="li9-list">
            <p class="white-text" align="center" v-html="dept.contact_us">
            </p>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import { genBackendURL,stripDesc } from '@/common.js'
import TableRenderer from '@/components/TableRenderer'
import CardCollapse from '@/components/CardCollapse'
import CardTestimonial from '@/components/CardTestimonial'

export default {
  name: "Department",
  data () {
    return {
      dept: undefined,
      research_header: [
        'Collaborating Institute / Organization',
        'Areas of Collaboration',
        'Faculty Members Involved',
        'Year'
      ],
      project_header: [
        'Collaborating Institute / Organization',
        'Areas of Collaboration',
        'Faculty Members Involved',
        'Funding',
        'Year'
      ]
    }
  },
  created () {
    axios.get(genBackendURL("department"))
         .then(response => {
           let departments = response.data.results
           let i
           for (i = 0; i < departments.length; i++) {
             if (this.$route.params.short_code == departments[i].short_code)
               break;
           }
           axios.get(genBackendURL("department/"+departments[i].id))
                .then(response => {
                  this.dept = response.data
                  this.$emit('hideloader', true)
                })
                .catch(e => {
                  console.log(e)
                })
         })
         .catch(e => {
           console.log(e)
         })
  },
  methods: {
    stripDesc: stripDesc
  },
  components: {
    LinksPage,
    Card,
    TableRenderer,
    CardCollapse,
    CardTestimonial
  }
}
</script>
