<template>
  <links-page>
    <card title="Examination">
      <ul class="list-group list-gr">
        <li v-for="link in exams">
          <a class="list-group-item" :href="link.file" target="new">
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
  name: 'Examinations',
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
