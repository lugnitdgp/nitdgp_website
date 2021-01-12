<template>
  <links-page>
    <card title="16th Convocation">
    	
      	<div class="sociallink" v-if="timeDiff<=0">
      		<span class="text-center"><!-- <a href="https://www.youtube.com/watch?v=rrqepcZwERI&t=781s" target="_new"> -->Youtube Recorded Video will be available soon<!-- </a> --></span>
      		<!-- <span>2.&nbsp;&nbsp;&nbsp;<a href="https://www.facebook.com/nitdgpofficial" target="_new">Facebook Live</a></span> -->
      		<!-- <span>3.&nbsp;&nbsp;&nbsp;<a href="https://teams.microsoft.com/l/meetup-join/19%3ameeting_MjFjZTBlMGUtNTYzMS00MDcyLTgwN2ItNmQxOTlmMjhiNGYx%40thread.v2/0?context=%7b%22Tid%22%3a%22a58978f7-efcb-4b53-bd81-8361fa13fa5c%22%2c%22Oid%22%3a%2228387cbc-5d0f-460c-887b-86f8054e568f%22%2c%22IsBroadcastMeeting%22%3atrue%7d" target="_new">Teams Live( Exclusively for our Students, Faculties and staffs)</a></span>
      		<span>4.&nbsp;&nbsp;&nbsp;<a href="https://web.microsoftstream.com/video/b3ea5266-d364-4962-9919-9868b7d08512" target="_new">MS Stream Live( Exclusively for our Students, Faculties and staffs)</a></span> -->
      		<!-- <span>5.&nbsp;&nbsp;&nbsp;<a href="https://moodle.nitdgp.ac.in" target="_new">Moodle Link</a></span> -->
      		<!-- <span>Microsoft Teams Link</span> -->
      	</div>

      	<div class="" v-else>
      		<p style="text-align: center;font-size:25px;color:#000;">16th Convocation Live Streaming Begins in</p>
    		<div class="comedoenwrapper">
    			<div class="smcrd">
	    			<strong>Days</strong>
	    			<span class="days">{{ time['days'] }}</span>
	    		</div>
	    		<div class="smcrd">
			    	<strong>Hours</strong>
	    			<span class="hours">{{ time['hours'] }}</span>
				</div>
				<div class="smcrd">
			    	<strong>Minutes</strong>
	    			<span class="minutes">{{ time['minutes'] }}</span>
			    </div>
			    <div class="smcrd">
			    	<strong>Seconds</strong>
	    			<span class="seconds">{{ time['seconds'] }}</span>
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
      image_sets:{},
      timeDiff: 0,
	  time: {
  		days: 0,
  		hours: 0,
  		minutes: 0,
  		seconds: 0,
	  },
    }
  },
  created () { 
  	this.countdown();   
    this.$emit('hideloader', true)
  },
  methods:{
  	countdown() {
      setTimeout(() => {
        var countDownDate = new Date('January 12, 2021 10:25:00');
          var now = new Date();
          this.timeDiff = countDownDate - now;
          this.time.days = Math.floor(this.timeDiff / (1000 * 60 * 60 * 24));
          this.time.hours = Math.floor((this.timeDiff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
          this.time.minutes = Math.floor((this.timeDiff % (1000 * 60 * 60)) / (1000 * 60));
          this.time.seconds = Math.floor((this.timeDiff % (1000 * 60)) / 1000);
        
        this.countdown()
      }, 1000)
    },
  },
  computed: {
    timeDiffComp(){
      return this.timeDiff
    },
    timeComp(){
      return this.time
    },
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
  .imageview{
    height:95%;
    border:3px solid #cad;
    border-radius:8px;

  }
  .comedoenwrapper{
  	margin: 0 auto;
  	text-align: center;
  	color: #000;
  	font-size: 25px;
  	display: flex;
  	flex-direction: row;
  	align-items: center;
  	justify-content: center;
  }
  .comedoenwrapper strong{  	
  	border-bottom: 3px solid #fff;
  	text-align: center;
  }
  .sociallink{
  	display: flex;
  	flex-direction: column;
  	align-items: left;
  	justify-content: left;
  	color: blue;
  	font-size: 25px;
  }
  .smcrd{
  	height: 100px;
  	width: 100px;
  	background: orange;
  	margin-right: 5px;
  	display: flex;
  	flex-direction: column;
  	align-items: center;
  	justify-content: center;
  }
  @media screen and (max-width: 1010px)  {
    .imageview{
      height:70%;
    }
  }
</style>
