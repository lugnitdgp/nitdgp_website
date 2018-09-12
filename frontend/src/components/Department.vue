<template>
  <div class="l2-idep">
    <sp-card v-if="dept" containerclass="l2-card" bodyclass="text-center">
      <p slot="header" class="tile-title-text">
        <a href="/departments" class="white-text">Department of {{ dept.short_code }}</a>
      </p>
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
            <a class="nav-link waves-light" data-toggle="tab" href="#li4" role="tab" >Peoples</a>
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
            <a class="nav-link waves-light" data-toggle="tab" href="#li9" role="tab">Photo Gallery</a>
          </li>
          <li class="nav-item">
            <a class="nav-link waves-light" data-toggle="tab" href="#li10" role="tab">Contact Us</a>
          </li>
        </ul>
      </div>
      <div class="tab-content card down-content">
        <div class="tab-pane fade show active big-list" id="li1" role="tabpanel" aria-labelledby="li1-list">
          <div class="row newscaro">
            <div class="col-8 caro">
              <h3 class="pane-title" align="left">About Us</h3>
              <p class="pane-text" align="left" v-html="dept.about_us"></p>
            </div>
            <div class="col-4 news" align="left">
              <Newsfeed :notices="dept.news"></Newsfeed>
            </div>
          </div>
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
                        <table-renderer :table="syllabus" :theader="['COURSE TITLE', 'CODE','L','T','S','C']"></table-renderer>
                      </card-collapse>
                    </div>
                  </div>
                </div>
              </div>
              <br>
              <div class="page-type-links">
                <h5><strong>Details of Syllabus in UG</strong></h5>
                <h6 class="red-text" v-if="!dept.syllabus.UG">
                  Not Available at the moment
                </h6>
                <ul class="list-group list-gr">
                  <li v-for="list,index in dept.syllabus.UG">
                    <a class="list-group-item" :href="list.file">{{ list.title }}</a>
                  </li>
                </ul>
              </div>
            </div>
            <div class="tab-pane fade page-type-links" id="panell2" role="tabpanel">
              <h5><strong>Details of Syllabus/Programmes in PG</strong></h5>
              <h6 class="red-text" v-if="!dept.syllabus.PG">
                Not Available at the moment
              </h6>
              <ul class="list-group list-gr">
                <li v-for="list,index in dept.syllabus.PG">
                  <a class="list-group-item" :href="list.file">{{ list.title }}</a>
                </li>
              </ul>
            </div>
            <div class="tab-pane fade page-type-links" id="panell3" role="tabpanel">
              <h5><strong>Details of Syllabus/Programmes in PhD</strong></h5>
              <h6 class="red-text" v-if="!dept.syllabus.PhD">
                Not Available at the moment
              </h6>
              <ul class="list-group list-gr">
                <li v-for="list,index in dept.syllabus.PhD">
                  <a class="list-group-item" :href="list.file">{{ list.title }}</a>
                </li>
              </ul>
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
                  <strong><span class="blue-text">Joined the Institute in {{ convertYear(dept.hod.joining_year) }}
                  </span></strong>
                </card-testimonial>
              </div>
            </div>
          </div>
        </div>

        <div class="tab-pane fade big-list" id="li4" role="tabpanel" aria-labelledby="li4-list">
          <h3 class="pane-title" align="left">Peoples</h3>
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
                    <span class="carousel-title">FACULTY</span>
                    <div class="carousel-inner person-list" role="listbox">
                      <div class="carousel-item active">
                        <div class="row">

                          <div class="col" v-for="person in dept.people.faculty">
                            <card-testimonial :name="person.name"
                              :id="person.id"
                              :image="person.image"
                              :desig="person.designation">
                              <strong>-- Research Interest --</strong><br>
                              <a :href="'/faculty/' + person.id">
                                <span v-html="stripDesc(person.research_interest)"></span><br>
                              </a>
                              <i class="fa fa-envelope"></i><br>
                              <strong>{{ person.email }}</strong><br>
                              <i class="fa fa-address-book"></i><br>
                              <strong>+91-{{ person.mobile }}</strong></br>
                              <strong><span class="blue-text">Joined the Institute in {{ convertYear(person.joining_year) }}
                              </span></strong>
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
              <span class="carousel-title">STAFF</span>
              <div class="container-fluid">
                <div class="row">
                  <div class="col staffs" v-for="person in dept.people.staff">
                    <card-testimonial
                      :name="person.name"
                      :image="person.image"
                      :desig="person.designation"/>
                  </div>
                </div>
              </div>
            </div>
            <div class="tab-pane fade page-type-links" id="p4l3" role="tabpanel">
              <span class="carousel-title">STUDENTS</span>
              <ul class="list-group list-gr">
                <li v-for="link in dept.people.students">
                  <a class="list-group-item" target="new" :href="link.file">
                    {{ link.title }}
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="tab-pane fade big-list" id="li5" role="tabpanel" aria-labelledby="li5-list">
          <h3 class="pane-title" align="left">Research</h3>
          <h4><strong>Collaboration with Academic and Research Institutions in recent times</strong></h4>
          <div class="card">
            <div class="card-body">
              <table-renderer :theader="research_header" :table="dept.research"></table-renderer>
            </div>
          </div>
        </div>

        <div class="tab-pane fade big-list" id="li6" role="tabpanel" aria-labelledby="li5-list">
          <h3 class="pane-title" align="left">Projects</h3>
          <h4 ><strong>Ongoing Sponsored Projects</strong></h4>
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

        <div class="tab-pane fade big-list" id="li8" role="tabpanel" aria-labelledby="li8-list">
          <h3 class="pane-title" align="left">Activities</h3>
          <h4 class="black-text"><strong>Programmes Hosted by the Department</strong></h4>
          <div class="card">
            <div class="card-body">
              <table-renderer :theader="activities_header" :table="dept.activities"></table-renderer>
            </div>
          </div>
        </div>

        <div class="tab-pane fade big-list" id="li9" role="tabpanel" aria-labelledby="li9-list">
          <div id="carousel-dept" class="carousel slide carousel-fade" data-ride="carousel">
            <ol class="carousel-indicators">
              <li v-for="(slide,index) in dept.photos" data-target="#carousel-home" :data-slide-to="index" :class="{ active: (index == 0) }"></li>
            </ol>
            <div class="carousel-inner" role="listbox">
              <div v-for="(slide,index) in dept.photos" class="carousel-item anim1" :class="{ active: (index == 0) }">
                <div class="view">
                  <img class="d-block w-100" :src="genBackendURL(slide.image, true)" :alt="['Slide ' + (index+1)]">
                  <div class="mask rgba-black-light"></div>
                </div>
                <div class="carousel-caption">
                  <h5 class="h5-responsive" style="color:#fff">{{ slide.title }}</h5>
                </div>
              </div>
            </div>
            <a class="carousel-control-prev" href="#carousel-dept" role="button" data-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carousel-dept" role="button" data-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="sr-only">Next</span>
            </a>
          </div>
        </div>

        <div class="tab-pane fade big-list" id="li10" role="tabpanel" aria-labelledby="li10-list">
          <p align="center" v-html="dept.contact_us">
          </p>
        </div>
      </div>
    </sp-card>
  </div>
