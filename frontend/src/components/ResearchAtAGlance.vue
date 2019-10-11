<template>
  <div class="l3-fac">
    <links-page>
      <card title="Research At a Glance">
        <ul class="nav md-pills nav-justified pills-secondary">
                <li class="nav-item">
                  <a class="nav-link active" data-toggle="tab" href="#p5l1" role="tab">Journals</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#p5l2" role="tab">Projects</a>
                </li>                
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#p5l3" role="tab">Patents</a>
                </li>
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade in show active" id="p5l1" role="tabpanel">
                  <h4>Journals</h4>
                  <!-- <div class="paginate">
                    <select v-model="alljournal" class="form-control bg-success">
                      <option v-for="jpage in journalpages">{{ jpage }}</option>
                    </select>
                  </div> -->
                  <table class="table table-bordered table-responsive">
                    <thead class="thead-dark">
                      <tr>
                        <th scope="col">SL. NO.</th>
                        <th scope="col">Title</th>
                        <th scope="col">Journal Name</th>
                        <th scope="col">Vol. & Page</th>
                        <th scope="col">Publisher</th>
                        <th scope="col">DOI</th>
                        <th scope="col">Year</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(journal,key) in alljournal">
                        <td>{{ key+1}}</td>
                        <td v-html="journal.title"></td>
                        <td>{{ journal.journal}}</td>
                        <td>{{ journal.vol_or_page}}</td>
                        <td>{{ journal.publisher}}</td>
                        <td>{{ journal.doi}}</td>                        
                        <td>{{ journal.year}}</td>
                      </tr>
                    </tbody>
                  </table>
                  <nav aria-label="Page navigation">
                    <ul class="pagination justify-content-center">
                      <li class="page-item bg-primary text-white active" style="margin-right: 5px;margin-top: 10px;">
                        <a class="page-link bordered" v-if="jprev != ''" @click="changeJournalPage(jprev)" href="#" tabindex="-1">Previous</a>
                      </li>                
                      <li class="page-item bg-primary text-white active" style="margin-right: 5px;margin-top: 10px;">
                        <a class="page-link bordered" v-if="jnext != ''" @click="changeJournalPage(jnext)" href="#">Next</a>
                      </li>
                    </ul>
                  </nav>
                </div>
                <div class="tab-pane fade page-type-links" id="p5l2" role="tabpanel">
                  <ul class="list-group list-gr">
                    <h4>Projects</h4>
                      <table class="table table-bordered table-responsive">
                        <thead class="thead-dark">
                          <tr>
                            <th class="col">Title</th>
                            <th class="col">Investigator</th>
                            <th class="col">Co-investigator</th>
                            <th class="col">Sponsered Agency</th>
                            <th class="col">Duration</th>
                            <th class="col">Status</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr v-for="project in allprojects">
                            <td v-html="project.projects"></td>
                            <td>{{ project.investigator}}</td>
                            <td>{{ project.co_investigator}}</td>
                            <td>{{ project.sponsored}}</td>
                            <td>{{ project.duration}}</td>
                            <td>{{ project.status}}</td>
                          </tr>
                        </tbody>
                      </table>
                      <nav aria-label="Page navigation">
                        <ul class="pagination justify-content-center">
                          <li class="page-item bg-primary text-white active" style="margin-right: 5px;margin-top: 10px;">
                            <a class="page-link bordered" v-if="prprev != ''" @click="changeProjectPage(prprev)" href="#" tabindex="-1">Previous</a>
                          </li>                
                          <li class="page-item bg-primary text-white active" style="margin-right: 5px;margin-top: 10px;">
                            <a class="page-link bordered" v-if="prnext != ''" @click="changeProjectPage(prnext)" href="#">Next</a>
                          </li>
                        </ul>
                      </nav>
                  </ul>
                </div>
                <div class="tab-pane fade in" id="p5l3" role="tabpanel">
                  <h4>Patents</h4>
                    <table class="table table-bordered table-responsive">
                        <thead class="thead-dark">
                          <tr>
                            <th class="col">Title</th>
                            <th class="col">Inventor</th>
                            <th class="col">Filed Year</th>
                            <th class="col">Link</th>
                            <th class="col">Status</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr v-for="patent in allpatents">
                            <td v-html="patent.title"></td>
                            <td>{{ patent.grantee_or_owner }}</td>
                            <td>
                              <span v-if="patent.year==1959">NA</span>
                              <span v-else>{{ patent.year}}</span>
                          </td>
                          <td>{{ patent.link }}</td>
                          <td>{{ patent.patent_status }}</td>
                          </tr>
                        </tbody>
                      </table>
                      <nav aria-label="Page navigation">
                        <ul class="pagination justify-content-center">
                          <li class="page-item bg-primary text-white active" style="margin-right: 5px;margin-top: 10px;">
                            <a class="page-link bordered" v-if="ptprev != ''" @click="changePatentPage(ptprev)" href="#" tabindex="-1">Previous</a>
                          </li>                
                          <li class="page-item bg-primary text-white active" style="margin-right: 5px;margin-top: 10px;">
                            <a class="page-link bordered" v-if="ptnext != ''" @click="changePatentPage(ptnext)" href="#">Next</a>
                          </li>
                        </ul>
                      </nav>
                </div>
                
            </div>         
        
            
      </card>
    </links-page>
    <!-- <div class="btn-group">
      <button v-if="next != ''" class="nit-btn"
        @click="changePage(next)">
        Next
      </button>
      <button v-if="prev != ''" class="nit-btn"
        @click="changePage(prev)">
        Previous
      </button>
    </div>  -->  
  </div>
