<template>
  <links-page>
    <card v-for="(links, title, i) in categories" :title="title" :key="i">
      <ul class="list-group list-gr">
        <li v-for="(link, j) in links" :key="j">
          <a v-if="typeof link.file != 'undefined'" class="list-group-item" target="new" :href="link.file">
            {{ link.title }}
          </a>
          <a v-if="typeof link.url != 'undefined'" class="list-group-item" target="new" :href="link.url">
            {{ link.title }}
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
  name: "QuickLinks",
  data () {
    return {
      categories: {}
    }
  },
  created: function () {
    axios.get(genBackendURL('dashboard/quick-links'))
         .then(response => {
           this.categories = response.data.groups
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log("Axios(GET[admission]): Error: " + e)
         })
  },
  components: {
    LinksPage,
    Card
  }
}
</script>
