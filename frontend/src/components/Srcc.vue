<template>
  <links-page>
    <card title="Sponsored Research & Consultancy Cell">

      <h3>Page Under Construction</h3>
    	<!--<div class="carouselstyle">
    		<Carousel :slides="slides"></Carousel>
    	</div>
    	<div style="border: 2px solid #cad;padding:5px;margin-bottom: 5px;text-align: justify;">
    		<p>
    			<h3>Description Text</h3>
    			Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
				Why do we use it?

				It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).

				Where does it come from?

				Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
    		</p>
    	</div>-->
      <collapse-list>
        <card-collapse  title="Ongoing Project">
          <div class="card-text">
            <!--<table class="table table-bordered">
            	<thead>
	            	<th style="width: 5%;margin: auto;">SL</th>
	            	<th style="width: 5%;">Year</th>
	            	<th style="width: 60%;">Title</th>
	            	<th style="width: 20%;">PI</th>
	            	<th style="width: 10%;">Sponsoring Agency</th>
	            </thead>
	            <tbody>
	            	<td>1</td>
	            	<td>2018</td>
	            	<td>Project  Title</td>
	            	<td>Investigator</td>
	            	<td>Agency</td>
	            </tbody>
            </table>-->
          </div>
        </card-collapse>
        <card-collapse  title="Completed Project">
          <div class="card-text">
            <!--<table class="table table-bordered">
            	<thead>
	            	<th>SL</th>
	            	<th>Year</th>
	            	<th>Title</th>
	            	<th>PI</th>
	            	<th>Sponsoring Agency</th>
	            </thead>
	            <tbody>
	            	<td>1</td>
	            	<td>2018</td>
	            	<td>Project  Title</td>
	            	<td>Investigator</td>
	            	<td>Agency</td>
	            </tbody>
            </table>-->
          </div>
        </card-collapse>
      </collapse-list>
    </card>
  </links-page>
</template>
<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import Carousel from './Carousel'
import CollapseList from '@/components/CollapseList'
import CardCollapse from '@/components/CardCollapse'
import axios from 'axios'
import { genBackendURL } from '@/common.js'


export default {
  name: 'Srcc',
  data () {
    return {
      slides: []
    }
  },
  created () {
  	axios.get(genBackendURL('dashboard/carousel'))
         .then(response => {
           this.slides = response.data.results
           this.$emit('hideloader', true)
           
         })
         .catch(e => {
           console.log(e)
         })  
  },
  components: {
    LinksPage,
    CollapseList,
    CardCollapse,
    Card,
    Carousel
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
.carouselstyle{
	margin-left: 15%;
	margin-right: 15%;
	margin-bottom: 10px;
}
  @media screen and (max-width: 1200px){
    .list-gr .contact-col{
      min-width: 100%;
      max-width: 100%;
    }
    .carouselstyle{
	margin-left: 10%;
	margin-right: 10%;
	margin-bottom: 10px;
	}
  }
  @media screen and (max-width: 800px){
    .list-gr .contact-col{
      min-width: 100%;
      max-width: 100%;
    }
    .carouselstyle{
	margin-left: 0%;
	margin-right: 0%;
	margin-bottom: 10px;
	}
  }
</style>