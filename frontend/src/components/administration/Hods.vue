<template>
  <links-page>
    <card title="Head Of Departments">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row">
            <div class="col" v-for="hod in hods">
              <div class="card testimonial-card">
                <div class="card-up">
                </div>
                <div class="avatar mx-auto">
                  <img :src="hod.image" class="rounded-circle img-responsive">
                </div>
                <div class="card-body-in">
                  <h4 class="card-title mt-1"><strong>{{ hod.name }}</strong></h4>
                  <hr>
									<strong> {{ hod.department }} </strong><br>
                  <p class="min-profile">
                    <i class="fa fa-envelope"></i><br>
                    <strong>{{ hod.email }}</strong><br>
                    <i class="fa fa-address-book"></i><br>
                    <strong>+91-{{ hod.mobile }}</strong></br>
                  </p>
                </div>
              </div>
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
import { genBackendURL } from '@/common.js'

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
    Card
  }
}
</script>
