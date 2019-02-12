<template>
  <links-page>
    <card title="National Institute of Technology Durgapur NCC Unit 10 Bengal BN, AsansoL">
      <div class="col-12 caro">
        <Carousel :slides="slides"></Carousel>
      </div>
      <br>
    	<div style="background-color: #001333;color: #fff;padding: 10px;text-align: center;">About Us</div>
          <div style="border: 2px solid #001333;padding: 10px;text-align: justify;color: #000;">
            A unit of National Cadet Corps )NCC) Army wing was started in this Institution since 2012  as open vacancy among UG students (Boys & Girls) under the supervision of 10 Bengal Bn, NCC, Asansol. The cadets have participated regular training programme including attend  camps, appearing ‘B’ ‘C’ Certificate examination and actiively involve in several extension activities like Independence Day celebration, Republic Day celebration, NCC Day celebration etc. This wing also observed and participated various important days like environment Day, Voters Day organized rallies, Swachchta  programme, tree plantation etc.<br>
            Beside above mentioned activities this wing undertake compulsory co-curricular credit courses (XXS-51 & XXS-52) for first two semester.<br>
            Mr. Hillol Mukherjee, Physical Training Instructor & I/C Student Activity Centre has supervised the NCC Activities as Company Commander of this Unit.

          </div>
      
    </card>
  </links-page>
</template>
<script>
import axios from 'axios'
import { genBackendURL, convertNewsfeed } from '@/common.js'
import Carousel from '@/components/Carousel'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
// import CollapseList from '@/components/CollapseList'
// import CardCollapse from '@/components/CardCollapse'


export default {
  name: 'Ncc',
  data () {
    return {
      crewimg: {},
      slides:{},
    }
  },
  created () {
    axios.get(genBackendURL('activities/coecarousel'))
         .then(response => {
          let coecarousels = response.data.coecarousels
          console.log(coecarousels)
          this.slides = coecarousels.CREW
          this.$emit('hideloader', true)
          })
         .catch(e => {
           console.log(e)
         })
  	
         
  },
  components: {
    LinksPage,
    Card,
    Carousel
  }
}
</script>
<style  >
  .list-gr .contact-col{
    min-width: 100%;
    max-width: 100%;
    padding-bottom: 15px;
    color: #fff;
  }
  .col {
    -ms-flex-preferred-size: 0;
    flex-basis: 0;
    -ms-flex-positive: 1;
    flex-grow: 1;
    max-width: 100%;
  }
  
  @media screen and (max-width: 1200px){
    .list-gr .contact-col{
      min-width: 100%;
      max-width: 100%;
    }
  }
  @media screen and (max-width: 800px){
    .list-gr .contact-col{
      min-width: 100%;
      max-width: 100%;
    }
  }
</style>