</template>
<script>
import axios from 'axios'
import Newsfeed from './Newsfeed'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import { genBackendURL, stripDesc, convertNewsfeed } from '@/common.js'
import TableRenderer from '@/components/TableRenderer'
import CardCollapse from '@/components/CardCollapse'
import CardTestimonial from '@/components/CardTestimonial'
import SpCard from '@/components/SpCard'

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
      ],
      activities_header: [
        'Programme',
        'Speakers',
        'Start Date',
        'End Date',
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
                  this.dept.news = convertNewsfeed(this.dept.news)
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
    stripDesc: stripDesc,
    genBackendURL: genBackendURL,
    convertYear: function (year) {
      return year == 1959 ? "N/A" : year
    }
  },
  components: {
    LinksPage,
    Newsfeed,
    Card,
    TableRenderer,
    CardCollapse,
    CardTestimonial,
    SpCard
  }
}
</script>

<style>
  .l2-idep {
    margin-top: 20px;
  }
  @media screen and (max-width: 600px){
    .l2-idep .tab-content{
      padding-left:5px;
      padding-right:5px;
    }
  }
  .l2-idep .l2-card .down-content .big-list .mb-0{
    font-size: 75%;
  }
  .l2-idep .l2-card .down-content .tab-pane .tab-content{
    background: none;border:dotted 1px #ECEFF1;
  }
  .l2-idep .l2-card {
    background: linear-gradient(#ECEFF1,#B0BEC5);
  }
  .l2-idep .l2-card div.tile-title{
    background: #001333;
  }
  .l2-idep .l2-card p.tile-title-text{
    color: #ffffff;
  }
  .l2-idep .l2-card .down-content{
    background-color:#ffffff;
  }
  .l2-idep .l2-card .down-content .pane-text{
    text-align: justify;
    color:#000000;
  }
  .l2-idep .l2-card .down-content .pane-title{
    text-align: justify;
    color:#000000;
  }
  .l2-idep .l2-card .down-content .big-list h5{
    color:#000000;
  }
  .l2-idep{
    padding-top: 5em;
    padding-bottom: 1em;padding-right: 1.5%;padding-left: 1.5%;
  }
  .l2-idep .card-body .down-content .caros .carousel-title{
    font-size: 180%;
  }
  .l2-idep .card-body .down-content .carousel-item .col{
    width: 100%;margin: 5px;max-width: 500px ! important;min-width: 200px !important;
  }
  .l2-idep .card-body .down-content .avatar{
    max-height: 100px;max-width: 100px;
  }
  .l2-idep .card-body .down-content .min-profile{
    font-size:55%;
  }
  .l2-idep .card-body .down-content .testimonial-card .card-title{
    font-size: 100%;
  }
  .l2-idep .card-body .down-content .testimonial-card .desig{
    font-size: 100%;
  }
  .l2-idep .card-body .down-content #li7 .col{
    min-width: 100%;
  }
  .l2-idep .card-body .up-content .classic-tabs .nav-link{
    font-size: 100%;
  }
  .l2-idep .card-body .up-content .classic-tabs .nav-item{
    margin: 0;
  }
  .l2-idep .card-body .up-content .classic-tabs .nav-item a{
    font-weight: bold;
    padding:10px;
  }
  .l2-idep .card-body .down-content #li2 .accordion .card-header{
    border:solid 1px black;
  }
  .l2-idep .card-body .down-content .table .th-lg{
    min-width: 5px;
  }
  .l2-idep .card-body .down-content .table td{
    font-weight: bold;
  }
  .l2-idep .card-body .down-content .table th{
    font-weight: bold;
  }
  .l2-idep .card-body .down-content #li3 h6{
    margin-top: -1em;
  }
  .l2-idep .card-body .down-content #li3 .col{
    padding-left: 250px;padding-right: 250px;
  }
  .l2-idep .card-body .down-content .testimonial-card hr{
    margin:5px;
  }
  .l2-idep .card-body .down-content .carousel-inner .col{
    max-width: 20%;margin: 2px;
  }
  .l2-idep .card-body .down-content .caros{
    margin-bottom: -45px !important;
  }
  .l2-idep .card-body .down-content .card-up{
    height: 80px;
  }
  .l2-idep .card-body .down-content .card-body-in .card-title{
    font-size: 75%;
  }
  .l2-idep .card-body .down-content .card-body-in h6{
    font-size: 75%;
  }
  .l2-idep .card-body .down-content .avatar{
    height: 80px;width: 80px;
  }
  .l2-idep .card-body .down-content .min-profile{
    font-size:55%;
    padding-left: 5px;
    padding-right: 5px;
  }
  .l2-idep .card-body .down-content #li4 .controls-top{
    margin-bottom: 10px;
  }
  .l2-idep #li4 .staffs{
    max-width: 220px!important;min-width: 220px!important;
  }
  .l2-idep #li4 .person-list .col{
    max-width: 220px!important;min-width: 220px!important;
  }
  @media screen and (max-width: 600px){
    .l2-idep #li4 .person-list .col{
      max-width: 100%!important;min-width: 100%!important;
    }
    .l2-idep #li4 .staffs{
      max-width: 100%!important;min-width: 100%!important;
    }
  }
  .l2-idep .card-body .down-content #li4 .controls-top i{
    font-size: 60%;margin-top: -20px;
  }
  .l2-idep .card-body .down-content #li4 h6{
    margin-top: -1em;
  }
  .l2-idep .card-body .down-content #li4 hr{
    margin-left: 2em;margin-right: 2em;
  }
  .l2-idep .card-body .down-content .table-wrapper-2{
    display: block;max-height: 2500px;overflow-y: auto;-ms-overflow-style: -ms-autohiding-scrollbar;
  }
  .l2-idep .card-body .down-content #li2 th{
    background-color: #E0E0E0;
    padding: 2px;
  }
  .l2-idep .card-body .down-content #li2 td{
    background-color: #F5F5F5;
    padding: 2px;
  }
  .l2-idep .card-body .down-content th{
    background-color: #E0E0E0;
    padding: 5px;
  }
  .l2-idep .card-body .down-content td{
    background-color: #F5F5F5;
    padding: 5px;
  }
  .l2-idep .card-body .down-content #li7 .tab-content{
    font-size: 80%;
  }
  .l2-idep .card-body{
    margin-top: -0.5em;margin-bottom: -0.5em;margin-left: -0.5em;margin-right:-0.5em;
  }
  .l2-idep .tile-title-text{
    letter-spacing: 2px;font-weight: bold;text-align: center;vertical-align: middle;line-height: 1px;color: #ffffff;
  }
  .l2-idep .tile-title{
    height: 1px;
  }
  .l2-idep .tile-small-text{
    font-size: 90%;font-weight: bold;
  }
  .l2-idep .card-body .down-content #li4 .card-up{
    background: linear-gradient(to right,#001333,#26C6DA);
  }
  .l2-idep .card-body .down-content #li3 .card-up{
    background: linear-gradient(to right,#001333,#26C6DA);
  }
  .l2-idep .card-body .up-content .classic-tabs{
    background-color: #001333;
  }
  .l2-idep .down-content .pills-secondary .nav-link.active{
    background-color: #001333 !important;
    color: #ECEFF1;
  }
  .l2-idep .down-content .tab-pane .nav-link{
    background-color: #E0E0E0;
    color: #78909C;
  }
  .l2-idep .card-body .down-content #li4 .controls-top .btn-floating{
    background-color: #001333;
    height: 25px;width: 25px;margin: 2px ! important;
  }
  .l2-idep .card-body .down-content #li4 .carousel-indicators li{
    background-color: #001333;
  }
  .l2-idep .card-body .down-content #li4 .carousel-indicators li.active{
    background-color: #001333;
  }
  .l2-idep .card-body .down-content .carousel-title{
    font-weight: bold;letter-spacing: 2px;font-size: 150%;color:#000000;
  }
  .classic-tabs li a.active {
    border: 1px solid !important;
    border-radius: 5px;
    color: inherit !important;
  }
</style>
