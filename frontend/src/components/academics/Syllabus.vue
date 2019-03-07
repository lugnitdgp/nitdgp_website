<template>
  <links-page>
    <card title="Curriculum and Syllabus">
      <ul class="list-group list-gr">
        <li v-for="curriculmn in curriculmns">
          <a class="list-group-item" target="new" :href="curriculmn.file">
            {{ curriculmn.title }}
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
  name: "Curriculmn",
  data () {
    return {
      curriculmns: {}
    }
  },
  created () {
    axios.get(genBackendURL('academics/curriculum'))
         .then(response => {
           this.curriculmns = response.data.results
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
         this.$emit('hideloader', true)
  },
  components: {
    LinksPage,
    Card
  }
}
</script>
