<template>
  <links-page>
    <card title="Semester Question Papers">
      <ul class="list-group list-gr">
        <li v-for="qset in qsets">
          <a class="list-group-item" target="new" :href="qset.file">{{ qset.title }}</a>
        </li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import axios from 'axios'
import Card from "@/components/Card"
import LinksPage from "@/components/LinksPage"
import { genBackendURL } from '@/common.js'

export default {
  name: "Question",
  data () {
    return {
       qsets:{},
    }
  },
  created () {
    axios.get(genBackendURL('facilities/question'))
              .then(response => {
                  this.qsets = response.data.results
                 
                  })
              .catch(e => {
                  console.log("Error:", e)
              })
    this.$emit('hideloader', true)
  },
  components: {
    Card,
    LinksPage
  }
}
</script>
