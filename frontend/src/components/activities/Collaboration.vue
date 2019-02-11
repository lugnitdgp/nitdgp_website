<template>
  <links-page>
    <card title="Collaboration">
      <ul class="nav nav-tabs nav-justified not-tab">
        <li class="nav-item">
          <a class="nav-link active show" data-toggle="tab" href="#panel1" role="tab">National Collaboration</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" data-toggle="tab" href="#panel2" role="tab">International Collaboration</a>
        </li>
      </ul>
      <div class="tab-content card">
        <div class="tab-pane fade" id="panel2" role="tabpanel">
           <!-- <notice-list :noticelist="international" /> --><br><br>
           <div v-for="category,category_name in outreach" v-if="category_name=='Colleges/Institutes/Universities (Abroad)'">
            <div style="background-color: #001333;color: #fff;padding: 10px;text-align: center;">{{category_name}}</div>
            <table class="table table-bordered tbl">
              <thead>
                <td style="color: #000;font-weight: bold;">Sl. No.</td>
                <td style="color: #000;font-weight: bold;">Name of {{category_name}}</td>
                <td style="color: #000;font-weight: bold;">Details of MoU</td>
              </thead>
              <tr v-for="(row,index) in category">
                <td>{{index+1}}</td>
                <td style="text-align: center;"><div class="text-center"><img :src="row.icon" width="100px" height="100px"/></div><p style="color: #000;font-weight: bold;">{{ row.name }}</p></td>
                <td><a :href="row.mou" >Click Here</a></td>
              </tr> 
            </table>
            <br/>
          </div>
        </div>
        <div class="tab-pane fade show active" id="panel1" role="tabpanel">
          <!-- <notice-list :noticelist="national" /> --><br><br>
          <div v-for="category,category_name in outreach" v-if="category_name=='Colleges/Institutes/Universities (India)'">
            <div style="background-color: #001333;color: #fff;padding: 10px;text-align: center;">{{category_name}}</div>
            <table class="table table-bordered tbl">
              <thead>
                <td style="color: #000;font-weight: bold;">Sl. No.</td>
                <td style="color: #000;font-weight: bold;">Name of {{category_name}}</td>
                <td style="color: #000;font-weight: bold;">Details of MoU</td>
              </thead>
              <tr v-for="(row,index) in category">
                <td>{{index+1}}</td>
                <td style="text-align: center;"><div class="text-center"><img :src="row.icon" width="100px" height="100px"/></div><p style="color: #000;font-weight: bold;">{{ row.name }}</p></td>
                <td><a :href="row.mou">Click Here</a></td>
              </tr> 
            </table>
            <br/>
          </div>
          <div v-for="category,category_name in outreach" v-if="category_name=='Industries/Organizations (India)'">
            <div style="background-color: #001333;color: #fff;padding: 10px;text-align: center;">{{category_name}}</div>
            <table class="table table-bordered tbl">
              <thead>
                <td>Sl. No.</td>
                <td style="color: #000;font-weight: bold;">Name of {{category_name}}</td>
                <td>Details of MoU</td>
              </thead>
              <tr v-for="(row,index) in category">
                <td>{{index+1}}</td>
                <td style="text-align: center;"><div class="text-center"><img :src="row.icon" width="100px" height="100px"/></div><p style="color: #000;font-weight: bold;">{{ row.name }}</p></td>
                <td><a :href="row.mou">Click Here</a></td>
              </tr> 
            </table>
            <br/>
          </div>
        <div v-for="category,category_name in outreach" v-if="category_name=='Research Institutions (India)'">
            <div style="background-color: #001333;color: #fff;padding: 10px;text-align: center;">{{category_name}}</div>
            <table class="table table-bordered tbl">
              <thead>
                <td>Sl. No.</td>
                <td style="color: #000;font-weight: bold;">Name of {{category_name}}</td>
                <td>Details of MoU</td>
              </thead>
              <tr v-for="(row,index) in category">
                <td>{{index+1}}</td>
                <td style="text-align: center;"><div class="text-center"><img :src="row.icon" width="100px" height="100px"/></div><p style="color: #000;font-weight: bold;">{{ row.name }}</p></td>
                <td><a :href="row.mou">Click Here</a></td>
              </tr> 
            </table>
            <br/>
          </div>
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
    /*axios.get(genBackendURL('activities/collaboration'))
         .then(response => {
          let collaborations = response.data.collaborations
          console.log(collaborations)
          this.national = collaborations.National
          this.international = collaborations.International
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })*/
    axios.get(genBackendURL("activities/outreach"))
         .then(response => {
           this.outreach = response.data.outreach
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
<style scoped>
  .card-body {
    padding-left: 0px;
    padding-right: 0px;
    padding-bottom: 0px
  }
  .nav-tabs {
    padding: 0px;
  }
  td{
    border: 1px solid #001333;
  }
</style>
