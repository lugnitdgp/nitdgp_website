<template>
  <links-page>
    <card title="Public Grievance Cell">
      <ul class="list-group list-gr">
        <li v-for="link in links">
          <a v-if="link.file" class="list-group-item" :href="link.file">
            <span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ link.date.substring(0,10) }} </span>&nbsp;{{ link.title }}
            </a>
          <a v-else class="list-group-item" :href="link.url">
            <span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ link.date.substring(0,10) }} </span>&nbsp;{{ link.title }}
          </a>
        </li>
      </ul>
    </card>
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
