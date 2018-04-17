<template>
  <links-page>
    <card title="Academic Documents">
      <div v-for="(links, doctype) in docs">
        <h3>{{ doctype }}</h3>
        <ul class="list-group list-gr">
          <li v-for="link in links">
            <a class="list-group-item" :href="backURL + link.filename" target="new">
              {{ link.title }}
            </a>
          </li>
        </ul>
      </div>
    </card>
  </links-page>
</template>

<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import axios from 'axios'
import { backURL, genBackendURL } from '@/common.js'

export default {
  name: 'Documents',
  data () {
    return {
      docs: {},
      backURL: backURL
    }
  },
  created () {
    axios.get(genBackendURL('academics/document'))
         .then(response => {
           this.docs = response.data.documents
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
