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
        <div v-if="general" @dblclick="general = false" class="row">
          <div class="col-4">
            <img :src="faculty.image" style="border: solid grey 2px;max-width: 100%; max-height: 100%">
          </div>
          <div class="col-8" style="min-height: 100%">
            <p style="font-size: 160%;font-weight: bold">{{ faculty.name }}</p>
            <p style="font-weight: bold">{{ faculty.designation }}</p>
            <i class="fa fa-mortar-board"></i><br>
            <span v-html="faculty.education" style="font-size: 80%"/>
            <p style="font-size: 80%">
              <strong v-if="faculty.joining_year==1959" >Joined in N/A<br></strong>
              <strong v-if="faculty.joining_year!=1959" >Joined in {{ faculty.joining_year }}<br></strong>
              <i class="fa fa-envelope"></i><br>
              {{ faculty.email }}
            </p>
          </div>
        </div>
        <div class="dropdown" style="text-align: center">
          <button class="btn btn-lg dropdown-toggle" type="button" id="dropdownMenu5" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <i class="fa fa-bars fa-2x"> &nbsp; &nbsp; MENU</i>
          </button>
          <div class="dropdown-menu" id="list-tab" role="tablist">
            <div class="list-group">
              <a class="dropdown-item active" :class="!('education' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li1" role="tab">Education</a>
              <a class="dropdown-item" :class="!('work_experience' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li2" role="tab">Work Experience</a>
              <a class="dropdown-item" :class="!('research_interest' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li3" role="tab">Research Interest</a>
              <a class="dropdown-item" :class="!('projects' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li4" role="tab">Projects</a>
              <a class="dropdown-item" :class="!('publication' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li5" role="tab">Publication</a>
              <a class="dropdown-item" :class="!('teachings' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li6" role="tab">Teachings</a>
              <a class="dropdown-item" :class="!('students' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li7" role="tab">Students</a>
              <a class="dropdown-item" :class="!('awards_and_recognition' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li8" role="tab">Awards and recognitions</a>
              <a class="dropdown-item" :class="!('administrative_responsiblities' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li9" role="tab">Administrative Responsibilities</a>
              <a class="dropdown-item" :class="!('contact' in faculty) ? 'disabled' : ''" data-toggle="list" href="#li10" role="tab">Contact</a>
            </div>
          </div>
        </div>
      </div>
      <div class="downc card">
        <div class="tab-content">
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
      general: true
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
  },
  components: {
    TableRenderer,
    CardCollapse,
    SpCard
  }
}
</script>
