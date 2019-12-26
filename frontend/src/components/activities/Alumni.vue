<template>
  <div>

  	<div class="text-center verticaly-center">
  		<div class="modal-content">
	        <div class="modal-header">
	          <h5 style="color:black;" class="modal-title" id="mhrdModal">You are leaving www.nitdgp.ac.in</h5>
	          <button type="button" class="close"  v-on:click="redirectpage" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
	        </div>
	        <div class="modal-body" style="color:black;">
	          Are you sure you want to go to www.alumnitdgp.in
	        </div>
	        <div class="modal-footer">
	          <button type="button" v-on:click="redirectpage" class="btn btn-primary">Stay Here</button>
	          <a v-on:click="redirectpagealumnipage" class="btn btn-danger">Go There</a>
	        </div>
	      </div>
  	</div>
	
	  
	</div>
</template>

<script>
export default {
  created () {
    //window.location.href = "http://alumni.nitdgp.ac.in"
    this.$emit('hideloader', true)
  },
  methods:{
  	redirectpage:function(e){
  		window.location.href = "http://nitdgp.ac.in"
  	},
  	redirectpagealumnipage:function(e){
  		window.location.href = "http://alumnitdgp.in"
  	}
  }
}
</script>
<style scoped>
	.verticaly-center{
		position: relative;
		left: 50%;
		top: 50%;
		transform: translate(-50%, -50%);
		margin-top: 120px;
		width: 80%;

	}
</style>