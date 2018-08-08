<template>
  <links-page>
    <card title="Notices">
      <ul class="nav nav-tabs nav-justified not-tab">
        <li class="nav-item">
          <a class="nav-link" data-toggle="tab" href="#panel1" role="tab">Academic</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" data-toggle="tab" href="#panel2" role="tab">Student</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" data-toggle="tab" href="#panel3" role="tab">General</a>
        </li>
      </ul>
      <div class="tab-content card">
        <div class="tab-pane fade notice-wrap" id="panel1" role="tabpanel">
          <notice-list idn="1" :noticelist="academic" />
        </div>
        <div class="tab-pane in show active fade notice-wrap" id="panel2" role="tabpanel">
          <notice-list :noticelist="student" />
        </div>
        <div class="tab-pane fade notice-wrap" id="panel3" role="tabpanel">
      	  <notice-list :noticelist="general" />
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
  name: 'Notices',
  data() {
    return {
      academic: [],
      student: [],
      general: []
    }
  },
  created () {
    axios.get(genBackendURL('academics/notices'))
         .then(response => {
           console.log(response)
           let notices = response.data.notices
           this.student.push(...notices.Student)
           this.academic = notices.Academic
           this.general = notices.General
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
</style>
