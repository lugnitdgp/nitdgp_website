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
      <div class="container-fluid fac-sm">
        <div class="row">
          <div class="photo" :class="getClassImg()">
            <img :src="faculty.image" style="max-width: 100%; max-height: 100%">
            <h4><p style="font-weight: bold">{{ faculty.name }}</p></h4>
            <p>{{ faculty.designation }}</p>
            <p style="font-size: 80%">
              <strong v-if="joining_year==1959" >Joined in N/A<br></strong>
              <strong v-if="joining_year!=1959" >Joined in {{ joining_year }}<br></strong>
              <i class="fa fa-envelope"></i><br>
              {{ faculty.email }}
            </p>
          </div>
          <div class="downc tab-content" :class="getClassContent()">
            <button class="btn" type="button" @click="showNav($event)">
              <i class="fa fa-bars fa-2x"></i>
            </button>
            <div class="tab-pane fade show active big-list" id="li1" role="tabpanel">
              <h4 class="pane-title" align="left">Education</h4>
              <hr>
              <span v-if="'education' in faculty" v-html="faculty.education"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>

            <div class="tab-pane fade big-list" id="li2" role="tabpanel">
              <h4 class="pane-title" align="left">Work Experiences</h4>
              <hr>
              <span v-if="'work_experience' in faculty" v-html="faculty.work_experience"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>

            <div class="tab-pane fade big-list" id="li3" role="tabpanel">
              <h4 class="pane-title" align="left">Research Interest</h4>
              <hr>
              <span v-if="'research_interest' in faculty" v-html="faculty.research_interest"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>

            <div class="tab-pane fade big-list" id="li4" role="tabpanel">
              <h4 class="pane-title" align="left">Projects</h4>
              <hr>
              <span v-if="'projects' in faculty" v-html="faculty.projects"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>

            <div class="tab-pane fade big-list" id="li5" role="tabpanel">
              <h4 class="pane-title" align="left">Publication</h4>
              <hr>
              <ul class="nav md-pills nav-justified pills-secondary">
                <li class="nav-item">
                  <a class="nav-link active" data-toggle="tab" href="#p5l1" role="tab">Journal</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#p5l2" role="tab">Conference</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#p5l3" role="tab">Books</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#p5l4" role="tab">Patents</a>
                </li>
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade in show active" id="p5l1" role="tabpanel">
                  <h4>Journals</h4>
                  <table-renderer :table="faculty.journals" :theader="['Citation','Journal','Year']" />
                </div>
                <div class="tab-pane fade page-type-links" id="p5l2" role="tabpanel">
                  <ul class="list-group list-gr">
                    <h4>Conferences</h4>
                    <table-renderer :table="faculty.conferences" :theader="['Citation','Location','Year']" />
                  </ul>
                </div>
                <div class="tab-pane fade in" id="p5l3" role="tabpanel">
                  <h4>Books</h4>
                  <ul>
                    <li v-for="book in faculty.books" >
                      <a v-if="book.file" :href="book.file" target="new">
                        <div v-html="book.title"></div>
                      </a>
                      <a v-else :href="book.url" target="new">
                        <div v-html="book.title"></div>
                      </a>
                    </li>
                  </ul>
                </div>
                <div class="tab-pane fade in" id="p5l4" role="tabpanel">
                  <h4>Patents</h4>
                    <ul>
                      <li v-for="patent in faculty.patents" >
                        <a v-if="patent.file" :href="patent.file" target="new">
                          <div>{{  patent.title }}</div>
                        </a>
                        <a v-else href="#">
                          <div v-html="patent.title"></div>
                        </a>
                      </li>
                    </ul>
                </div>
              </div>
            </div>

            <div class="tab-pane fade big-list" id="li6" role="tabpanel">
              <h4 class="pane-title" align="left">Teachings</h4>
              <hr>
              <div v-if="'notes' in faculty" class="table-wrapper-2 table-bordered">
                <table class="table table-responsive-md">
                  <thead class="mdb-color lighten-4">
                    <tr>
                      <th class="th-lg" v-for="thead in ['Subject Name','Subject Code','Semester','Degree','Download Key']">
                        {{ thead }}
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(row, i) in faculty.notes">
                      <td v-for="(data,key) in row" v-if="key != 'id'">
                        <span v-if="key != 'input_key'" v-html="data" />
                        <form v-else-if="key == 'input_key' && data != 'Notes Not Available'"
                          @submit.prevent="download_note(faculty.notes[i]['id'], data)">
                          <input v-model="faculty.notes[i][key]" />
                          <input type="submit" class="btn-primary" value="Submit" />
                        </form>
                        <span v-else-if="key == 'input_key' && data == 'Notes Not Available'" v-html="data" />
          </span>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <br>
              <span v-if="'teachings' in faculty" v-html="faculty.teachings"/>
              <h4 v-else-if="!('notes' in faculty || 'teachings' in faculty)" class="red-text">Not Available</h4>
            </div>
            <div class="tab-pane fade big-list" id="li7" role="tabpanel">
              <h4 class="pane-title" align="left">List of students</h4>
              <hr>
              <div v-if="'students' in faculty">
                <div class="carousel-inner person-list" role="listbox">
                  <div class="carousel-item active">
                    <div class="row">
                      <card-testimonial v-for="(student, i) in faculty.students" :key="i"
                        class="staffs"
                        :name="student.name"
                        :image="student.image"
                        :desig="student.degree + ' (' + student.type + ')'">
                        {{student.description}}
                      </card-testimonial>
                    </div>
                  </div>
                </div>
              </div>
              <h4 v-else class="red-text">Not Available</h4>
            </div>
            <div class="tab-pane fade big-list" id="li8" role="tabpanel">
              <h4 class="pane-title" align="left">Awards and Recognitions</h4>
              <hr>
              <span v-if="'awards_and_recognition' in faculty" v-html="faculty.awards_and_recognition"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>
            <div class="tab-pane fade big-list" id="li9" role="tabpanel">
              <h4 class="pane-title" align="left">Administrative Responsibilities</h4>
              <hr>
              <span v-if="'administrative_responsibilities' in faculty" v-html="faculty.administrative_responsibilities"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>
            <div class="tab-pane fade big-list" id="li10" role="tabpanel">
              <h4 class="pane-title" align="left">Contact</h4>
              <hr>
              <span>Mobile : +91-{{mobile}}<br/>
                    Email : {{faculty.email}}<br/>
              </span>
            </div>
            <div class="tab-pane fade big-list" id="li11" role="tabpanel">
              <h4 class="pane-title" align="left">Miscellanous</h4>
              <hr>
              <span v-if="'misc' in faculty" v-html="faculty.misc"/>
              <h4 v-else class="red-text">Not Available</h4>
            </div>
          </div>
          <div class="list-group"
            :class="extraNavClasses.concat([getClassNav()])"
            :style="{ top: popUpTop + 'px' }">
            <a class="dropdown-item active" :class="{ 'disabled': !('education' in faculty) }" data-toggle="list" href="#li1" role="tab">Education</a>
            <a class="dropdown-item" :class="{ 'disabled': !('work_experience' in faculty) }" data-toggle="list" href="#li2" role="tab">Work Experience</a>
            <a class="dropdown-item" :class="{ 'disabled': !('research_interest' in faculty) }" data-toggle="list" href="#li3" role="tab">Research Interest</a>
            <a class="dropdown-item" :class="{ 'disabled': !('projects' in faculty) }" data-toggle="list" href="#li4" role="tab">Projects</a>
            <a class="dropdown-item" data-toggle="list" href="#li5" role="tab">Publication</a>
            <a class="dropdown-item" :class="{ 'disabled': !('teachings' in faculty || 'notes' in faculty) }" data-toggle="list" href="#li6" role="tab">Teachings</a>
            <a class="dropdown-item" :class="{ 'disabled': !('students' in faculty) }" data-toggle="list" href="#li7" role="tab">Students</a>
            <a class="dropdown-item" :class="{ 'disabled': !('awards_and_recognition' in faculty) }" data-toggle="list" href="#li8" role="tab">Awards and recognitions</a>
            <a class="dropdown-item" :class="{ 'disabled': !('administrative_responsibilities' in faculty) }" data-toggle="list" href="#li9" role="tab">Administrative Responsibilities</a>
            <a class="dropdown-item" data-toggle="list" href="#li10" role="tab">Contact</a>
            <a class="dropdown-item" data-toggle="list" href="#li11" role="tab">Miscellanous</a>
            <a class="dropdown-item faculty-login" :href="genBackendURL('admin')" target="new" role="tab">Faculty Login</a>
          </div>
        </div>
      </div>
    </sp-card>
    <div v-show="nav" id="fade" class="black_overlay"></div>
  </div>
