<template>
  <links-page>
    <card title="Head Of Departments">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row">
            <card-testimonial v-for="(hod, i) in hods" :key="i"
              class="black-text"
              :image="hod.image"
              :name="hod.name"
              :id="hod.id"
              :desig="hod.department">
              <i class="fa fa-envelope"></i><br>
              <strong>{{ hod.email }}</strong><br>
              <i class="fa fa-address-book"></i><br>
              <strong>+91-{{ hod.mobile }}</strong></br>
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
  name: "Hods",
  data () {
    return {
      hods: {}
    }
  },
  created () {
    axios.get(genBackendURL("administration/hod"))
         .then(response => {
           this.hods = response.data.results
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
