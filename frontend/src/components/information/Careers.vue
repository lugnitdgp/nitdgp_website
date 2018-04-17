<template>
  <links-page>
    <card title="Careers">
      <ul class="list-group list-gr">
        <li v-for="career in careers">
          <a class="list-group-item" :href="career.file">{{ career.title }}</a>
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
  name: "Careers",
  data () {
    return {
      careers: {}
    }
  },
  created () {
    axios.get(genBackendURL("information/careers"))
         .then(response => {
           this.careers = response.data.results
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
