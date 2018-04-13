<template>
  <div class="page-content-container l1-dep">
    <div class="all-tiles row big-row">
      <sp-card containerclass="col big-col card-2">
        <p slot="header" class="tile-title-text">Departments</p>
        <div v-for="row in departments" class="row">
          <small-tile v-for="col in row"
            :title="col.short_code"
            :desc="col.name"
            :link="getDeptURL(col.short_code)"
            :key="col.short_code" />
        </div>
      </sp-card>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SmallTile from '@/components/SmallTile'
import SpCard from '@/components/SpCard'
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
  },
  components: {
    SmallTile,
    SpCard
  }
}
</script>
