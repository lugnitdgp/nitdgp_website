<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text">Quick Links</a>
      <div class="card-body">
        <div class="row">
          <div class="col">
            <h4>Admissions</h4>
            <ul>
              <li v-for="link in links['Admission']">
                <a v-if="link.link" :href="link.link">{{link.title}}</a>
                <a v-else :href="link.file">{{link.title}}</a>
              </li>
            </ul>
          </div>
          <div class="col">
            <h4>General</h4>
            <ul>
              <li v-for="link in links['General']">
                <a v-if="link.link" :href="link.link">{{link.title}}</a>
                <a v-else :href="link.file">{{link.title}}</a>
              </li>
            </ul>
          </div>
          <div class="col">
            <h4>National Portal</h4>
            <ul>
              <li v-for="link in links['National Portal']">
                <a v-if="link.link" :href="link.link">{{link.title}}</a>
                <a v-else :href="link.file">{{link.title}}</a>
              </li>
            </ul>
          </div>
          <div class="col">
            <h4>Social Media</h4>
            <ul>
              <li v-for="link in links['Social Media']">
                <a v-if="link.link" :href="link.link">{{link.title}}</a>
                <a v-else :href="link.file">{{link.title}}</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import CardTestimonial from '@/components/CardTestimonial'
import { range, genBackendURL } from '@/common.js'

export default {
  name: "QuickLinks",
  data () {
    return {
      links: {}
    }
  },
  created () {
    axios.get(genBackendURL("dashboard/quick-links"))
         .then(response => {
           this.links = response.data.groups
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
  components: {
    LinksPage,
    Card,
    CardTestimonial
  }
}
</script>

<style scoped>
ul {
  text-decoration: none;
}
</style>