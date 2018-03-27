<template>
  <links-page>
    <card v-for="(content, title) in details" :title="prettify(title)" :key="title.id">
      <div v-html="content">
      </div>
    </card>
    <card title="E-Resources">
      <ul>
        <li v-for="eres in eresources">
          <a :href="eres.url">
            {{ eres.title }}
          </a>
        </li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import Card from "@/components/Card"
import LinksPage from "@/components/LinksPage"
import axios from 'axios'
import { genBackendURL, prettify } from '@/common.js'

export default {
  name: "Library",
  data () {
    return {
      details: {},
      eresources: []
    }
  },
  created () {
    axios.get(genBackendURL('facilities/library'))
         .then(response => {
           this.details = response.data.results[0]
           if (response.data.results.length > 1)
             console.log("Error: More than one Library found")
         })
         .catch(e => {
           this.errors.push(e)
           console.log(errors)
         })
    axios.get(genBackendURL('facilities/eresource'))
         .then(response => {
           this.eresources = response.data.results
         })
         .catch(e => {
           this.errors.push(e)
           console.log(errors)
         })
  },
  methods: {
    prettify
  },
  components: {
    Card,
    LinksPage
  }
}
</script>
