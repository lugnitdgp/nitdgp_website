<template>
  <div class="l1 page-type-links notices">
    <div class="card">
      <a class="card-header white-text">Notices</a>
      <div class="card-body">
      	<!-- Nav tabs -->
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
      	<!-- Tab panels -->
      	<div class="tab-content card">
      	  <notice-list idn="1" :noticelist="academic">
          </notice-list>
      	  <notice-list class="in show active" :noticelist="student" idn="2"></notice-list>
      	  <notice-list :noticelist="general" idn="3"></notice-list>
      	</div>
      </div>
    </div>
  </div>
</template>

<script>
import NoticeList from '@/components/NoticeList'
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
           if ("8e23a092684f4c3189728772de4bf244" in notices) {
             // For backward compatibility
             this.student.push(...notices["8e23a092684f4c3189728772de4bf244"])
           }
           this.academic = notices.Academic
           this.general = notices.General
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
  components: {
    NoticeList
  }
}
</script>
<style>
  .notices .card-body{
    padding-left: 0px;
    padding-right: 0px;
    padding-bottom: 0px
  }
</style>