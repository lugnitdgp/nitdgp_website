<template>
  <links-page>
    <card title="Notices">
      <ul class="nav nav-tabs nav-justified not-tab">
        <li class="nav-item">
          <a v-if="$route.params.tab === 'general'" class="nav-link active" data-toggle="tab" href="#panel3" role="tab">General</a>
          <a v-else class="nav-link" data-toggle="tab" href="#panel3" role="tab">General</a>
        </li>
        <li class="nav-item">
          <a v-if="$route.params.tab === 'academic'" class="nav-link active" data-toggle="tab" href="#panel1" role="tab">Academic</a>
          <a v-else class="nav-link" data-toggle="tab" href="#panel1" role="tab">Academic</a>
        </li>
        <li class="nav-item">
          <a v-if="$route.params.tab === 'student'" class="nav-link active" data-toggle="tab" href="#panel2" role="tab">Student</a>
          <a v-else class="nav-link" data-toggle="tab" href="#panel2" role="tab">Student</a>
        </li>
      </ul>
      <div class="tab-content card">
        <div v-if="$route.params.tab === 'academic'" class="tab-pane in show active fade" id="panel1" role="tabpanel">
          <notice-list :noticelist="academic" />
        </div>
        <div class="tab-pane fade" id="panel1" role="tabpanel">
          <notice-list :noticelist="academic" />
        </div>

        <div v-if="$route.params.tab === 'student'" class="tab-pane in show active fade" id="panel2" role="tabpanel">
          <notice-list :noticelist="student" />
        </div>
        <div class="tab-pane fade" id="panel2" role="tabpanel">
          <notice-list :noticelist="student" />
        </div>

        <div v-if="$route.params.tab === 'general'" class="tab-pane in show active fade" id="panel3" role="tabpanel">
      	  <notice-list :noticelist="general" />
        </div>
        <div class="tab-pane fade" id="panel3" role="tabpanel">
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
