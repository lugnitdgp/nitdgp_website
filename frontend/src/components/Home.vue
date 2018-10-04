<template>
  <div style="margin-top: 80px">
    <div class="row newscaro">
      <div v-if="(windowWidth > 1000)" class="col-8 caro">
        <Carousel :slides="slides"></Carousel>
      </div>
      <div class="col-4 news">
        <Newsfeed :notices="notices"></Newsfeed>
      </div>
    </div>
    <div class="l0 brow">
      <div class="all-tiles">
        <!-- Big row of sections -->
        <div v-for="(row,row_index) in results" class="row big-row">
          <!-- A section -->
          <div v-for="section in row" class="col big-col">
            <sp-card-collapse bodyclass="text-center" :show="false"
              :containerclass="'card-' + section.priority" :row_index="row_index">
              <p slot="header" class="tile-title-text">
                <span>
                  {{ section.section_name }}
                </span>
                <i style="float:right; text-align:right; margin-top:-10px" class="fa fa-chevron-down" aria-hidden="true"></i>
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
    <div class="l0 mobi">
      <div class="all-tiles">
        <!-- Big row of sections -->
        <div v-for="row in results" class="row big-row">
          <!-- A section -->
          <div v-for="section in row" class="col big-col">
            <sp-card-collapse2 bodyclass="text-center" show="false"
              :containerclass="'card-' + section.priority">
              <p slot="header" class="tile-title-text">
                <span>
                  {{ section.section_name }}
                </span>
                <i style="float:right; text-align:right; margin-top:-10px" class="fa fa-chevron-down" aria-hidden="true"></i>
              </p>
              <div v-for="tile_row in section.contents" class="row">
                <small-tile v-for="tile in tile_row"
                  :icon="tile.icon"
                  :desc="tile.name"
                  :link="link(tile,section.section_name)"
                  :key="tile.name" />
              </div>
            </sp-card-collapse2>
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
import SpCardCollapse2 from './SpCardCollapse2'

export default {
  name: 'Home',
  components: {
    Carousel,
    Newsfeed,
    SmallTile,
    SpCardCollapse,
    SpCardCollapse2
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
              // Custom logic for Facilities Section
              if(element.section_name == 'Facilities') {
                let libindex = 0      // Index of Library tile
                cur_inp.map((tile,tindex) => {
                  if(tile.name == 'Library')
                    libindex = tindex
                })
                // Making library as the first tile
                var temp = cur_inp[0]
                cur_inp[0] = cur_inp[libindex]
                cur_inp[libindex] = temp
                // Buble Sort from index i to n-1
                var len = cur_inp.length, i, j, stop;
                for (i=1; i < len; i++){
                  for (j=1, stop=len-i; j < stop; j++){
                    if (cur_inp[j].name > cur_inp[j+1].name) {
                      temp = cur_inp[j];
                      cur_inp[j] = cur_inp[j+1];
                      cur_inp[j+1] = temp;
                    }
                  }
                }
                
              }
              else {
                cur_inp.sort(function(a,b){
                    return (a.name > b.name) ? 1 : ((b.name > a.name) ? -1 : 0);
                })
              }
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

.col-4 {
  padding-right: 0px;
}
.mobi {
  display: none;
}

@media screen and (max-width: 1010px)  {
  .brow {
    display: none;
  }
  .mobi {
    display: block !important;
  }
}
</style>
