<template>
  <div>
    <div class="page-content-container l0">
      <div class="all-tiles">
        <div v-for="(row,index) in results" class="row big-row">
          <div v-for="section in row" class="col big-col">
            <div :class="['card card-cascade narrower card-' + section.priority]">
              <div class="view gradient-card-header tile-title">
                  <p class="tile-title-text">{{ section.section_name }}</p>
              </div>
              <div class="card-body text-center">
                <div v-for="tile_row in section.contents" class="row">
                  <div v-for="tile in tile_row" class="col tile-small">
                    <a :href="tile.link">
                      <div align="center" class="tile-content">
                        <i :class="['fa fa-2x ' + tile.icon]"></i></br>
                        <p class="tile-small-text">{{ tile.name }}</p>
                      </div>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
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
      let x = 0, y = 0;
      let rows = [[]]
      this.results.map((element, index) => {
        let prev = 0;
        let r = 0;
        let tiles = [];
        element.contents.map((tile, tile_index) => {
          if (prev != tile.row) {
            ++prev, r = 0;
            tiles[prev-1] = [];
          }
          tiles[prev-1][r] = tile;
          r++;
        });
        element.contents = tiles;
        rows[x][y] = element;
        y++;
        if ((index+1) % 3 == 0) {
          x++, y = 0;
          rows[x] = [];
        }
      });
      this.results = rows;
      console.log(this.results);
    })
    .catch(e => {
      this.errors.push(e)
    })
  }
}
</script>

<style scoped>

</style>
