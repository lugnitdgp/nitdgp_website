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
        <p class="white-text" align="justify">
          Prof. Anupam Basu, currently the Director and Professor of NIT Durgapur, is also a Professor at Department of Computer Science Engineering in IIT Kharagpur, India. Previously He has taught at University of California, Irvine and University of Guelph, Ontario, Canada as a visiting Professor and have been the Humboldt Fellow at TU Dortmund, Germany. Even before that, He has been a Systems Engineer for Webel Computers Ltd, India. His research Interests are Embedded Systems, Natural Language Processing, Assistive Technology, Natural Interface Design, Human Computer Interaction and ICT4D.He is the recipient of Da Vinci Award, Engineering Society of Detroit and Multiple Sclerosis Society of Michigan, for the technology for communication by the speech impaired and people with cerebral palsy, 2004. Fellow of Indian National Academy of Engineering, 2000, Humboldt Fellowship, Jaycee Award for Outstanding Persons,  Young Scientist Award, Dept. of Science & Technology, Govt. of India, 1992, for R&D towards devices for visually handicapped. <a href="http://www.iitkgp.ac.in/cv/cs-anupam" target="_new">http://www.iitkgp.ac.in/cv/cs-anupam</a>
        </p>
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
