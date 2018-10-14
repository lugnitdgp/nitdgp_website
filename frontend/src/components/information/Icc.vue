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
        {name:"Prof.(Mrs.) Kajla Basu", title:"Prof. of Mathematics", designation:"Presiding Officer", image:"https://admin.nitdgp.ac.in/files/faculty/Kajla%20Basu/kajla_basu.jpg"},
        {name:"Mrs. Soma Sinha", title:"Advocate, Calcutta High Court", designation:"Member(External)" },
        {name:"Prof A. Gangopadhyay", title:"Prof, Dept of EES" ,designation:"Member", image:"https://admin.nitdgp.ac.in/files/faculty/Aniruddha%20Gangopadhyay/aniruddha_ganguly.jpg"},
        {name:"Dr (Ms.) Mamata Dalui", title:"Astt. Prof. C.Sc. Deptt" ,designation:"Member", image:"https://admin.nitdgp.ac.in/files/faculty/Mamata%20Dalui%20(Chakraborty)/m_dalui.jpg"},
        {name:"Dr. Kazy Sufia Khannam", title:"Astt. Prof Deptt. of BT" ,designation:"Member", image:"https://admin.nitdgp.ac.in/files/faculty/Sufia%20Khannam%20Kazy/Sufia_Kazy.jpg"},
        {name:"Dr. G. Prabhavathi", title:"Medical Officer, NITD" ,designation:"Member" },
        {name:"Dr. (Mrs.) Debjani Dutta", title:"Astt. Prof. Deptt. of BT" ,designation:"Member & Convenor", image:"https://admin.nitdgp.ac.in/files/faculty/Debjani%20Dutta/debjani_dutta.jpg"}
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
