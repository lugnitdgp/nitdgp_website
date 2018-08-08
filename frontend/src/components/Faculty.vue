<template>
  <div class="l3-fac">
    <sp-card containerclass="l3-card">
      <div slot="header">
        <p class="tile-title-text">
          <a class="white-text" :href="'/department/' + faculty.dept_short_code">
            FACULTY | {{ faculty.dept_short_code }}
          </a>
          <span v-if="!general" @click="general = true">
            - Show
          </span>
        </p>
      </div>
      <div class="container-fluid card fac-sm">
        <div class="row">
          <div class="photo" :class="getClassImg()">
            <img :src="faculty.image" style="border: solid grey 2px;max-width: 100%; max-height: 100%">
            <p style="font-weight: bold">{{ faculty.name }}</p>
            <p>{{ faculty.designation }}</p>
            <i class="fa fa-mortar-board"></i><br>
            <span v-html="faculty.education" style="font-size: 80%"/>
            <p style="font-size: 80%">
              <strong v-if="faculty.joining_year==1959" >Joined in N/A<br></strong>
              <strong v-if="faculty.joining_year!=1959" >Joined in {{ faculty.joining_year }}<br></strong>
              <i class="fa fa-envelope"></i><br>
              {{ faculty.email }}
            </p>
          </div>
          <div class="downc card tab-content" :class="getClassContent()">
            <button class="btn" type="button" @click="showNav($event)">
              <i class="fa fa-bars fa-2x"></i>
            </button>
            <div class="tab-pane fade show active big-list" id="li1" role="tabpanel">
              <h3 class="pane-title" align="left">Education</h3>
              <hr>
              <span v-if="'education' in faculty" v-html="faculty.education"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>

            <div class="tab-pane fade big-list" id="li2" role="tabpanel">
              <h3 class="pane-title" align="left">Work Experiences</h3>
              <hr>
              <span v-if="'work_experience' in faculty" v-html="faculty.work_experience"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>

            <div class="tab-pane fade big-list" id="li3" role="tabpanel">
              <h3 class="pane-title" align="left">Research Interest</h3>
              <hr>
              <span v-if="'research_interest' in faculty" v-html="faculty.research_interest"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>

            <div class="tab-pane fade big-list" id="li4" role="tabpanel">
              <h3 class="pane-title" align="left">Projects</h3>
              <hr>
              <span v-if="'projects' in faculty" v-html="faculty.projects"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>

            <div class="tab-pane fade big-list" id="li5" role="tabpanel">
              <h3 class="pane-title" align="left">Publication</h3>
              <hr>
              <ul class="nav md-pills nav-justified pills-secondary">
                <li class="nav-item">
                  <a class="nav-link active" data-toggle="tab" href="#p5l1" role="tab">Journal/Conference</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#p5l2" role="tab">Books/Patnets</a>
                </li>
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade in show active" id="p5l1" role="tabpanel">
                  <table-renderer :theader="pub_header" :table="faculty.publication"></table-renderer>
                </div>
                <div class="tab-pane fade page-type-links" id="p5l2" role="tabpanel">
                  <ul class="list-group list-gr">
                    <li v-for="link in faculty.books_and_patents">
                      <a class="list-group-item" target="new" :href="link.url || link.file">
                        {{ link.title }}
                      </a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>

            <div class="tab-pane fade big-list" id="li6" role="tabpanel">
              <h3 class="pane-title" align="left">Teachings</h3>
              <hr>
              <ul class="nav md-pills nav-justified pills-secondary">
                <li class="nav-item">
                  <a class="nav-link active" data-toggle="tab" href="#p6l1" role="tab">B-Tech &amp; M-Tech</a>
                </li>
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade in show active" id="p6l1" role="tabpanel">
                  <div class="accordion" id="accordionEx" role="tablist" aria-multiselectable="true">
                    <div class="card">
                      <div class="card-header" role="tab" id="heading11">
                        <a data-toggle="collapse" data-parent="#accordionEx" href="#collapse11" aria-expanded="true" aria-controls="collapse11">
                          <p class="mb-0">
                            ODD SEMESTER <i class="fa fa-angle-down rotate-icon"></i>
                          </p>
                        </a>
                      </div>
                      <div id="collapse11" class="collapse" role="tabpanel" aria-labelledby="heading11">
                        <div class="card-body">
                          <table-renderer :theader="subj_header" :table="faculty.teachings"></table-renderer>
                        </div>
                      </div>
                    </div>
                    <div class="card">
                      <div class="card-header" role="tab" id="heading12">
                        <a data-toggle="collapse" data-parent="#accordionEx" href="#collapse12" aria-expanded="true" aria-controls="collapse12">
                          <p class="mb-0">
                            EVEN SEMESTER <i class="fa fa-angle-down rotate-icon"></i>
                          </p>
                        </a>
                      </div>
                      <div id="collapse12" class="collapse" role="tabpanel" aria-labelledby="heading12">
                        <div class="card-body">
                          <table-renderer :theader="subj_header" :table="faculty.teachings"></table-renderer>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="tab-pane fade big-list" id="li7" role="tabpanel">
              <h3 class="pane-title" align="left">List of students</h3>
              <hr>
              <span v-if="'students' in faculty" v-html="faculty.students"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>
            <div class="tab-pane fade big-list" id="li8" role="tabpanel">
              <h3 class="pane-title" align="left">Awards and Recognitions</h3>
              <hr>
              <span v-if="'awards_and_recognition' in faculty" v-html="faculty.awards_and_recognition"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>
            <div class="tab-pane fade big-list" id="li9" role="tabpanel">
              <h3 class="pane-title" align="left">Administrative Responsibilities</h3>
              <hr>
              <span v-if="'administrative_responsibilities' in faculty" v-html="faculty.administrative_responsibilities"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>
            <div class="tab-pane fade big-list" id="li10" role="tabpanel">
              <h3 class="pane-title" align="left">Contact</h3>
              <hr>
              <span v-if="'contact' in faculty" v-html="faculty.contact"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>
          </div>
          <div class="list-group" :class="extraNavClasses.concat([getClassNav()])">
            <a class="dropdown-item active" :class="!('education' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li1" role="tab">Education</a>
            <a class="dropdown-item" :class="!('work_experience' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li2" role="tab">Work Experience</a>
            <a class="dropdown-item" :class="!('research_interest' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li3" role="tab">Research Interest</a>
            <a class="dropdown-item" :class="!('projects' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li4" role="tab">Projects</a>
            <a class="dropdown-item" :class="!('publication' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li5" role="tab">Publication</a>
            <a class="dropdown-item" :class="!('teachings' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li6" role="tab">Teachings</a>
            <a class="dropdown-item" :class="!('students' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li7" role="tab">Students</a>
            <a class="dropdown-item" :class="!('awards_and_recognition' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li8" role="tab">Awards and recognitions</a>
            <a class="dropdown-item" :class="('administrative_responsiblities' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li9" role="tab">Administrative Responsibilities</a>
            <a class="dropdown-item" :class="!('contact' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li10" role="tab">Contact</a>
          </div>
          <div v-show="nav" id="fade" class="black_overlay"></div>
        </div>
      </div>
    </sp-card>
  </div>
