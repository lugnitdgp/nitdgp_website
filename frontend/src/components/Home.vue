<template>
  <div style="margin-top: 160px">
    <div class="row newscaro">
      <div v-if="(windowWidth > 1000)" class="col-8 caro">
        <Carousel :slides="slides"></Carousel>
      </div>
      <div class="col-4 news">
        <Newsfeed :notices="notices"></Newsfeed>
      </div>
    </div>
    <div class="l0">
      <div class="all-tiles">
        <!-- Big row of sections -->
        <div v-for="row in results" class="row big-row">
          <!-- A section -->
          <div v-for="section in row" class="col big-col">
            <sp-card-collapse bodyclass="text-center" show="false"
              :containerclass="'card-' + section.priority">
              <p slot="header" class="tile-title-text">
                <span style="float: left; width:80%; text-align:left">
                  {{ section.section_name }}
                </span>
                <i style="float:right; width:20%; text-align:right; margin-top:-10px" class="fa fa-chevron-down" aria-hidden="true"></i>
              </p>
              <div v-for="tile_row in section.contents" class="row">
                <small-tile v-for="tile in tile_row"
                  :icon="tile.icon"
                  :desc="tile.name"
                  :link="link(tile,section.section_name)"
                  :key="tile.name" />
              </div>
            </sp-card-collapse>
          </div>
        </div>
        <!-- End of a section -->
      </div>
      <!-- End of big row of sections -->
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
import { genBackendURL, convertNewsfeed } from '@/common.js'
import Carousel from './Carousel'
import Newsfeed from './Newsfeed'
import SmallTile from './SmallTile'
import SpCardCollapse from './SpCardCollapse'

export default {
  name: 'Home',
  components: {
    Carousel,
    Newsfeed,
    SmallTile,
    SpCardCollapse
  },
  data () {
    return {
      results: {},
      slides: [],
      notices: [],
      windowWidth: 1000
    }
  },
  created() {
    let count_axios = 0
    axios.get(genBackendURL('dashboard'))
         .then(response => {
           var struct = [0,1,11,111,1111,1121,2121,2122,2222,2232,3232,3323,3333,3343,3344,4434,4444];
           this.results = response.data.results
           let x = 0, y = 0
           let section_rows = []
           section_rows[0] = []
           section_rows[1] = []
           let group_up=0
           let group_dw=0
           let inp = JSON.parse(JSON.stringify(this.results))
           inp.map((element,index) => {
              let cur_inp = element.contents
              cur_inp.sort(function(a,b){
                  return (a.name > b.name) ? 1 : ((b.name > a.name) ? -1 : 0);
              })
              let tiles_rows = []
              let div =  struct[cur_inp.length]
              let it = -1
              let row = 0
              while(div!=0)
              {
                let curr_div = div%10;
                div = Math.floor(div/10);
                let col = 0
                tiles_rows[row] = []
                while(curr_div--)
                  tiles_rows[row][col++]=cur_inp[++it]
                row++
              }
              element.contents = tiles_rows
              if(index<=2)
                section_rows[0][group_up++] = element
              else
                section_rows[1][group_dw++] = element
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
           this.notices = convertNewsfeed(response.data.results)
           if (count_axios == 2) {
             this.$emit('hideloader', true)
           }
           count_axios++
         })
         .catch(e => {
           console.log(e)
         })
    window.addEventListener('resize', this.updateWidth)
    this.windowWidth = document.body.clientWidth
  },
  methods: {
    genBackendURL,
    updateWidth () {
      this.windowWidth = document.body.clientWidth
    },
    link (tile,section) {
      // For generating links on the frontend
      let link = '/'
      let suburl = tile.name.toLowerCase().replace(/ /g, "");
      //if (suburl.indexOf("event") != -1)
      //  return link + "events"
      if (suburl.indexOf("notice") != -1) {
        if(section == "Academics")
          return link + "notices/" + "academic"
        if(section == "Students & Alumni")
          return link + "notices/" + "student"
        if(section == "Information")
          return link + "notices/" + "general"
        }
        // return link + "notices/"
      if (suburl.indexOf("bwc") != -1)
        return link + "bwcifc"
      return link + suburl
    }
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateWidth);
  }
}
</script>

<style scoped>
</style>
