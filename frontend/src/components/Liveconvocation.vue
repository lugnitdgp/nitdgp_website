<template>
  <links-page>
    <card title="15th Convocation Still Pictures">
      <collapse-list>
        <card-collapse v-for="(images,key,i) in image_sets" :title="key.split('-')[0]" :key="i">
          <div class="row" style="margin:0 auto;">
            <div class="col" v-for="(image,index) in images" :key="index">
              <a :href="'https://nitdgp.ac.in/convocation-photos/'+key.split('-')[0] + '/' + image"
                :download="key.split('-')[0] + '-' + image"
                @contextmenu.prevent="">
                <img :src="'https://nitdgp.ac.in/convocation-photos/' + key + '/' + image" :alt="image" class="imageview" />
              </a>
            </div>
          </div>
        </card-collapse>
      </collapse-list>
      <!--<table width="100%"  border="1">
        <tr>
          <td>
          <div align="center">
            <iframe width="1280" height="720" src="https://www.youtube.com/embed/vL8dL6DQxVc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div></td>
        </tr>
      </table>-->
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
    axios.get(genBackendURL("convocation-links/10"))
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
