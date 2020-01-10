<template>
  <links-page>
    <card title="STRATEGIC PLAN OF NIT DURGAPUR">
      <div style="background-color: #001333;font-size: 20px;color: #fff;padding: 10px;text-align: center;">STRATEGIC PLAN</div>
          <div style="border: 2px solid #001333;padding: 10px;font-size:18px;text-align: justify;color: #000;">
            The Institute Strategy document was prepared to reaffirm its commitment to excellence in technical education and research, develop life-long learning and analytical capabilities and inculcate values and ethics among the students and contribute meaningfully to the society. The students would be expected to contribute significantly to the industries and be encouraged to take up higher education, research and entrepreneurship. Innovation and flexibility would be at the focus of all endeavours. Emphasis shall be placed on the outreach activities.<br>

            The Institute envisions its place among the top premier institutions in the world in a foreseeable future. To achieve that, the Vision and Missions of the Institute were formulated, a few long-term and short-term goals were identified, and the activitieson plans were decided upon.<br>
            <ol>
              <b><li>Vision:</li></b>
              To impart quality technical education and focus on research and innovation to cater to the need of the country
            <b><li>Mission:</li></b>

              To impart quality technical and scientific education and produce engineers, technologists, scientists and citizens who will contribute meaningfully to the growth and development of the country and excel in various disciplines of knowledge

              To initiate the students to research-oriented teaching-learning environment in the Institute with a focus on excellence and innovation
            <b><li>Goals: </li></b>
              The following goals, long-term and short-term, were set to achieve the Vision and Missions.
              <ol>
                <li><b>Long-term Goals</b></li>
                    Provide transformational education to have life-long learning. 
                    Lead research and innovation to uplift the prestige of the country. 
                    Cultivate a community that embodies collaborative and inclusive excellence. 
                    Enhance engagement with the society and industry
                <li><b>Short-term Goals</b></li>
                  Become a leading educational institute, ranked in the top 10 of NIRF ranking in engineering category. 
                  Establish reputation in research and innovation for industrial and national needs 
                  Broaden the educational areas and funding base.
                  Attract more number of international students and increase international collaborations.
                  Enhance alumni linkage
                  Develop cleaner and greener campus.
              </ol> 
            <b><li>Action Plan</li></b>
              To achieve the goals, a set of Action Plan in various domains of activities was prepared.
              <ol>
                <li><b>Academics (Teaching – Learning)</b></li>
                Revision of curriculum to meet today’s need of the Industry and society and allow flexibility to the students 
Increase in participation of industrial subject experts in the curriculum revision process and content delivery. 
Systematic conduct of regular academic audit in-line of the guidelines given by NIT Council. 
Initiatives to have all the programs accredited. 
Use of language laboratory, finishing school and soft skill development to improve the employability of the students. 
Create enthusiasm about higher studies among the students. 
Capacity increase in the demanding academic programs. 
Collaboration with other reputed academic institutes / organizations in India and abroad for student exchange program at all levels. 
Promoting development of e-learning courses
More multi-disciplinary academic programs to be developed
Promoting participation in competitive sports and games and other extra-curricular activities. 

<li><b>Research </b></li>
Emphasizing on the research-spike areas including environment and water management, assistive technology for people with special needs, etc.
Increase in the number of quality research publications, patents, sponsored research and consultancy projects. 
Development of more numbers of industry / alumni-funded research facilities
Encouraging Faculty members to conduct quality research in collaboration with reputed academic / research / industrial organizations. 
Increase in intake of PhD research scholars 
Development of tinkering laboratories for the UG students to get engaged in research early
Quality improvement of the COEs, central research facilities established through HEFA
Strengthening of Sponsored Research & Consultancy Cell

<li><b>Human Resource Development</b></li>
Regular conduct of recruitment of faculty, staff and officers.
Initiatives to create enthusiasm among the employees to be in continuous development process of the Institute and their all-round personal development. 
Increase in participation, organization of different faculty development process (refresher courses, pedagogical training, conferences and training programs in domain areas).
 
<li><b>Infrastructure Development</b></li>

<p><b>(a)</b> Hostel - Complete renovation of existing old hostels, increase in recreation, games and sports facilities, furniture in the hostels, development of a common mess catering diversified meals. </p>

<p><b>(b)</b> Internet Facility – Improvement in the internet network for un-interrupted and high-speed connectivity at all corners of the Institute.</p> 

<p><b>(c)</b> Library – Increase in text and reference books, reading room facility, journal access, and RFID tagging of all textual materials and use of an ERP system, improvement of the ambience.</p> 

<p><b>(d)</b> Class Room – Modernization of existing class-rooms of the old academic building equipped with audio-visual aids. Increase in the number of more AC class rooms.</p> 

<p><b>(e)</b> Workshop and Laboratory – Modernization and replacement of old equipments, expansion of existing UG and PG laboratories, creation of a RPT and 3D printing facility in the workshop, establishment of some laboratory equipments for learning beyond the syllabus and to have joy of engineering and technology. </p>

<p><b>(f)</b> Capacity and facility enhancement of the academic and administrative buildings</p>

<p><b>(g)</b> Use of a comprehensive ERP system</p>

<p><b>(h)</b> Campus Facility - Promote and sustain a campus environment that supports a high quality of life and learning through continuous maintenance of quarters, medical unit, shops, roads, drainage and lighting systems, security, play grounds and campus beautification. Building a new space for Yoga and Counseling centre.</p> 

<li><b>Outreach Activities</b></li>
Societal Participation - Unnat Bharat Aviyan, Rashtriya Avishkar Aviyan, Vigyan Prasar, Adoption of Rural Schools etc.
Promoting organization of more and more GIAN, STCs, Collaborative Workshops and Conferences. 
Active participation in TEQIP-III, mentoring other institutes 
Increase in MOUs and Collaboration with the outside world. 

<li><b>Miscellaneous</b></li>
<ol type="i">
  <li>Improvement of ranking – The Institute aspires to secure an NIRF rank within 20 among the top engineering institutions in India. It would also like to be included in the QS and THE international ranking. All efforts shall be made to improve research, academic, placement performance and infrastructure to achieve it.</li>

  <li>Strengthening of alumni networking – The Alumni Cell shall be rejuvenated to enhance interaction with the alumni. Support will be sought from them for creation of infrastructure and sharing their expertise for the development of the students and the faculty.</li>

  <li>Strengthening of Industry-Institute-Interaction and I-I-I cell in the Institute – Greater interaction shall be made with the industries by way of collaborative projects, Industry PhD programme, visiting lectures by the industry experts and their participation in the academic committees and revision of curricula.</li>
</ol>
</ol>
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