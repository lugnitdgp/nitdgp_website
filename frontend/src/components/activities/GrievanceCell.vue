<template>
  <links-page>
    <card title="Grievance Cell">
      <ul class="list-group list-gr">
        <li v-for="link in links">
          <a class="list-group-item" v-if="link.file" :href="link.file" target="new">
            {{ link.title }}
          </a>
          <a class="list-group-item" v-if="link.url" :href="link.url" target="new">
            {{ link.title }}
          </a>
        </li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import axios from 'axios'
import { backURL, genBackendURL } from '@/common.js'

export default {
  name: 'Research',
  data () {
    return {
      links: [],
      backURL: backURL
    }
  },
  created () {
    axios.get(genBackendURL('activities/grievance-cell'))
         .then(response => {
           this.links = this.links.concat(response.data.results)
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
