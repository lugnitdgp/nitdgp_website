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
              <a :href="'http://172.16.20.3:4567/department/' + col.id">
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

export default {
  name: 'Departments',
  data () {
    return {
      departments: []
    }
  },
  created () {
    axios.get('http://172.16.20.3:8000/department?format=json')
         .then(response => {
           let res = response.data.results
           let j = 0, i = 0
           let row = [res[0]]
           for (i = 1; i < (4 - (res.length % 4)) * 3; i++) {
             row.push(res[i])
             if ((i + 1) % 3 == 0) {
               this.departments.push(row)
               row = []
             }
           }
           for (; i < res.length; i++) {
             let x = res.length - i - 1
             row.push(res[i])
             if (x % 4 == 0) {
               this.departments.push(row)
               row = []
             }
           }
         })
         .catch(e => {
           console.log(e)
         })
  }
}
</script>
