<template>
  <div>
    <div class="page-content-container l0">
      <div class="all-tiles">
        <!-- Big row of sections -->
        <div v-for="row in results" class="row big-row">
          <!-- A section -->
          <div v-for="section in row" class="col big-col">
            <div :class="['card card-cascade narrower card-' + section.priority]">
              <div class="view gradient-card-header tile-title">
                <p class="tile-title-text">{{ section.section_name }}</p>
              </div>
              <div class="card-body text-center">
                <!-- A row of tiles -->
                <div v-for="tile_row in section.contents" class="row">
                  <!-- A tile -->
                  <div v-for="tile in tile_row" class="col tile-small">
                    <a :href="tile.link">
                      <div align="center" class="tile-content">
                        <i :class="['fa fa-2x ' + tile.icon]"></i></br>
                        <p class="tile-small-text">{{ tile.name }}</p>
                      </div>
                    </a>
                  </div>
                  <!-- End of a tile -->
                </div>
                <!-- End of a row of tiles -->
              </div>
            </div>
          </div>
          <!-- End of a section -->
        </div>
        <!-- End of big row of sections -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home',
  data () {
    return {
      results: {},
      errors: []
    }
  },
  created() {
    axios.get('http://172.16.20.3:8000/dashboard')
         .then(response => {
           this.results = response.data.results;
           let x = 0, y = 0
           let section_rows = [[]]
           // Loop over all the sections
           this.results.map((element, index) => {
             let row = 0, col = 0
             let tiles_rows = []
             // Loop over the tiles of a section
             element.contents.map((tile) => {
               // Go to the next row when a new tile row value has been encountered.
               // Reset the col value and initialize the new row with an empty list.
               if (row != tile.row) {
                 row++
                 col = 0
                 tiles_rows[row-1] = []
               }
               tiles_rows[row-1][col++] = tile
             })
             element.contents = tiles_rows
             section_rows[x][y++] = element
             // Go to next row after 3 elements. Increment the x value, reset the y
             // value and initialize the next row with an empty list.
             if ((index+1) % 3 == 0) {
               x++, y = 0
               section_rows[x] = []
             }
           })
           this.results = section_rows
         })
         .catch(e => {
           this.errors.push(e)
           console.log(errors)
         })
  }
}
</script>

<style scoped>

</style>
