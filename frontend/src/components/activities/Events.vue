<template>
  <links-page>
    <card title="Seminars and Events">
      <ul class="list-group list-gr">
        <li v-for="event in events">
        	
          <a v-if="event.file" class="list-group-item" :href="event.file"><span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ event.date }} </span>&nbsp;{{ event.title }}</a>

          <a v-else="event.url" class="list-group-item" :href="event.url"><span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ event.date }} </span>&nbsp;{{ event.title }}</a>
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
