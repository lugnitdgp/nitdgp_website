<template>
  <links-page>
    <card title="Deans">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row">
            <div class="col" v-for="dean in deans">
              <card-testimonial :image="dean.image" :name="dean.name"
                :desig="dean.role + ' ' + dean.designation">
                <i class="fa fa-envelope"></i><br>
                <strong>{{ dean.email }}</strong><br>
                <i class="fa fa-address-book"></i><br>
                <strong>+91-343-{{ dean.phone }}</strong></br>
                <strong>+91-{{ dean.alternate_phone }}</strong></br>
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
import { genBackendURL } from '@/common.js'

export default {
  name: "Deans",
  data () {
    return {
      deans: {}
    }
  },
  created () {
    axios.get(genBackendURL("administration/deans"))
         .then(response => {
           this.deans = response.data.results
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
