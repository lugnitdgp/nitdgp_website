<template>
  <links-page>
    <card title="National Service Scheme (NSS)">
      <div class="col-12 caro">
        <Carousel :slides="slides"></Carousel>
      </div>
      <br>
    	<div style="background-color: #001333;color: #fff;padding: 10px;text-align: center;">About Us</div>
          <div style="border: 2px solid #001333;padding: 10px;text-align: justify;color: #000;">
            The National Service Scheme (NSS) is an Indian government-sponsored
flagship for public service program conducted by the Ministry of Youth Affairs
and Sports of the Government of India. Popularly known as NSS, the scheme
was launched in Gandhiji&#39;s Centenary year in 1969. Since the inception of NSS
by the Indian Government, a unit of National Service Scheme was started in
our institution. NSS is a voluntary association of young people in colleges,
universities and at +2 level working for a campus-community linkage, aimed at
developing student’s personality through community service. We work with a
main motto of “NOT ME, BUT YOU”. NSS at NIT, Durgapur is currently being
supervised/coordinated by Dr.Shri Krishan Rai.
We observe many important events celebrated by Government of India like
Independence Day, Republic day, Swachchta Pakhwada, Vigilance awareness
week, National Education day, Hindi Pakhwada, Matribhasha diwas etc., Our
volunteers participate in the Parade that takes place in our college during
Independence Day, Republic Day and Sports day every year. In order to create
awareness, our volunteers even conduct some rallies, quizzes, essay writing
competitions etc., on National Education Day, Vigilance awareness week etc.
Also as a part of Matribhasha diwas we organise a major event containing
cultural performances by students from various parts of our country and also a
food fest where students from different regions cook and sell some famous
dishes of their regions.
Apart from the above events we do make some camps at nearby villages. This
includes Annual Medical Camp (in which we organise basic medical facilities for
two or three days in a nearby village), Plastic Free Village and Water
Conservation Campaign (in which we explained people in a nearby village
about ill effects of Plastic on earth, importance of water conservation and
distributed Jute bags), Plantation campaign within the campus, Cloth
distribution campaign to the poor and needy (in which we collect clothes not in
use from our students and staff and distribute them to the poor and needy)
and many more.
We induce our Volunteers as a part of compulsory co-curricular activity
courses in Semester-1,2. We also induce any other interested candidates at the
beginning of every semester. Active volunteers receive certificates at the end

of 8 th semester. For proper functioning we divide ourselves into units and
distribute the work.

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
      slides:{},
    }
  },
  created () {
    axios.get(genBackendURL('activities/coecarousel'))
         .then(response => {
          let coecarousels = response.data.coecarousels
          this.slides = coecarousels.NSS
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