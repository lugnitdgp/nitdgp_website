<template>
  <links-page>
    <card title="CREW">
    	<h3>Page Under Construction</h3>
    </card>
  </links-page>
</template>
<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import CollapseList from '@/components/CollapseList'
import CardCollapse from '@/components/CardCollapse'


export default {
  name: 'Crew',
  data () {
    return {
      
    }
  },
  created () {
  	this.$emit('hideloader', true)
         
  },
  components: {
    LinksPage,
    CollapseList,
    CardCollapse,
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