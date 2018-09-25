<template>
  <links-page>
    <card title="Student Cell">
      <ul class="list-group list-gr">
        <li v-for="link in links">
          <a v-if="link.file" class="list-group-item" :href="link.file">
            {{ link.title }}
            </a>
          <a v-else class="list-group-item" :href="link.url">
            {{ link.title }}
          </a>
        </li>
      </ul>
    </card>
    <div class="card">
      <a class="card-header white-text">Liason Officer, SC-ST Cell, NIT, Durgapur </a>
      <div class="card-body">
	<font>
	    Dr. Apurba Layek<br/>
        Associate Professor of Mechanical Enginnering<br/>
        NIT, Durgapur, West Bengal, India.<br/>
        Mobile No.+91-94347-88058<br/>
        e-mail : apurba_layek@yahoo.co.in
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
    axios.get(genBackendURL("activities/grievance-cell"))
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
