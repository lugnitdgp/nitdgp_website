<template>
  <links-page>
    <card title="Convocation Images">
      <!-- <iframe width="1280" height="720" src="https://www.youtube.com/embed/C1_mK81r7jA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe> -->
      <collapse-list>
        <card-collapse v-for="images,key in image_sets" :title="key.split('-')[0]">
          <div class="row" style="margin:0 auto;">
            <div class="col" v-for="image in images">
              <img :src="'https://nitdgp.ac.in/convocation-images/' + key + '/' + image" class="imageview img img-responsive" />
            </div>
          </div>
        </card-collapse>
      </collapse-list>
    </card>
  </links-page>
</template>

<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import CollapseList from '@/components/CollapseList'
import CardCollapse from '@/components/CardCollapse'
import axios from 'axios'
import { genBackendURL } from '@/common.js'

export default {
  name: 'Liveconvocation',
  data() {
    return {
      image_sets:{},
    }
  },
  created () {
    axios.get(genBackendURL("convocation-links/4"))
         .then(response=>{
           this.image_sets= response.data
           console.log(response.data)
         })
    this.$emit('hideloader', true)
  },
  components: {
    LinksPage,
    Card,
    CollapseList,
    CardCollapse
  }
}
</script>
<style scoped>
  .col{
    padding:0;
    text-align: center;
  }
  .imageview{
    height:95%;
    border:3px solid #cad;
    border-radius:8px;
  }
  @media screen and (max-width: 1010px)  {
    .imageview{
      height:70%;
    }
  }
</style>
