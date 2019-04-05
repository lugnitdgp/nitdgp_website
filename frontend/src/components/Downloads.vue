<template>
  <links-page>
    <card title="Downloads">
      <ul class="list-group list-gr">
        <li v-for="file in files">
          <a class="list-group-item" target="new" :href="file.file">
            {{file.title}}
          </a>
        </li>
      </ul>
      <div class="btn-group">
        <button v-if="next != ''" class="nit-btn"
          @click="changePage(next)">
          Next
        </button>
        <button v-if="prev != ''" class="nit-btn"
          @click="changePage(prev)">
          Previous
        </button>
      </div>
    </card>
  </links-page>
</template>

<script>
import Card from "@/components/Card"
import LinksPage from "@/components/LinksPage"
import axios from 'axios'
import { genBackendURL } from '@/common.js'

export default {
  name: "Downloads",
  data () {
    return {
      files: [],
      next: '',
      prev: ''
    }
  },
  created () {
    this.changePage(genBackendURL('dashboard/downloads'))
    this.$emit('hideloader', true)
  },
  methods:{
    changePage: function(url){
      axios.get(url)
           .then(response => {
             this.files = response.data.results
             if (response.data.next != null)
               this.next = response.data.next
             else
               this.next = ''
             if (response.data.previous != null)
               this.prev = response.data.previous
             else
               this.prev = ''
           })
           .catch(e => {
             console.log("Axios(GET[information]): Error: " + e)
           })
    }
  },
  components: {
    Card,
    LinksPage
  }
}
</script>

