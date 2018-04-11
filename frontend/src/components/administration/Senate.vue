<template>
  <links-page>
    <card title="Senate">
      <ul>
        <li v-for="meeting in meetings">
          <a :href="meeting.file">{{ meeting.title }}</a>
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
  name: "Senate",
  data () {
    return {
      meetings: {}
    }
  },
  created () {
    axios.get(genBackendURL("administration/senate"))
         .then(response => {
           this.meetings = response.data.results
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
