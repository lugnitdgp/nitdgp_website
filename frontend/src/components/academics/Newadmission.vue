<template>
	<div class="l1 page-type-links">
		<!-- CONTENT -->
		<div class="card">
		  <a class="card-header white-text">Admission 2020</a>
		  <div class="card-body">
		      <div class="card-text">
		        <ul class="list-group list-gr">
	              <li v-for="newad in newadmission">
	              	<a v-if="newad.file" class="list-group-item" target="new" :href="newad.file">
	                  {{ newad.title }}
	                </a>
	                <a v-else class="list-group-item" target="new" :href="newad.link">
	                  {{ newad.title }}
	                </a>	                
	              </li>
	            </ul>
		      </div>
		  </div>
		</div>
	</div>
</template>
<script>
import axios from 'axios'
import { genBackendURL } from '@/common.js'
export default {
  name: 'Newadmission',
  data(){
  	return{
  		newadmission:{}
  	}
  },
  created () {
    axios.get(genBackendURL("academics/newadmission/"))
        .then(response => {
           this.newadmission = response.data.results
           this.$emit('hideloader', true)
        })
        .catch(e => {
           console.log(e)
        })
  }
}
</script>
