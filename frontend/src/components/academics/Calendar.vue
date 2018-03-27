<template>
  <links-page>
    <card title="Academic Calendars">
      <ul>
        <li v-for="calendar in calendars">
          <a :href="calendar.file">
            Academic Calendar for the year {{ calendar.year }}
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
import {genBackendURL} from '@/common.js'

export default {
  name: "Calendar",
  data () {
    return {
      calendars: {}
    }
  },
  created () {
    axios.get(genBackendURL("academics/calendar"))
         .then(response => {
           this.calendars = response.data.results
           console.log(response.data)
           this.$emit('hideloader', true)
         })
         .catch(e => {
           this.errors.push(e)
           console.log("Axios(GET[admission]): Error: " + e)
         })
  },
  components: {
    LinksPage,
    Card
  }
}
</script>
