<template>
  <div class="l1 page-type-links notices">
    <div class="card">
      <a class="card-header white-text">Notices</a>
      <div class="card-body">
      	<!-- Nav tabs -->
      	<ul class="nav nav-tabs nav-justified not-tab">
      	  <li class="nav-item">
      	    <a class="nav-link active" data-toggle="tab" href="#panel1" role="tab">Academic</a>
      	  </li>
      	  <li class="nav-item">
      	    <a class="nav-link" data-toggle="tab" href="#panel2" role="tab">Student</a>
      	  </li>
      	  <li class="nav-item">
      	    <a class="nav-link" data-toggle="tab" href="#panel3" role="tab">General</a>
      	  </li>
      	</ul>
      	<!-- Tab panels -->
      	<div class="tab-content card">
      	  <!--Panel 1-->
      	  <div class="tab-pane fade in show active" id="panel1" role="tabpanel">
      	    <ul v-if="academic">
      	      <li v-for="notice in academic">
                <a :href="notice.file" target="new">{{ notice.title }}</a>
              </li>
      	    </ul>
      	    <div>
      	      <ul v-if="academic" class="pagination justify-content-center">
      	        <li class="page-item">
      	          <a class="page-link" aria-label="Previous">
      	            <span aria-hidden="true">&laquo;</span>
      	            <span class="sr-only">Previous</span>
      	          </a>
      	        </li>

      	        <li v-for="i in parseInt(academic.length/10 + 1)"
                    class="'page-item ' + i == 1 : 'active' ? ''" >
                      <a class="page-link" data-toggle="tab"
                         href="'#li' + i" role="tab">{{i}}</a>
                </li>

      	        <li class="page-item">
      	          <a class="page-link" aria-label="Next">
      	            <span aria-hidden="true">&raquo;</span>
      	            <span class="sr-only">Next</span>
      	          </a>
      	        </li>
      	      </ul>
      	    </div>
      	  </div>
      	  <!--/.Panel 1-->
      	  <!--Panel 2-->
      	  <div class="tab-pane fade" id="panel2" role="tabpanel">
            <ul v-if="student">
              <li v-for="notice in student">
                <a :href="notice.file" target="new">{{ notice.title }}</a>
              </li>
            </ul>
      	    <div>
      	      <ul  v-if="student" class="pagination justify-content-center">
      	        <li class="page-item">
      	          <a class="page-link" aria-label="Previous">
      	            <span aria-hidden="true">&laquo;</span>
      	            <span class="sr-only">Previous</span>
      	          </a>
      	        </li>

                <li v-for="i in parseInt(student.length/10 + 1)"
                    class="'page-item ' + i == 1 : 'active' ? ''" >
                      <a class="page-link" data-toggle="tab"
                         href="'#li' + i" role="tab">{{i}}</a>
                </li>

      	        <li class="page-item">
      	          <a class="page-link" aria-label="Next">
      	            <span aria-hidden="true">&raquo;</span>
      	            <span class="sr-only">Next</span>
      	          </a>
      	        </li>
      	      </ul>
      	    </div>
      	  </div>
      	  <!--/.Panel 2-->
      	  <!--Panel 3-->
      	  <div class="tab-pane fade" id="panel3" role="tabpanel">
      	    <br>
            <ul v-if="general">
              <li v-for="notice in general">
                <a :href="notice.file" target="new">{{ notice.title }}</a>
              </li>
            </ul>
      	    <div>
      	      <ul v-if="general" class="pagination justify-content-center">
      	        <li class="page-item">
      	          <a class="page-link" aria-label="Previous">
      	            <span aria-hidden="true">&laquo;</span>
      	            <span class="sr-only">Previous</span>
      	          </a>
      	        </li>

                <li v-for="i in parseInt(general.length/10 + 1)"
                    class="'page-item ' + i == 1 : 'active' ? ''" >
                      <a class="page-link" data-toggle="tab"
                         href="'#li' + i" role="tab">{{i}}</a>
                </li>

      	        <li class="page-item">
      	          <a class="page-link" aria-label="Next">
      	            <span aria-hidden="true">&raquo;</span>
      	            <span class="sr-only">Next</span>
      	          </a>
      	        </li>
      	      </ul>
      	    </div>
      	  </div>
      	  <!--/.Panel 3-->
      	</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { genBackendURL } from '@/common.js'

export default {
  name: 'Notices',
  data() {
    return {
      academic: [],
      student: [],
      general: []
    }
  },
  created () {
    axios.get(genBackendURL('academics/notices'))
         .then(response => {
           this.academic = response.data.notices.academic
           this.student = response.data.notices.student
           this.general = response.data.notices.general
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
}
</script>
