<template>
  <links-page>
    <card title="Careers">
      <ul class="list-group list-gr">
        <li v-for="career, key in careers">
          <a class="list-group-item" :href="career.file"><span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ career.date }} </span>&nbsp;{{ career.title }}</a>
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
           this.careers = response.data.careers
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
