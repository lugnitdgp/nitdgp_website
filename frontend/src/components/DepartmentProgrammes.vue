<template>
  <div class="l2-idep">
    <sp-card v-if="dept" containerclass="l2-card" bodyclass="text-center">
      <p slot="header" class="tile-title-text">
        <a href="/departments" class="white-text sh-dex">Department of {{ dept.name }}</a>
        <a href="/departments" class="white-text sh-mob notranslate">Department of {{ dept.short_code }}</a>
      </p>
      <div class="tabs-wrapper up-content mx-auto">
        <ul class="nav classic-tabs" role="tablist">
          <li class="nav-item">
            <a class="nav-link waves-light" :href="'/department/'+this.$route.params.short_code" role="tab">About Us</a>
          </li>
          <li class="nav-item">
            <a class="nav-link waves-light active" :href="'/department/'+this.$route.params.short_code+'/programmes'" role="tab" >Programmes</a>
          </li>
          <li class="nav-item">
            <a class="nav-link waves-light" :href="'/department/'+this.$route.params.short_code+'/HOD'" role="tab" >HOD</a>
          </li>
          <li class="nav-item">
            <a class="nav-link waves-light" :href="'/department/'+this.$route.params.short_code+'/people'" role="tab" >People</a>
          </li>
          <li class="nav-item">
            <a class="nav-link waves-light" :class="{'disabled': !dept.research.length }" :href="'/department/'+this.$route.params.short_code+'/Research'" role="tab" >Research</a>
          </li>
          <li class="nav-item">
            <a class="nav-link waves-light" :class="{'disabled': !dept.projects.length }" :href="'/department/'+this.$route.params.short_code+'/Projects'" role="tab" >Projects</a>
          </li>
          <li class="nav-item">
            <a class="nav-link waves-light" :href="'/department/'+this.$route.params.short_code+'/Facilities'" role="tab" >Facilities</a>
          </li>
          <li class="nav-item">
            <a class="nav-link waves-light" :class="{'disabled': !dept.activities.length }" :href="'/department/'+this.$route.params.short_code+'/Activities'" role="tab" >Activities</a>
          </li>
          <li class="nav-item">
            <a class="nav-link waves-light" :class="{'disabled': !dept.photos.length }" :href="'/department/'+this.$route.params.short_code+'/Photo-Gallery'" role="tab">Photo Gallery</a>
          </li>
          <li class="nav-item">
            <a class="nav-link waves-light" :href="'/department/'+this.$route.params.short_code+'/Contact-us'" role="tab">Contact Us</a>
          </li>
        </ul>
      </div>
      <div class="tab-content card down-content">
        <div class="tab-pane fade show active big-list" id="li2" role="tabpanel" aria-labelledby="li2-list">
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
                  <span v-if="dept.name=='Electronics and Communication Engineering'"><a href="http://nitdgp.ac.in/AllPDF/NITD_ECE_NBA_2020_23.pdf" target="_blank">(Program accreditated by NBA)</a></span>
                  <div class="accordion" id="accordionEx" role="tablist" aria-multiselectable="true">
                    <div v-for="syllabus,sem in programme">
                      <card-collapse v-if="sem!='programme_title'" :title="'Semester '+sem">
                        <table-renderer :table="syllabus" :theader="['COURSE TITLE', 'CODE','L','T','S','C']"></table-renderer>
                      </card-collapse>
                    </div>
                  </div>
                </div>
              </div>
              <br>
              <collapse-list>
                <card-collapse v-for="(curriculum,i) in dept.previous_year_curriculum.UG"
                  :title="curriculum.title" :key="i">
                  <div v-html="curriculum.details" />
                </card-collapse>
              </collapse-list>
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
              <div v-if="dept.peo != ''">
                <hr>
                <h3 class="pane-text text-center"><strong>Programme Educational Objectives</strong></h3>
                <div v-html="dept.peo" />
              </div>
            </div>
            <div class="tab-pane fade page-type-links" id="panell2" role="tabpanel">

              <h5><strong>Details of Syllabus/Programmes in PG</strong></h5>
              <h6 class="red-text" v-if="!dept.syllabus.PG">
                Not Available at the moment
              </h6>
              <ul class="list-group list-gr">
                <li v-for="list,index in dept.syllabus.PG">
                  <a class="list-group-item" v-if="list.file!=null" :href="list.file">{{ list.title }}</a>
                  <a class="list-group-item" v-if="list.link!=''" target="blank" :href="list.link">{{ list.title }}</a>
                </li>
              </ul>
              <div v-if="dept.pgpeo != ''">
                <hr>
                <h3 class="pane-text text-center"><strong>Programme Educational Objectives</strong></h3>
                <div v-html="dept.pgpeo" /></div>
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
import ActivityRenderer from '@/components/ActivityRenderer'
import CardCollapse from '@/components/CardCollapse'
import CollapseList from '@/components/CollapseList'
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
        'Speakers',
        'Programme',
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
    ActivityRenderer,
    CardCollapse,
    CollapseList,
    CardTestimonial,
    SpCard
  }
}
</script>

<style>
  .card-test {
    min-width: 230px !important;
    min-height: 300px !important;
    max-width: 500px !important;
    max-height: 500px !important;
    padding: 10px !important;
  }
  .staffs {
    min-width: 200px !important;
    min-height: 300px !important;
    max-width: 500px !important;
    max-height: 500px !important;
    padding: 10px !important;
  }
  .l2-idep .sh-mob{
    display: none;
  }
  @media screen and (max-width: 750px){
    .l2-idep .sh-mob{
      display: block!important;
    }
    .l2-idep .sh-dex{
      display: none!important;
    }
  }
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
  .l2-idep .card-body .down-content .carousel-inner .col{
    max-width: 20%;margin: 2px;
  }
  .l2-idep .card-body .down-content .caros{
    margin-bottom: -45px !important;
  }
  .l2-idep .card-body .down-content .min-profile{
    font-size:55%;
    padding-left: 5px;
    padding-right: 5px;
  }
  .l2-idep .card-body .down-content #li4 h6{
    margin-top: -1em;
  }
  .l2-idep .card-body .down-content .table-wrapper-2{
    display: block;max-height: 2500px;overflow-y: auto;-ms-overflow-style: -ms-autohiding-scrollbar;
  }
  .l2-idep .card-body .down-content th{
    background-color: #E0E0E0;
    padding: 6px;
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
