<template>
  <links-page>
    <card title="Archives">
      <collapse-list>
        <card-collapse  title="Academic Notices">
          <div class="card-text">
            <ul class="list-group list-gr">
              <li v-for="list in academicnotices">
                <a class="list-group-item" :href="list.file"><span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ list.date }}</span>&nbsp;&nbsp;&nbsp; {{ list.title }}</a>
              </li>                
            </ul>
          </div>
        </card-collapse>
        <card-collapse  title="General Notices">
          <div class="card-text">
            <ul class="list-group list-gr">
              <li v-for="list in generalnotices">
                <a class="list-group-item" :href="list.file"><span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ list.date }}</span>&nbsp;&nbsp;&nbsp;{{ list.title }}</a>
              </li>                
            </ul>
          </div>
        </card-collapse>
        <card-collapse  title="Student Notices">
          <div class="card-text">
            <ul class="list-group list-gr">
              <li v-for="list in studentnotices">
                <a class="list-group-item" :href="list.file"><span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ list.date }}</span>&nbsp;&nbsp;&nbsp;{{ list.title }}</a>
              </li>                
            </ul>
          </div>
        </card-collapse>
        <card-collapse  title="Careers">
          <div class="card-text">
            <ul class="list-group list-gr">
              <li v-for="list in careers">
                <a class="list-group-item" :href="list.file"><span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ list.date }}</span>&nbsp;&nbsp;&nbsp;{{ list.title }}</a>
              </li>                
            </ul>
          </div>
        </card-collapse>
        <card-collapse  title="Tenders">
          <div class="card-text">
            <ul class="list-group list-gr">
              <li v-for="list in tenders">
                <a class="list-group-item" :href="list.file"><span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ list.date }}</span>&nbsp;&nbsp;&nbsp;{{ list.title }}</a>
              </li>                
            </ul>
          </div>
        </card-collapse>
        <card-collapse  title="Seminar and Events">
          <div class="card-text">
            <ul class="list-group list-gr">
              <li v-for="list in events">
                <a class="list-group-item" :href="list.file"><span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ list.date }}</span>&nbsp;&nbsp;&nbsp;{{ list.title }}</a>
              </li>                
            </ul>
          </div>
        </card-collapse>
      </collapse-list>
    </card>
  </links-page>
</template>
<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import CollapseList from '@/components/CollapseList'
import CardCollapse from '@/components/CardCollapse'
import axios from 'axios'
import { genBackendURL } from '@/common.js'


export default {
  name: 'Archives',
  data () {
    return {
      academicnotices: [],
      generalnotices: [],
      studentnotices: [],
      careers: [],
      tenders: [],
      events: [],
    }
  },
  created () {
    axios.get(genBackendURL("/archives/"))
     .then(response => {
           let archives = response.data
           this.careers = archives.career
           this.academicnotices = archives.academic_notice
           this.generalnotices = archives.general_notice
           this.studentnotices = archives.student_notice
           this.tenders = archives.tender
           this.events = archives.event
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })    
  },
  components: {
    LinksPage,
    CollapseList,
    CardCollapse,
    Card
  }
}
</script>
<style >
  .list-gr .contact-col{
    min-width: 100%;
    max-width: 100%;
    padding-bottom: 15px;
    color: #fff;
  }
  .col {
    -ms-flex-preferred-size: 0;
    flex-basis: 0;
    -ms-flex-positive: 1;
    flex-grow: 1;
    max-width: 100%;
}
  @media screen and (max-width: 1200px){
    .list-gr .contact-col{
      min-width: 100%;
      max-width: 100%;
    }
  }
  @media screen and (max-width: 800px){
    .list-gr .contact-col{
      min-width: 100%;
      max-width: 100%;
    }
  }
</style>