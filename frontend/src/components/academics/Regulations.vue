<template>
  <links-page>
    <card title="Academic Regulations" class="list-group list-grations">
      <ul class="list-group list-gr">
        <li v-for="regulation in regulations">
          <a class="list-group-item" :href="regulation.file" target="new">
            {{ regulation.title }}
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
  name: "Regulations",
  data () {
    return {
      regulations: {}
    }
  },
  created () {
    axios.get(genBackendURL("academics/regulations"))
         .then(response => {
           this.regulations = response.data.results
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
