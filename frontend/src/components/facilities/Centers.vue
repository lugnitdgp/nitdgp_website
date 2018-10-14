<template>
  <links-page>
    <card title="Centers">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row">
            <card-testimonial v-for="(center, i) in centers" :key="i"
              class="card-centers"
              :name="center.title"
              :image="center.image">
              <a :href="center.link">
                <span v-html="center.description"></span>
              </a>
            </card-testimonial>
          </div>
        </div>
      </div>
    </card>
  </links-page>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import CardTestimonial from '@/components/CardTestimonial'
import { range, genBackendURL } from '@/common.js'

export default {
  name: 'Centers',
  data () {
    return {
      centers: {}
    }
  },
  created () {
    axios.get(genBackendURL("facilities/centers"))
         .then(response => {
           this.centers = response.data.centers
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

<style>
  .card-centers {
    min-width: 230px !important;
    min-height: 200px !important;
    max-width: 300px !important;
    max-height: 500px !important;
    padding: 10px !important;
  }
</style>
