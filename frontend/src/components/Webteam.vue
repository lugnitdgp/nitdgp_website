<template>
  <links-page>
    <card title="Web Team">
      <div class="carousel-inner person-list" role="listbox">
	<div class="carousel-item active">
	  <div class="row">
	    <div class="col" v-for="person in webteam.people">
	      <card-testimonial :name="person.name" :image="person.image">
		
		<strong>
		  <i class="fa fa-github fa-lg"></i>
		  <a :href="'https://github.com/' + person.github_id">{{ person.github_id }}</a>
		</strong>
		
	      </card-testimonial>
	    </div>
	  </div>
	</div>
      </div>
    </card>
  </links-page>
</template>

<script>
import axios from 'axios'
import Card from '@/components/Card'
import CardTestimonial from '@/components/CardTestimonial'
import LinksPage from '@/components/LinksPage'

export default {
  name: 'Webteam',
  data () {
		return {
			webteam: {
				people: [
					{
						name: "Abhishek Prasad",
						image: "static/img/abhishek_prasad.jpg",
						github_id: "Compro-Prasad"
					},
					{
						name: "Ankan Poddar",
						image: "static/img/ankan_poddar.jpg",
						github_id: "ankan17"
					},
					{
						name: "Arnav",
						image: "static/img/arnav_kumar.jpg",
						github_id: "arnav-amb"
					},
					{
						name: "Devansh Goenka",
						image: "",
						github_id: "devanshgoenka97"
					},
					{
						name: "Divyanshu Mehta",
						image: "static/img/divyanshu_mehta.jpg",
						github_id: "divyanshumehta"
					},
					{
						name: "Vivek Modi",
						image: "static/img/vivek_modi.jpg",
						github_id: "modihere"
					}
				]
			}
		}
  },
  created () {
    this.$emit('hideloader', true)
  },
  components: {
		Card,
		CardTestimonial,
		LinksPage
  }
}
</script>
