<template>
  <links-page>
    <card title="Examination">
      <ul>
        <li v-for="link in exams">
          <a :href="link.filename" target="new">
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
import { genBackendURL } from '@/common.js'

export default {
  name: 'Exams',
  data () {
    return {
      exams: {}
    }
  },
  created () {
    axios.get(genBackendURL('academics/examination'))
         .then(response => {
           this.exams = response.data.results
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
