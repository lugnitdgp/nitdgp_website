<template>
  <links-page>
    <card title="Wardens">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row">
            <div style="min-width:100%;"><h3>Chief Warden</h3></div>
            <card-testimonial v-for="(warden, i) in wardens.chief_warden" :key="i"
              class="card-wardens black-text"
              :image="warden.image"
              :name="warden.name"
              :desig="warden.designation">
                <strong>{{ warden.email }}</strong><br>
                <strong>+91-{{ warden.mobile }}</strong></br>
            </card-testimonial>
          </div>
          <div class="row">
            <div style="min-width:100%;"><h3>Associate Chief Warden</h3></div>
            <card-testimonial v-for="(warden, i) in wardens.associate_chief_warden" :key="i"
              class="card-wardens black-text"
              :image="warden.image"
              :name="warden.name"
              :desig="warden.designation">
              <strong>{{ warden.email }}</strong><br>
              <strong>+91-{{ warden.mobile }}</strong></br>
            </card-testimonial>
          </div>
          <div class="row">
            <div style="min-width:100%;"><h3>Warden</h3></div>
            <card-testimonial v-for="(warden, i) in wardens.warden" :key="i"
              class="card-wardens black-text"
              :image="warden.image"
              :name="warden.name"
              :desig="warden.designation">
              <strong>{{ warden.email }}</strong><br>
              <strong>+91-{{ warden.mobile }}</strong></br>
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

<style>
  .card-wardens {
    min-width: 230px !important;
    min-height: 200px !important;
    max-width: 400px !important;
    max-height: 500px !important;
    padding: 10px !important;
  }
</style>
