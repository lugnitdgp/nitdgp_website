<template>
  <div class="l1-dep">
    <div class="all-tiles row big-row">
      <sp-card containerclass="col big-col card-2">
        <p slot="header" class="tile-title-text">Departments</p>
        <div v-for="row in departments" class="row">
          <small-tile v-for="col in row"
            :title="col.short_code"
            :desc="col.name"
            :link="'/department/' + col.short_code"
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
  created () {
    axios.get(genBackendURL('department'))
         .then(response => {
           let res = response.data.results

           // i : count departments
           // j : count rows
           // k : count departments in a row
           let j = 0, k = 0

           // Numbers in the array represent: number of departments in a row
           // Length of this array represents row count
           let structure = [3, 3, 4, 4, 4, 4, 4]

           let row = []
           for (let i = 0; i < res.length; i++) {
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
