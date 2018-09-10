<template>
  <div class="page-type-person">
    <h1 class="name-title" align="center">MEET OUR DIRECTOR</h1>
    <div class="card testimonial-card">
      <div class="card-up">
        <img :src="director.image" >
      </div>
      <div class="card-body">
        <h3 class="mt-1 white-text">
          <a :href="genBackendURL('faculty/2c36b313-cfa6-47bf-b1fa-9b2b226fa8f0',true)"><strong>{{director.name}}</strong></a>
        </h3>
        <h4 class="desig cyan-text">Director</h4>
        <hr class="hr-grey">
        <p class="white-text" align="center">
          <i class="fa fa-map-marker fa-1x"></i><br>
          National Institute of Technology,<br>
          Mahatma Gandhi Avenue,<br>
          Durgapur, West Bengal, India,<br>
          PIN – 713209.<br>
          <i class="fa fa-envelope fa-1x"></i><br>
          {{ director.email }}<br>
          <i class="fa fa-phone fa-1x"></i><br>
          Phone :+91 {{ director.mobile }} (O)<br>
          Fax :+91 {{ director.fax }}<br>
          <!-- Fax :+91 343 2547375<br> -->
          <!-- <a href="#" class="white-text">*MoreInfo*</a> -->
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { genBackendURL } from '@/common.js'

export default {
  name: 'Director',
  data () {
    return {
      director: {
        name: "Prof. Anupam Basu",
        image: "/static/img/director_image.jpg",
        email: "director@admin.nitdgp.ac.in",
        mobile: "343 2546397",
        fax: "343 2547375"
      }
    }
  },
  methods: {
    genBackendURL: genBackendURL
  },
  created () {
    this.$emit('hideloader', true)
  }
}
</script>
