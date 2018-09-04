<template>
  <links-page>
    <card title="Centers of Excellence">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row">
            <div class="col" v-for="center in centers">
              <card-testimonial :name="center.title" :image="center.image">
                <a :href="center.link">
                  <span v-html="center.description"></span>
                </a>
              </card-testimonial>
            </div>
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
  name: 'Coe',
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
