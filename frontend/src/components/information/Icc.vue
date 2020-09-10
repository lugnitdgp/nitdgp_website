<template>
  <links-page>
    <card title="ICC Members">
      <div class="carousel-inner person-list" role="listbox">
	<div class="carousel-item active">
	  <div class="row">
	    <card-testimonial v-for="(person, i) in members" :key="i"
              :name="person.name"
              :image="person.image"
              :desig="person.title">
	      {{person.designation}}
	    </card-testimonial>
	  </div>
	</div>
      </div>
    </card>
    <card title="ICC">
      <ul class="list-group list-gr">
        <li v-for="icc in iccs">
          <a v-if="icc.link" class="list-group-item" target="new" :href="icc.link">
            {{icc.title}}
          </a>
          <a v-else class="list-group-item" target="new" :href="icc.file">
            {{icc.title}}
          </a>
        </li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import Card from "@/components/Card"
import CardTestimonial from '@/components/CardTestimonial'
import LinksPage from "@/components/LinksPage"
import axios from 'axios'
import { genBackendURL } from '@/common.js'

export default {
  name: "Icc",
  data () {
    return {
      iccs: [],
      members: [
        
        {name:"Dr. Seema Sarkar Mandal", title:"Professor, Department of Mathematics National Institute of Technology Durgapur", designation:"Presiding Officer"},
        {name:"Dr. Jaya Sikdar", title:" Associate Professor, Department of Chemical Engineering National Institute of Technology Durgapur", designation:"Convener", image:"https://admin.nitdgp.ac.in/files/faculty/Jaya%20Sikder/20200108_193644.jpg"}, {name:"Dr.  Sanghita Bhattacharjee ", title:" Associate Professor, Department of Computer Science & Engineering National Institute of Technology Durgapur", designation:"Nodal Person", image:"https://admin.nitdgp.ac.in/files/faculty/Sanghita%20Bhattacharjee/s_mukh.jpg"}, 
        {name:"Dr. Surabhi Chaudhuri", title:"Professor, Department of Biotechnology National Institute of Technology Durgapur", designation:"Member", image:"https://admin.nitdgp.ac.in/files/faculty/Surabhi%20Chaudhuri/828.JPG"},
        {name:"Dr. Lakshmi Kanta Dey", title:"Associate Professor, Department of Mathematics National Institute of Technology Durgapur", designation:"Member", image:"https://admin.nitdgp.ac.in/files/faculty/Lakshmi%20Kanta%20Dey/l_K_dey.jpg"},
        {name:"Mr. Santosh Saha", title:"Technical Officer, National Institute of Technology Durgapur", designation:"Member"},        
        {name:"Dr. G. Prabhavathi", title:"Medical Officer, National Institute of Technology Durgapur", designation:"Member"},
        {name:"Ms. Sarmistha Dutta Gupta", title:"Founder-Secretary Ebong Alaptop", designation:"Member"},
        {name:"Dr. Mallika ghosh Sarbadhikary", title:"Associate Professor, Department of Humanities and Social Science Indian Institute of Engineering Science & Technology", designation:"Member"},
        {name:"Ms. Nandita Dhawan", title:"Assistant Professor, School of Women's Studies Jadavpur University", designation:"Member"},
        {name:"Mr. Sirajul Islam", title:"Senior Advocate Durgapur Court", designation:"Member"}       
        
        
        
        
      ]
    }
  },
  created () {
    axios.get(genBackendURL('information/icc'))
         .then(response => {
           this.iccs = response.data.results
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log("Axios(GET[information]): Error: " + e)
         })
  },
  components: {
    Card,
    CardTestimonial,
    LinksPage
  }
}
</script>
