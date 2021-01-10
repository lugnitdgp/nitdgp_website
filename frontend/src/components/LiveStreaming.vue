<template>
  <links-page>
    <card title="16th Convocation Live Streaming">
    	
      	<div class="sociallink" v-if="timeDiff<=0">
      		<span><a href="https://www.youtube.com/channel/UC1svhZpnCQ1OoqYiMnhh-3g" target="_new">Youtube Link</a></span>
      		<span><a href="https://www.facebook.com/nitdgpofficial" target="_new">Facebook Link</a></span>
      		<span><a href="https://www.moodle.nitdgp.ac.in" target="_new">Moodle Link</a></span>
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
      <!--<table width="100%"  border="1">
        <tr>
          <td>
          <div align="center">
            <iframe width="1280" height="720" src="https://www.youtube.com/embed/vL8dL6DQxVc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div></td>
        </tr>
      </table>-->
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
        var countDownDate = new Date('January 12, 2021 10:20:00');
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
  	align-items: center;
  	justify-content: center;
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