</template>
<script>
import axios from 'axios'
import { genBackendURL, backURL } from '@/common.js'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'

export default {
  name: 'Researchataglance',
  data () {
    return {      
      alljournal:[],
      allprojects:[],
      allpatents:[],
      patentpages:1,
      journalpages:1,
      jpage:'',
      projectpages:1,
      jnext: '',
      jprev: '',
      prnext: '',
      prprev: '',
      ptnext: '',
      ptprev: ''
      
    }
  },
  created () {
    this.changeJournalPage(genBackendURL('activities/alljournal/'))
    this.changeProjectPage(genBackendURL('activities/allproject/'))
    this.changePatentPage(genBackendURL('activities/allpatent/'))
    this.$emit('hideloader', true)
        
  },
  methods:{
    changeJournalPage: function(url){
      axios.get(url)
           .then(response => {
             this.alljournal = response.data.results
             this.journalpages = Math.ceil(response.data.count/20)
             console.log(this.journalpages)
             if (response.data.next != null)             
               this.jnext = response.data.next

             else
               this.jnext = ''
             if (response.data.previous != null)
             {
               this.jprev = response.data.previous
             }
             else
               this.jprev = ''
           })
           .catch(e => {
             console.log("Axios(GET[information]): Error: " + e)
           })
    },
    changeProjectPage: function(url){
      axios.get(url)
           .then(response => {
             this.allprojects = response.data.results
             
             if (response.data.next != null)             
               this.prnext = response.data.next

             else
               this.prnext = ''
             if (response.data.previous != null)
             {
               this.prprev = response.data.previous
             }
             else
               this.prprev = ''
           })
           .catch(e => {
             console.log("Axios(GET[information]): Error: " + e)
           })
    },
    changePatentPage: function(url){
      axios.get(url)
           .then(response => {
             this.allpatents = response.data.results
             
             if (response.data.next != null)             
               this.ptnext = response.data.next

             else
               this.ptnext = ''
             if (response.data.previous != null)
             {
               this.ptprev = response.data.previous
             }
             else
               this.ptprev = ''
           })
           .catch(e => {
             console.log("Axios(GET[information]): Error: " + e)
           })
    }
  },
  components:{
    LinksPage,
    Card
  }
 
  
}
</script>

<style scoped>
  .pills-secondary .nav-link.active, .pills-secondary .show > .nav-link, .tabs-secondary {
    background-color: #00033f !important;
  }
  .md-pills .nav-link.active {
    color: #fff;
    background-color: #00033f;
  }
  .paginate{
    min-height: 100px;
    min-width: 300px;
    left: 50%;
    top:100px;
    background: #f2f8f8;
  }
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
  .custom-color{
    background: #1287A5;
    margin-right: 3px;
    color: #fff !important;
    font-size: 20px;
    font-weight:bold;
  }
  .bordered{
    border:0.5px solid #000 !important;
  }
  .classic-tabs li a{
    padding: 5px 5px !important;
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
