<template>
  <links-page>
    <card title="Collaboration">
      <ul class="nav nav-tabs nav-justified not-tab">
        <li class="nav-item">
          <a v-if="$route.params.tab === 'national'" class="nav-link active show" data-toggle="tab" href="#panel3" role="tab">National Collaboration</a>
          <a v-else class="nav-link active show" data-toggle="tab" href="#panel3" role="tab">National Collaboration</a>
        </li>
        <li class="nav-item">
          <a v-if="$route.params.tab === 'international'" class="nav-link " data-toggle="tab" href="#panel1" role="tab">International Collaboration</a>
          <a v-else class="nav-link" data-toggle="tab" href="#panel1" role="tab">International Collaboration</a>
        </li>
      </ul>
      <div class="tab-content card">

        <div v-if="$route.params.tab === 'international'" class="tab-pane " id="panel1" role="tabpanel">
          <notice-list :noticelist="international" />
        </div>
        <div v-else class="tab-pane fade" id="panel1" role="tabpanel">
           <!-- <notice-list :noticelist="international" /> --><br><br>
           <div v-for="category,category_name in outreach" v-if="category_name=='Colleges/Institutes/Universities (Abroad)'">
            <h2 style="margin-left: 15%;">{{category_name}}</h2>
            <table class="table table-bordered tbl" style="width: 70%;margin-left: 15%;">
              <thead>
                <td>Sl. No.</td>
                <td>Name of {{category_name}}</td>
                <td>Details of MoU</td>
              </thead>
              <tr v-for="(row,index) in category">
                <td>{{index+1}}</td>
                <td style="text-align: center;"><div class="text-center"><img :src="row.icon" width="100px" height="100px"/></div>{{ row.name }}</td>
                <td><a :href="row.mou" >Click Here</a></td>
              </tr> 
            </table>
            <br/>
          </div>
        </div>

        <div v-if="$route.params.tab === 'national'" class="tab-pane in show active fade" id="panel3" role="tabpanel">
          <notice-list :noticelist="national" />
        </div>
        <div v-else class="tab-pane fade show active" id="panel3" role="tabpanel">
          <!-- <notice-list :noticelist="national" /> --><br><br>
          <div v-for="category,category_name in outreach" v-if="category_name=='Colleges/Institutes/Universities (India)'">
            <h2 style="margin-left: 15%;">{{category_name}}</h2>
            <table class="table table-bordered tbl" style="width: 70%;margin-left: 15%;">
              <thead>
                <td>Sl. No.</td>
                <td>Name of {{category_name}}</td>
                <td>Details of MoU</td>
              </thead>
              <tr v-for="(row,index) in category">
                <td>{{index+1}}</td>
                <td style="text-align: center;"><div class="text-center"><img :src="row.icon" width="100px" height="100px"/></div>{{ row.name }}</td>
                <td><a :href="row.mou">Click Here</a></td>
              </tr> 
            </table>
            <br/>
          </div>
          <div v-for="category,category_name in outreach" v-if="category_name=='Industries/Organizations (India)'">
            <h2 style="margin-left: 15%;">{{category_name}}</h2>
            <table class="table table-bordered tbl" style="width: 70%;margin-left: 15%;">
              <thead>
                <td>Sl. No.</td>
                <td>Name of {{category_name}}</td>
                <td>Details of MoU</td>
              </thead>
              <tr v-for="(row,index) in category">
                <td>{{index+1}}</td>
                <td style="text-align: center;"><div class="text-center"><img :src="row.icon" width="100px" height="100px"/></div>{{ row.name }}</td>
                <td><a :href="row.mou">Click Here</a></td>
              </tr> 
            </table>
            <br/>
          </div>
        </div>
        <div v-for="category,category_name in outreach" v-if="category_name=='Research Institutions (India)'">
            <h2 style="margin-left: 15%;">{{category_name}}</h2>
            <table class="table table-bordered tbl" style="width: 70%;margin-left: 15%;">
              <thead>
                <td>Sl. No.</td>
                <td>Name of {{category_name}}</td>
                <td>Details of MoU</td>
              </thead>
              <tr v-for="(row,index) in category">
                <td>{{index+1}}</td>
                <td style="text-align: center;"><div class="text-center"><img :src="row.icon" width="100px" height="100px"/></div>{{ row.name }}</td>
                <td><a :href="row.mou">Click Here</a></td>
              </tr> 
            </table>
            <br/>
          </div>
        </div>

      </div>
    </card>
  </links-page>
</template>

<script>
import NoticeList from '@/components/NoticeList'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import axios from 'axios'
import { genBackendURL } from '@/common.js'

export default {
  name: 'Collaboration',
  data() {
    return {
      national: [],
      international: [],
      outreach: {}
    }
  },
  created () {
    axios.get(genBackendURL('activities/collaboration'))
         .then(response => {
          let collaborations = response.data.collaborations
          console.log(collaborations)
          this.national = collaborations.National
          this.international = collaborations.International
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
    axios.get(genBackendURL("activities/outreach"))
         .then(response => {
           this.outreach = response.data.outreach
           console.log(this.outreach)
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
  components: {
    NoticeList,
    LinksPage,
    Card
  }
}
</script>
<style>
  .card-body {
    padding-left: 0px;
    padding-right: 0px;
    padding-bottom: 0px
  }
  .nav-tabs {
    padding: 0px;
  }
  td{
    border: 1px solid #cad;
  }
  tr:hover{
    background: #C7ECF5;
  }
</style>
