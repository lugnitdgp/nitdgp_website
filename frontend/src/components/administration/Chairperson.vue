<template>
  <div class="page-type-person">
    <h1 class="name-title" align="center"> MEET OUR CHAIRPERSON </h1>
    <div class="card testimonial-card">
      <div class="card-up">
        <img :src="chairperson.image" >
      </div>
      <div class="card-body">
        <h3 class="mt-1 white-text">
          <strong>{{ chairperson.name }}</strong>
        </h3>
        <h4 class="desig cyan-text">Chairperson</h4>
        <hr class="hr-grey">
        <p class="white-text" align="center">
          <i class="fa fa-map-marker fa-1x"></i><br>
          National Institute of Technology,<br>
          Mahatma Gandhi Avenue,<br>
          Durgapur, West Bengal, India,<br>
          PIN – 713209.<br>
          <i class="fa fa-envelope fa-1x"></i><br>
          {{ chairperson.email }}<br>
          <i class="fa fa-phone fa-1x"></i><br>
          Phone :+91 {{ chairperson.mobile }} (O)<br>
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
  name: 'Chairperson',
  data () {
    return {
      chairperson: {}
    }
  },
  created () {
    axios.get(genBackendURL("administration/chairperson"))
         .then(response => {
           this.chairperson = response.data.chairperson
           this.chairperson.mobile = String(this.chairperson.mobile).slice(0,3) +
                                  " " + String(this.chairperson.mobile).slice(3,)
         })
         .catch(e => {
           console.log(e)
         })
    this.$emit('hideloader', true)
  }
}
</script>
