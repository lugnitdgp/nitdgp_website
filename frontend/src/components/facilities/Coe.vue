<template>
  <!-- <div class="l1 page-type-links">
    <div class="card">
      <a class="card-header white-text">Centre of Excellence in Advanced Materials</a>
      <div class="card-body">
        <div class="card-text">
          <ul>
            <li><a target="new" href="http://nitdgp.ac.in/AllPDF/Centre of Excellence in Advanced Materials-home.pdf">CEAM home</a></li>
            <li><a target="new" href="http://nitdgp.ac.in/AllPDF/coe-converted.pdf">CEAM Doc</a></li>
          </ul>
        </div>
      </div>      
    </div> -->
    <links-page>
    <card title="Centre of Excellence">
      <div class="row">
        <div v-for="(coe, i) in coes" :key="i">
        <a :href="coe.link" target="_blank"><card-testimonial :image="coe.image" :name="coe.name">
            <!-- <span v-html="stripDesc(coe.description)"></span> --><br>
            <strong>{{ coe.link }}</strong><br>
          </card-testimonial></a>
        </div>
      </div>
    </card>
  </links-page>
 <!--  </div> -->
</template>
<script>
  import axios from 'axios'
  import LinksPage from '@/components/LinksPage'
  import Card from '@/components/Card'
  import CardTestimonial from '@/components/CardTestimonial'
  import { genBackendURL,stripDesc } from '@/common.js'

export default {
  name: 'Coe',
  data () {
    return {
      coes: {}
    }
  },
  methods: {
    stripDesc: stripDesc
  },
  created () {
    axios.get(genBackendURL("activities/coe"))
         .then(response => {
           console.log(response)
           this.coes = response.data.results
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
  a{
    font-size: 18px;
    color: #000;
    text-decoration: none;
  }
</style>