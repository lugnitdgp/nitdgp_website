<template>
  <links-page>
    <card title="Unnat Bharat Abhiyan (UBA)">
      <div class="col-12 caro">
        <Carousel :slides="slides"></Carousel>
      </div>
      <br>
      <div style="background-color: #001333;font-size: 20px;color: #fff;padding: 10px;text-align: center;">About UBA</div>
          <div style="border: 2px solid #001333;padding: 10px;text-align: justify;color: #000;">
            <h2>Background and Need:</h2>
            As foreseen by Gandhi Ji in his seminal work, ‘Hind Swaraj’, the western developmental paradigm, based on centralized technologies
            and urbanization, has given rise to serious problems like increasing inequity (leading to crime and violence), and climate change due to rapid ecological
            degradation. To ameliorate these problems, it is necessary to promote development of rural areas in tune with Gandhian vision of self-sufficient ‘village republics’, based on local resources and using decentralized, eco-friendly technologies so that the basic needs of food, clothing, shelter, sanitation, health care, energy, livelihood, transportation, and education are locally met. This should be the vision of holistic development of villages. Presently, 70% of the population in India lives in rural areas engaged in agrarian economy with agriculture and allied sector employing 51% of the total work-force but accounting for only 17% of the country’s GDP. There are huge developmental disconnects between the rural and urban sectors such as inequity in health, education, incomes and basic amenities as well as employment opportunities – all causing great discontent and large-scale migration to urban areas. The imperatives of sustainable development which are being felt more and more acutely all over the world also demand eco-friendly development of the villages and creation of appropriate employment opportunities locally. Increasing urbanization is neither sustainable nor desirable. So far, our professional higher education institutions have largely been oriented to cater to the mainstream industrial sector and, barring a few exceptions, have hardly contributed directly to the development of the rural sector. Unnat Bhārat Abhiyān (UBA) is a much needed and highly challenging initiative in this direction.
            <h2>History:</h2>
            The conceptualization of Unnat Bharat Abhiyan started with the initiative of a group of dedicated faculty members of Indian Institute of Technology
            (IIT) Delhi working for long in the area of rural development and appropriate technology. The concept was nurtured through wide consultation with the
            representatives of a number of technical institutions, Rural Technology Action Group (RuTAG) coordinators, voluntary organizations and government agencies,
            actively involved in rural development work, during a National workshop held at IIT Delhi in September, 2014. The workshop was sponsored by Council for
            Advancement of People’s Action and Rural Technology (CAPART), Ministry of Rural Development, Govt. of India. The program was formally launched by
            the Ministry of Human Resource Development (MHRD) in presence of The President of India on 11th Novembter, 2014.

            <h2>Vision:</h2>
            Unnat Bharat Abhiyan is inspired by the vision of transformational change in rural development processes by leveraging knowledge institutions to help build the architecture of an Inclusive India.
            <h2>Mission:</h2>
            The Mission of Unnat Bharat Abhiyan is to enable higher educational institutions to work with the people of rural India in identifying development challenges and evolving appropriate solutions for accelerating sustainable growth. It also aims to create a virtuous cycle between society and an inclusive academic system by providing knowledge and practices for emerging professions and to upgrade the capabilities of both the public and the private sectors in responding to the development needs of rural India.
            <h2>Goals:</h2>
            <ul>
              <li>To build an understanding of the development agenda within institutes of Higher Education and an institutional capacity and training relevant to national needs, especially those of rural India.</li> 
              <li>To re-emphasize the need for field work, stake-holder interactions and design for societal objectives as the basis of higher education.</li> 
              <li>To stress on rigorous reporting and useful outputs as central to developing new professions.</li> 
              <li>To provide rural India and regional agencies with access to the professional resources of the institutes of higher education, especially those that have acquired academic excellence in the field of science, engineering and technology, and management.</li> 
              <li>To improve development outcomes as a consequence of this research. To develop new professions and new processes to sustain and absorb the outcomes of research.</li> 
              <li>To foster a new dialogue within the larger community on science, society and the environment and to develop a sense of dignity and collective destiny.</li>
            </ul> 
            <h2>How You Can Participate in UBA?</h2>
            You are welcome to participate in the Unnat Bharat Abhiyan in any of the following capacity as per your present status, competence and interest: <br>
            <ul>
              <li>As a prospective Mentoring Institute </li>
              <li>As a Participating Institute </li>
              <li>As a Subject Expert </li>
              <li>As a Voluntary Organization </li>
              <li>As a Developmental Agency </li>
              <li>As a Philanthropist or a CSR Promoter </li>
              <li>As NSS Member </li>
              <li>As an Enthusiastic Volunteer</li>
            </ul>
          </div><br>
          <div style="background-color: #001333;font-size: 20px;color: #fff;padding: 10px;text-align: center;">Committee of UBA at NIT Durgapur</div>
          <div style="border: 2px solid #001333;padding: 10px;text-align: justify;color: #000;">
            <ol>
              <li><b>Advisor:</b></li> 
              <div>Prof. Anupam Basu,<br> Director,<br> NIT Durgapur</div>
              <li><b>Coordinators:</b></li> 
              <div>Prof. Tapas Kumar Saha (Coordinator)<br> Professor Department of Electrical Engineering<br> NIT Durgapur</div>
              <div>Dr. Shri Krishan Rai (Co-coordinator)<br> Associate Professor<br> Department of Humanities and Social Sciences<br> NIT Durgapur </div>
              <div>Dr. Hirok Chaudhuri (Co-coordinator)<br> Associate Professor<br> Department of Physics<br> NIT Durgapur </div>
          </ol>
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


export default {
  name: 'Uba',
  data () {
    return {
      slides:{},
    }
  },
  created () {
    axios.get(genBackendURL('activities/coecarousel'))
         .then(response => {
          let coecarousels = response.data.coecarousels
          this.slides = coecarousels.UBA
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
  .member{
    width: 30%;
    background: #e0f7fa;
    padding: 5px;
    float: left;
    display: border-box;
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