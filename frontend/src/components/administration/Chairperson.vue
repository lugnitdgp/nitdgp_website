<template>
  <div class="page-type-person">
    <h1 class="name-title" align="center">MEET OUR CHAIRPERSON</h1>
    <div class="card testimonial-card">
      <div class="card-up">
        <img v-if="director.image" :src="director.image" >
      </div>
      <div class="card-body">
        <a :href="director.details" target="_blank">
          <h3 class="mt-1 white-text">
            <strong>{{director.name}}</strong>
          </h3>
        </a>
        <h4 class="desig cyan-text">Chairperson of BoG </h4>
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
        name: "Prof. (Retd.) Sadanand Sadashiv Gokhale",
        image: "",
        email: "",
        mobile: "",
        details: "http://nitdgp.ac.in/AllPDF/SSG_Short.pdf",
        fax: ""
      }
    }
  },
  created () {
    this.$emit('hideloader', true)
  }
}
</script>