</template>
<script>
import axios from 'axios'
import { genBackendURL } from '@/common.js'
import TableRenderer from '@/components/TableRenderer'
import CardCollapse from '@/components/CardCollapse'
import SpCard from '@/components/SpCard'

export default {
  name: 'Faculty',
  data () {
    return {
      faculty: {},
      pub_header: [
        'Author(s)',
        'Title',
        'Name of Journal/Conference',
        'Year'
      ],
      subj_header: [
        'title',
        'short_code',
        'semester',
        'credits'
      ],
      general: true,
      windowWidth: 1000,
      extraNavClasses: [],
      nav: false
    }
  },
  created () {
    axios.get(genBackendURL("faculty/" + this.$route.params.id))
         .then(response => {
           this.faculty = response.data
           for (var key in this.faculty) {
             if (this.faculty.hasOwnProperty(key) &&
                 Object.keys(this.faculty[key]).length === 0) {
               delete this.faculty[key];
             }
           }
           console.log(this.faculty)
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
           window.location = '/NotAvailable'
         })
    window.addEventListener('resize', this.updateWidth)
    this.windowWidth = document.body.clientWidth
  },
  mounted () {
    Array.from(document.getElementsByClassName('dropdown-item')).forEach(el => {
      console.log("Hiding Div", el)
      el.addEventListener('click', this.hideNav)
    })
  },
  methods: {
    hideNav () {
      this.nav = false
      this.extraNavClasses = []
    },
    showNav (event) {
      console.log(event)
      this.extraNavClasses = ['lift', 'div-block']
      this.nav = true
      document.getElementsByClassName('lift')[0].style.top = event.clientY.toString() + 'px'
    },
    getClassImg () {
      let width = this.windowWidth
      if (width > 1180)
        return 'col-2'
      else if (width > 900)
        return 'col-3'
      else if (width > 600)
        return 'col-4'
      else
        return 'col-12'
    },
    getClassContent () {
      let width = this.windowWidth
      if (width > 1180)
        return 'col-8'
      else if (width > 900)
        return 'col-6'
      else if (width > 600)
        return 'col-8'
      else
        return 'col-12'
    },
    getClassNav () {
      let width = this.windowWidth
      if (width > 1180)
        return 'col-2'
      else if (width > 900)
        return 'col-3'
      else
        return 'div-none'
    },
    updateWidth () {
      this.windowWidth = document.body.clientWidth
    }
  },
  components: {
    TableRenderer,
    CardCollapse,
    SpCard
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateWidth);
  }
}
</script>

<style scoped>
    .list-group a, .list-group a:hover {
      white-space: pre-wrap;
    }
    .dropdown-item:hover{
      background-color: #001333!important;
      color: #fff!important;
    }
    .photo {
      text-align: center;
    }
    .downc {
      margin: 0 auto;
      padding: 10px;
    }
    .btn {
      background: #001333;
      width: 50px;
      padding: 10px;
      float: right;
      margin-left: auto;
      margin-bottom: 0px;
    }
    @media screen and (min-width: 909px) {
      .btn {
        display: none;
        height: 0px;
      }
    }
    .lift {
      position: absolute;
      left: 10%;
      width: 80%;
      background-color: white;
      z-index: 2;
      overflow: auto;
    }
    .black_overlay {
      position: absolute;
      top: 0%;
      left: 0%;
      bottom: 0%;
      width: 100%;
      height: 100%;
      z-index: 1;
      background-color: black;
      -moz-opacity: 0.8;
      opacity: .80;
      filter: alpha(opacity=80);
    }
</style>
