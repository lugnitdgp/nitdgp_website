<template>
  <div>
    <div class="row newscaro">
      <div class="col-8 caro">
        <Carousel :slides="slides"></Carousel>
      </div>
      <div class="col-4 news">
        <Newsfeed :notices="notices"></Newsfeed>
      </div>
    </div>
    <div class="page-content-container l0 mob">
      <div class="all-tiles">
        <!-- Big row of sections -->
        <div v-for="row in results" class="row big-row">
          <!-- A section -->
          <div v-for="section in row" class="col big-col">
            <div :class="['card card-cascade narrower card-' + section.priority]">
              <a data-toggle="collapse" :href="'#collapse'+section.section_name">
                <div class="view gradient-card-header tile-title">
                <p class="tile-title-text">{{ section.section_name }}</p>
                </div>
              </a>
              <div class="card-body text-center collapse" :id="'collapse'+section.section_name">
                <div v-for="tile_row in section.contents" class="row">
                  <small-tile v-for="tile in tile_row"
                    :icon="tile.icon"
                    :desc="tile.name"
                    :link="link(tile)"
                    :key="tile.name" />
                </div>
              </div>
            </div>
          </div>
          <!-- End of a section -->
        </div>
        <!-- End of big row of sections -->
      </div>
    </div>
    <div class="page-content-container l0 brow">
      <div class="all-tiles">
        <!-- Big row of sections -->
        <div v-for="row in results" class="row big-row">
          <!-- A section -->
          <div v-for="section in row" class="col big-col">
            <div :class="['card card-cascade narrower card-' + section.priority]">
              <a data-toggle="collapse" :href="'#collapse1'+section.section_name">
                <div class="view gradient-card-header tile-title">
                <p class="tile-title-text">{{ section.section_name }}</p>
                </div>
              </a>
              <div class="card-body text-center collapse show" :id="'collapse1'+section.section_name">
                <!-- A row of tiles -->
                <div v-for="tile_row in section.contents" class="row">
                  <!-- A tile -->
                  <small-tile v-for="tile in tile_row"
                    :icon="tile.icon"
                    :desc="tile.name"
                    :link="link(tile)"
                    :key="tile.name" />
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
import axios from 'axios'
import { genBackendURL } from '@/common.js'

import Carousel from './Carousel';
import Newsfeed from './Newsfeed';
import SmallTile from './SmallTile';

export default {
  name: 'Home',
  components: {
    Carousel,
    Newsfeed,
    SmallTile
  },
  data () {
    return {
      results: {},
      slides: [],
      notices: []
    }
  },
  created() {
    let count_axios = 0
    axios.get(genBackendURL('dashboard'))
         .then(response => {
           this.results = response.data.results
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
           if (count_axios == 2) {
             this.$emit('hideloader', true)
           }
           count_axios++
         })
         .catch(e => {
           console.log(e)
         })
    axios.get(genBackendURL('dashboard/carousel'))
         .then(response => {
           this.slides = response.data.results
           if (count_axios == 2) {
             this.$emit('hideloader', true)
           }
           count_axios++
         })
         .catch(e => {
           console.log(e)
         })
    axios.get(genBackendURL('dashboard/newsfeed'))
         .then(response => {
           this.notices = response.data.results
           const months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUNE", "JULY",
                           "AUG", "SEPT", "OCT", "NOV", "DEC"]
           let notices = []
           let news_slide = []
           this.notices.map((news,index) => {
             let date = new Date(news.date)
             news.month = months[date.getMonth()]
             news.date = date.getDate()
             news_slide.push(news)
             if ((index+1) % 4 == 0) {
               notices.push(news_slide)
               news_slide = []
               this.slides_count++
             }
           })
           if (news_slide.length) {
             notices.push(news_slide)
             this.slides_count++
           }
           this.notices = notices
           if (count_axios == 2) {
             this.$emit('hideloader', true)
           }
           count_axios++
         })
         .catch(e => {
           console.log(e)
         })
  },
  methods: {
    genBackendURL,
    link (tile) {
      // For generating links on the frontend
      let link = '/'
      let suburl = tile.name.toLowerCase().replace(/ /g, "");
      if (suburl.indexOf("event") != -1)
        return link + "events"
      if (suburl.indexOf("bwc") != -1)
        return link + "bwcifc"
      return link + suburl
      // For getting links from backend
      // return tile.link
    }
  }
}
</script>

<style scoped>

</style>
