<template>
  <links-page>
    <card title="Seminars and Events">
      <ul class="list-group list-gr">
        <li v-for="event in events">
          <a class="list-group-item" :href="event.file">{{ event.title }}</a>
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
  name: "Events",
  data () {
    return {
      events: {}
    }
  },
  created () {
    axios.get(genBackendURL("activities/seminars-and-events"))
         .then(response => {
           this.events = response.data.results
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
