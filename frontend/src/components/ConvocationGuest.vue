<template>
  <links-page>
    <card title="16th Convocation Chief Guests'">
      <div class="guest-wrapper">
        <div class="single-guest">
          <div class="imageview">
            <img src="http://nitdgp.ac.in/convocation16guest/RameshPokhriyal.jpg" class="img img-responsive img-thumbnail">
            <p class="text-center text-black">Chief Guest, Dr. Ramesh Pokhriyal, Hon’ble Education Minister</p>
          </div>
          <div class="details">
            Dr. Ramesh Pokhriyal, Hon’ble Education Minister is also known by his pen name Nishank. He was born in Pinani village, Pauri Garhwal, Uttarakhand to Paramanand Pokhriyal and Vishambhari Devi. He received an M.A. degree from Hemwati Nandan Bahuguna Garhwal University. He represents the Haridwar Parliamentary constituency of Uttarakhand in the 17th Lok Sabha. He was the 5th Chief Minister of Uttarakhand from 2009 to 2011. He was member of 16th Lok Sabha and chairperson, Committee on Government Assurances. Pokhriyal has written novels, stories and poems. He has authored 44 books in Hindi, some of which have been translated to English as well as other Indian languages.
          </div>
        </div>
        <div class="single-guest">          
          <div class="details">
            Prof. Ashutosh Sharma (Secretary, Department of Science and Technology, Govt. of India) is an Institute Chair Professor and C. V. Seshadri Chair Professor at the Department of chemical engineering of Indian Institute of Technology Kanpur. Prof. Ashutosh Sharma got his B.Tech degree in Chemical Engineering from Indian Institute of Technology Kanpur (IIT Kanpur), India in 1982. Prof. Sharma graduated with master's degree from Pennsylvania State University in 1984 and three years later obtained his Ph.D. in Chemical Engineering from the University at Buffalo. He is best known for his pioneering research work in the areas of colloids, thin film, interfaces, adhesion, patterning and in the fabrication and application of self-assembled nano-structures.
          </div>
          <div class="imageview">
            <img src="http://nitdgp.ac.in/convocation16guest/ashutosh.jpg" class="img img-responsive img-thumbnail">
            <p class="text-center text-black">Guest of Honour, Prof. Ashutosh Sharma</p>
          </div>
        </div>
        <div class="single-guest">
          <div class="imageview">
            <img src="http://nitdgp.ac.in/convocation16guest/Prof. Gokhale.png" class="img img-responsive img-thumbnail">
            <p class="text-center text-black">Chairperson of BoG, Prof. Sadanand Sadashiv Gokhale</p>
          </div>
          <div class="details">
            Prof. Gokhale studied Aeronautical Engineering from IIT Bombay and did his MS and PhD from University of Illinois Urbana-Champaign USA in same discipline. After a brief stint as PDF he returned in 1980 and joined IIT Madras as an Assistant Professor and worked there till 2003. He served the Institute in various capacities including HoD, Adviser, Dean Students, and Management Representative for ISO 9001, Strategic Planning Committee Member etc. His academic field of specialization is Aircraft and Missile Propulsion, CFD, Simulation and Optimization and Multimedia in Engineering Education. For R&D and Consultancy projects Prof. Gokhale received funding from ISRO, DRDO, AR&DB, MHRD etc. He has published his work at several renowned national and international forums.
          </div>
        </div>
        <div class="single-guest">
          <div class="details">
            Prof. Anupam Basu, currently the Director and Professor of NIT Durgapur, is also a Professor at Department of Computer Science Engineering in IIT Kharagpur, India. Previously He has taught at University of California, Irvine and University of Guelph, Ontario, Canada as a visiting Professor and have been the Humboldt Fellow at TU Dortmund, Germany. Even before that, He has been a Systems Engineer for Webel Computers Ltd, India. His research Interests are Embedded Systems, Natural Language Processing, Assistive Technology, Natural Interface Design, Human Computer Interaction and ICT4D.
          </div>
          <div class="imageview">
            <img src="http://nitdgp.ac.in/convocation16guest/Prof. Anupam Basu.jpg" class="img img-responsive img-thumbnail">
            <p class="text-center text-black">Director of NIT Durgapur, Prof. Anupam Basu</p>
          </div>
        </div>
      </div>
    </card>
  </links-page>
</template>

<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import CollapseList from '@/components/CollapseList'
import CardCollapse from '@/components/CardCollapse'
import axios from 'axios'
import { genBackendURL } from '@/common.js'

export default {
  name: 'Liveconvocation',
  data() {
    return {
      
    }
  },
  created () { 
  	this.$emit('hideloader', true)
  },
  components: {
    LinksPage,
    Card,
    CollapseList,
    CardCollapse
  }
}
</script>
<style scoped>
  .col{
    padding:0;
    text-align: center;
  }
  .text-black{
    font-size: 15px;
    color: #000;
    font-weight: bold;
  }
  .imageview{
    height:auto;
    border-radius:8px;
    width: 60%;
  }
  .imageview img{
    height: 400px;
    width: 400px;
  }
  .single-guest{
    display: flex;
    flex-direction: row;
    width: 100%;
    box-shadow: 0 0 8px #D0D0D0; 
    padding: 10px;
    margin-bottom: 8px;
  }
  .single-guest:nth-child(1){
    background: tomato;
  }
  .single-guest:nth-child(2){
    background: #005cb9;
  }
  .single-guest:nth-child(3){
    background: #736AFF;
  }
  .single-guest:nth-child(4){
    background: #3090C7;
  }
  .details{
    margin: 8px;
    text-align: justify;
    width: 100%;
    color: #000;
    font-size: 20px;
  }
  @media screen and (max-width: 1010px)  {
    .imageview{
      height:auto;
      width: 100%;
    } 
    .imageview img{
      width: 100%;
      height: 100%;
    }
    .details{
      margin-top: 38px;
      text-align: justify;
      width: 100%;
      color: #000;
      font-size: 20px;
    }
    .single-guest{
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
    }
  }
</style>
