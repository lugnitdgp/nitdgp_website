<template>
  <links-page>
    <card title="Convocation and Special Events">
      <ul>
        <li v-for="file in convocations">
          <a :href="file.file">{{ file.title }}</a>
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
  name: "Convocations",
  data () {
    return {
      convocations: {}
    }
  },
  created () {
    axios.get(genBackendURL("academics/regulations"))
         .then(response => {
           this.convocations = response.data.results
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
