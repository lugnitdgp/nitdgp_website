<template>
  <links-page>
    <card title="Achievements">
      <ul class="list-group list-gr">
        <li v-for="achievement in achievements">
          <a class="list-group-item" :href="achievement.file">{{ achievement.title }}</a>
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
  name: "Achievements",
  data () {
    return {
      achievements: {}
    }
  },
  created () {
    axios.get(genBackendURL("activities/achievements"))
         .then(response => {
           this.achievements = response.data.results
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
