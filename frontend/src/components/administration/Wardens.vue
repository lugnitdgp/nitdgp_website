<template>
  <links-page>
    <card title="Wardens">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row">
            <div style="min-width:100%;"><h3>Chief Warden</h3></div>
            <div class="col black-text" v-for="warden in wardens.chief_warden">
              <card-testimonial :image="warden.image" :name="warden.name"
                :desig="warden.designation">
                <i class="fa fa-envelope"></i><br>
                <strong>{{ warden.email }}</strong><br>
                <i class="fa fa-address-book"></i><br>
                <strong>+91-{{ warden.mobile }}</strong></br>
              </card-testimonial>
            </div>
          </div>
          <div class="row">
            <div style="min-width:100%;"><h3>Associate Chief Warden</h3></div>
            <div class="col black-text" v-for="warden in wardens.associate_chief_warden">
              <card-testimonial :image="warden.image" :name="warden.name"
                :desig="warden.designation">
                <i class="fa fa-envelope"></i><br>
                <strong>{{ warden.email }}</strong><br>
                <i class="fa fa-address-book"></i><br>
                <strong>+91-{{ warden.mobile }}</strong></br>
              </card-testimonial>
            </div>
          </div>
          <div class="row">
            <div style="min-width:100%;"><h3>Warden</h3></div>
            <div class="col black-text" v-for="warden in wardens.warden">
              <card-testimonial :image="warden.image" :name="warden.name"
                :desig="warden.designation">
                <i class="fa fa-envelope"></i><br>
                <strong>{{ warden.email }}</strong><br>
                <i class="fa fa-address-book"></i><br>
                <strong>+91-{{ warden.mobile }}</strong></br>
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
  name: "Wardens",
  data () {
    return {
      wardens: {}
    }
  },
  created () {
    axios.get(genBackendURL("administration/wardens"))
         .then(response => {
           this.wardens = response.data.wardens
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
