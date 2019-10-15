<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text">Student Activity Centre Introduction</a>
      <div class="card-body">
	<div>
	  <div align="justify">
	    <font v-html="sacdata[0].about"></font>
	  </div>
	</div>
      </div>
    </div>
    <div class="card">
      <a class="card-header white-text">Vision &amp; Mission</a>
      <div class="card-body">
	<div>
	  <div align="justify">
	    <strong>Vision</strong><br>
	    <font v-html="sacdata[0].vision"></font><br><br>
	    <strong>Mission</strong><br>
	    <font v-html="sacdata[0].mission"></font>
	  </div>
	</div>
      </div>
    </div>
    <div class="card">
      <a class="card-header white-text">Programme offered</a>
      <div class="card-body">
	<font v-html="sacdata[0].program_offered"></font>
      </div>
    </div>
    <div class="card">
      <a class="card-header white-text">Other Activities</a>
      <div class="card-body">
	<font v-html="sacdata[0].other_activities"></font>
      </div>
    </div>
    <div class="card">
      <a class="card-header white-text">Facilities in the Department</a>
      <div class="card-body">
	<font v-html="sacdata[0].facility"></font>
      </div>
    </div>
    <div class="card">
      <a class="card-header white-text">Achievements</a>
      <div class="card-body">
	<a :href="sacdata[0].ach_url">Achievements in Sports &amp; Games of NIT Durgapur since March 2007</a><br>
	<a :href="sacdata[0].rec_url">Record of Games & Sports Activities of NIT Durgapur since March 2007</a>
		
      </div>
    </div>
    <div class="card">
      <a class="card-header white-text">Contact</a>
      <div class="card-body">
		<img style="float: left;" :src="sacdata[0].image" alt="sac head">
		  <font v-html="sacdata[0].contact_us" style="float: left;"></font>
	
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import { genBackendURL } from '@/common.js'
export default {
  name: 'Sac',
  data () {
    return {
       sacdata:[],
    }
  },
  created () {
  	axios.get(genBackendURL('facilities/sac'))
              .then(response => {
                  this.sacdata = response.data.results
                  console.log(this.sacdata[0].about)
                  })
              .catch(e => {
                  console.log("Error:", e)
              })
    this.$emit('hideloader', true)
  }
}
</script>