</template>
<script>
import axios from 'axios'
import { genBackendURL, backURL } from '@/common.js'
import TableRenderer from '@/components/TableRenderer'
import CardCollapse from '@/components/CardCollapse'
import SpCard from '@/components/SpCard'
import CardTestimonial from '@/components/CardTestimonial'

export default {
  name: 'Faculty',
  data () {
    return {
      faculty: {},
      mobile: 0,
      joining_year: "",
      general: true,
      windowWidth: 1000,
      extraNavClasses: [],
      nav: false,
      popUpTop: 0,
      top: -1
    }
  },
  created () {
    axios.get(genBackendURL("faculty/" + this.$route.params.id))
         .then(response => {
           this.faculty = response.data.faculty[0]
           this.mobile = this.faculty.mobile
           this.joining_year = this.faculty.joining_year
           for (let key in this.faculty) {
             if (this.faculty.hasOwnProperty(key)) {
               if (Object.keys(this.faculty[key]).length === 0) {
                 delete this.faculty[key]
               }
             }
           }
           this.$emit('hideloader', true)
         })
         .catch(e => {
           window.location = '/NotAvailable'
         })
    window.addEventListener('resize', this.updateWidth)
    this.windowWidth = document.body.clientWidth
  },
  mounted () {
    Array.from(document.getElementsByClassName('dropdown-item')).forEach(el => {
      el.addEventListener('click', this.hideNav)
    })
  },
  methods: {
    genBackendURL: genBackendURL,
    hideNav () {
      this.nav = false
      this.extraNavClasses = []
      this.popUpTop = 0
    },
    showNav (event) {
      this.extraNavClasses = ['lift', 'div-block']
      this.nav = true
      this.popUpTop = event.clientY + this.top * 200
    },
    getClassImg () {
      let width = this.windowWidth
      if (width > 1180)
        return 'col-2'
      else if (width > 900)
        return 'col-2'
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
        return 'col-7'
      else if (width > 600) {
        this.top = -1
        return 'col-8'
      }
      else {
        this.top = 1
        return 'col-12'
      }
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
    },
    download_note (id, input) {
      let data = new FormData()
      data.append('id', id)
      data.append('input_key', input)
      axios({
	method: 'post',
	url: genBackendURL('faculty/notes'),
	data: data,
      })
          .then(response => {
            window.location.href = backURL + response.data.download_url
          })
          .catch(e => {
            alert("Wrong download key")
          })
    }
  },
  components: {
    TableRenderer,
    CardCollapse,
    SpCard,
    CardTestimonial
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateWidth);
  }
}
</script>

<style scoped>
  .staffs {
    min-width: 200px !important;
    min-height: 300px !important;
    max-width: 500px !important;
    max-height: 500px !important;
    padding: 10px !important;
  }
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
  .dropdown-item.faculty-login {
    background-color: #8f8;
  }
  .dropdown-item.faculty-login:hover {
    background-color: #0f0!important;
  }
</style>
