<template>
  <div class="page-content-container l1-dep">
    <!-- all-tiles -->
    <div class="all-tiles row big-row">
      <div class="col big-col card card-cascade narrower card-2">
        <div class="view gradient-card-header tile-title">
          <p class="tile-title-text">Departments</p>
        </div>
        <div class="card-body">
          <!-- Row -->
          <div v-for="row in departments" class="row">
            <!-- Col -->
            <div v-for="col in row" class="col tile-small">
              <!-- Tile -->
              <a :href="getDeptURL(col.short_code)">
                <div class="tile-content" align="center">
                  <i class="fa fa-2x">{{ col.short_code }}</i>
                  <br>
                  <p class="tile-small-text">{{ col.name }}</p>
                </div>
              </a>
              <!-- Tile -->
            </div>
            <!-- /Col -->
          </div>
          <!-- /Row -->
        </div>
      </div>
    </div>
    <!--/all-tiles-->
  </div>
</template>

<script>
import axios from 'axios'
import { baseURL, genBackendURL } from '@/common.js'

export default {
  name: 'Departments',
  data () {
    return {
      departments: []
    }
  },
  methods: {
    getDeptURL: function (short_code) {
      return baseURL + '/department/' + short_code;
    }
  },
  created () {
    axios.get(genBackendURL('department'))
         .then(response => {
           let res = response.data.results

           // i counts the total Departments, j counts the total number of rows
           // and k counts the number of Departments in a row
           let i = 0, j = 0, k = 0

           // This structure will be followed for laying out the departments
           let structure = [3, 3, 4, 4, 4, 4, 4]

           let row = []
           while (i < res.length) {
             // Don't display the Administrative Department
             if (res[i].name != "Administrative") {
               row.push(res[i])
               k++
               if (k == structure[j]) {
                 this.departments.push(row)
                 row = []
                 k = 0
                 j++
               }
             }
             i++
           }
           this.departments.push(row)
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  }
}
</script>
