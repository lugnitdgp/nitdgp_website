<template>
  <links-page>
    <card title="Public Grievance Cell">
      <ul class="list-group list-gr">
        <li v-for="link in links">
          <a v-if="link.file" class="list-group-item" :href="link.file" target="new">
            {{ link.title }}
            </a>
          <a v-else class="list-group-item" :href="link.link" target="new">
            {{ link.title }}
          </a>
        </li>
      </ul>
    </card>
    <div class="card">
      <a class="card-header white-text">Staff Grievance Officer </a>
      <div class="card-body">
	<font>
	  Prof. Vijay Kumar Dwivedi<br/>
    Department of Civil Engineering,<br/>
    National Institute of Technology,<br/>
    Durgapur, West Bengal-713209.<br/>
    Mobile: +91-9434788097<br/>
    Email: sgo@admin.nitdgp.ac.in 
	</font>
      </div>
    </div>
  </links-page>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import { genBackendURL } from '@/common.js'

export default {
  name: "Pgcell",
  data () {
    return {
      links: {}
    }
  },
  created () {
    axios.get(genBackendURL("information/publicgrievance"))
         .then(response => {
           this.links = response.data.results
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
  components: {
    LinksPage,
    Card
  }
}
</script>
