<template>
  <links-page>
    <card title="Academic Regulations">
      <ul>
        <li v-for="regulation in regulations">
          <a :href="regulation.file">{{ regulation.title }}</a>
        </li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import {genBackendURL} from '@/common.js'

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
           console.log(response.data)
           this.$emit('hideloader', true)
         })
         .catch(e => {
           this.errors.push(e)
           console.log(e)
         })
  },
  components: {
    LinksPage,
    Card
  }
}
</script>
