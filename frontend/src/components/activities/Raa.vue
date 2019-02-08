<template>
  <links-page>
    <card title="Rashtriya Avishkar Abhiyan (RAA)">
    	Rashtriya Avishkar Abhiyan (RAA) is an initiative of the Government of India, Ministry of Human Resource and Development (MHRD) to popularize science, mathematics and technology among school students. While emphasising the primacy of the schools and classroom transactions, the RAA aims to leverage the potential for science, mathematics and technology learning in non-classroom settings. Beyond the four walls of a classroom, opportunities for science, mathematics and technology learning abound. Accordingly, the RAA is planned to provide nourishing and nurturing support to and a platform for schools in a dual track approach to make Science, Mathematics and Technology exciting to children and encourage them to have an enduring interest both inside classroom and outside classroom activities. The objectives of this RAA programme is (i) to enable children to become motivated and engaged in Science, Mathematics and Technology (SMT) through observation, experimentation, inference drawing, model building, rational reasoning, testability etc. (ii) to create curiosity, excitement and exploration among school children in Science, Mathematics and Technology. (iii) to create a culture of thinking, inventing, tinkering and doing to promote enquiry based learning in Schools. RAA will target students in the age group of 6-18 years and in turn the execution of RAA will span across MHRD’s schematic interventions of Sarva Shiksha Abhiyan in the Department of School Education & Literacy and programmes and schemes of Department of Higher Education to encourage Science, Mathematics & Technology. NIT Durgapur is a mentoring institute along with IIT Kharagpur and IISER Kolkata for RAA for the state of West Bengal. In collaboration with Govt. of West Bengal, Paschim Banga Samagra Shiksha Mission, NIT Durgapur prepare a plan for promotion of science and mathematics among the school students of the state of West Bengal. 

    </card>
  </links-page>
</template>
<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
// import CollapseList from '@/components/CollapseList'
// import CardCollapse from '@/components/CardCollapse'


export default {
  name: 'Raa',
  data () {
    return {
      
    }
  },
  created () {
  	this.$emit('hideloader', true)
  },
  components: {
    LinksPage,
    Card
  }
}
</script>
<style >
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
  h2{
    height: 40px;
    background: #01576A;
    display: block;
    width: 15%;
    font-size: 20px;
    color: #FFF;
    text-align: center;
    line-height: 40px;
    border-top-left-radius: 8px;
  }
   .descbox:hover{
    background: #C7ECF5;

  }
  @media screen and (max-width: 1200px){
    .list-gr .contact-col{
      min-width: 100%;
      max-width: 100%;
    }
    h2{
    height: 40px;
    background: #01576A;
    display: block;
    width: 30%;
    font-size: 18px;
    color: #FFF;
    line-height: 40px;
    border-top-left-radius: 8px;
    }
  }
  @media screen and (max-width: 800px){
    .list-gr .contact-col{
      min-width: 100%;
      max-width: 100%;
    }
    h2{
    height: 40px;
    background: #01576A;
    color: #FFF;
    display: block;
    width: 100%;
    font-size: 25px;
    line-height: 40px;
    border-top-left-radius: 8px;
  }
  }
</style>