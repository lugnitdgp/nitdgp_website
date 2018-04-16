<template>
	<links-page>
		<card title="Web Team">
			<div class="carousel-inner person-list" role="listbox">
	      <div class="carousel-item active">
	        <div class="row">
						<div class="col" v-for="person in webteam.people">
							<card-testimonial :name="person.name" :image="person.image" :desig="person.designation">
								<!-- <strong>-- Research Interest --</strong><br>
								<span v-html="stripDesc(person.research_interest)"></span><br>
								<i class="fa fa-envelope"></i><br>
								<strong>{{ person.email }}</strong><br>
								<i class="fa fa-address-book"></i><br>
								<strong>+91-{{ person.mobile }}</strong></br>
								<span class="grey-text">Joined the Institute in {{ person.joining_year }}
								</span> -->
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
						name: "Dr. Saravanan Chandran",
						image: "",
						designation: "Faculty in Charge"
					},
					{
						name: "Abhishek Prasad",
						image: "",
						designation: "Developer"
					},
					{
						name: "Ankan Poddar",
						image: "",
						designation: "Developer"
					},
					{
						name: "Arnav",
						image: "",
						designation: "Developer"
					},
					{
						name: "Devansh Goenka",
						image: "",
						designation: "Developer"
					},
					{
						name: "Divyanshu Mehta",
						image: "",
						designation: "Developer"
					},
					{
						name: "Vivek Modi",
						image: "",
						designation: "Developer"
					},
					{
						name: "Parul Chandel",
						image: "",
						designation: "Developer"
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
