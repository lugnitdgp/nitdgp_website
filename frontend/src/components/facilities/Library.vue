<template>
  <links-page>
    <card v-for="(content, title) in details" :title="prettify(title)" :key="title.id">
      <div v-html="content">
      </div>
    </card>
    <card v-if="resources" title="E-Resources">
      <div class="row">
        <div class="col">
        <h4>Text Resources</h4>
          <ul class="list-group list-gr">
            <li v-for="resource in resources['Text Resource']">
              <a class="list-group-item" :href="resource.url">
                {{ resource.title }}
              </a>
            </li>
          </ul>
        </div>
        <div class="col">
        <h4>E Resources</h4>
          <ul class="list-group list-gr">
            <li v-for="resource in resources['E Resource']">
              <a class="list-group-item" :href="resource.url">
                {{ resource.title }}
              </a>
            </li>
          </ul>
        </div>
      </div>
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
      resources: []
    }
  },
  created () {
    let f = false
    axios.get(genBackendURL('facilities/library'))
         .then(response => {
           this.details = response.data.results[0]
           if (response.data.results.length > 1)
             console.log("Error: More than one Library found")
           if (f)
             this.$emit('hideloader', true)
           f = true
         })
         .catch(e => {
           console.log(e)
         })
    axios.get(genBackendURL('facilities/resource'))
         .then(response => {
           this.resources = response.data.resources
           if (f)
             this.$emit('hideloader', true)
           f = true
         })
         .catch(e => {
           console.log(e)
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
