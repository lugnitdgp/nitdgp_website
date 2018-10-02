<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text">Outreach</a>
      <div class="card-body outr">
				<div class="text-center"><img src="/static/img/nitdgp_logo.png" width="100px" height="100px"></div>
				<div class="text-center">
					<h2>National Institute of Technology Durgapur</h2>
					<p><u><h3>List of Memorandum of Understanding (MoU)</h3></u></p>
				</div>
				<div v-for="category,category_name in outreach">
					<h2>{{category_name}}</h2>
					<table class="table table-bordered tbl">
						<thead>
							<td>Sl. No.</td>
							<td>Name of {{category_name}}</td>
							<td>Details of MoU</td>
						</thead>
						<tr v-for="(row,index) in category">
							<td>{{index+1}}</td>
							<td style="text-align: center;"><div class="text-center"><img :src="row.icon" width="100px" height="100px"/></div>{{ row.name }}</td>
							<td><a :href="row.mou">Click Here</a></td>
						</tr>	
					</table>
					<br/>
				</div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import TableRenderer from '@/components/TableRenderer'
import { genBackendURL, stripDesc, convertNewsfeed } from '@/common.js'

export default {
  name: 'Outreach',
	data() {
		return {
			outreach: {}
		}
	},
  created () {
		axios.get(genBackendURL("activities/outreach"))
         .then(response => {
					 this.outreach = response.data.outreach
					 console.log(this.outreach)
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
	},
	methods: {
    genBackendURL: genBackendURL,
	},
	components: {
    TableRenderer
  }
}
</script>
