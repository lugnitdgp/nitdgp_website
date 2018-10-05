<template>
    <ul class="">
    <li class="dropdown mega-dropdown active">
      <a class="dropdown-toggle" id="navbarDropdownMenuLink2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">QuickLinks
        <span class="sr-only">(current)</span>
      </a>
      <div class="dropdown-menu mega-menu v-2 z-depth-1 special-color py-5 px-3" aria-labelledby="navbarDropdownMenuLink2">
        <div class="row">
          <div class="col-md-6 col-xl-3 sub-menu mb-xl-0 mb-4">
            <h6 class="sub-title text-uppercase font-weight-bold white-text">Admission</h6>
            <ul class="list-unstyled">
              <li v-for="link in links['Admission']">
                <a class="menu-item pl-0" v-if="link.link" :href="link.link">{{link.title}}</a>
                <a class="menu-item pl-0" v-else :href="link.file">{{link.title}}</a>
                <br><div class="line-break">-------------------</div>
              </li>
            </ul>
          </div>
          <div class="col-md-6 col-xl-3 sub-menu mb-xl-0 mb-4">
            <h6 class="sub-title text-uppercase font-weight-bold white-text">General</h6>
            <ul class="list-unstyled">
              <li v-for="link in links['General']">
                <a class="menu-item pl-0" v-if="link.link" :href="link.link">{{link.title}}</a>
                <a class="menu-item pl-0" v-else :href="link.file">{{link.title}}</a>
                <br><div class="line-break">-------------------</div>
              </li>
            </ul>
          </div>
          <div class="col-md-6 col-xl-3 sub-menu mb-xl-0 mb-4">
            <h6 class="sub-title text-uppercase font-weight-bold white-text">National Portal</h6>
            <ul class="list-unstyled">
              <li v-for="link in links['National Portal']">
                <a class="menu-item pl-0" v-if="link.link" :href="link.link">{{link.title}}</a>
                <a class="menu-item pl-0" v-else :href="link.file">{{link.title}}</a>
                <br><div class="line-break">-------------------</div>
              </li>
            </ul>
          </div>
          <div class="col-md-6 col-xl-3 sub-menu mb-xl-0 mb-4">
            <h6 class="sub-title text-uppercase font-weight-bold white-text">Social Media</h6>
            <ul class="list-unstyled">
              <li v-for="link in links['Social Media']">
                <a class="menu-item pl-0" v-if="link.link" :href="link.link">{{link.title}}</a>
                <a class="menu-item pl-0" v-else :href="link.file">{{link.title}}</a>
                <br><div class="line-break">-------------------</div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </li>
    </ul>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import CardTestimonial from '@/components/CardTestimonial'
import { range, genBackendURL } from '@/common.js'

export default {
  name: "QuickLinks",
  data () {
    return {
      links: {}
    }
  },
  created () {
    axios.get(genBackendURL("dashboard/quick-links"))
         .then(response => {
           this.links = response.data.groups
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
  components: {
    LinksPage,
    Card,
    CardTestimonial
  }
}
</script>

<style scoped>
.col-md-6{
  padding: 5px!important;
}
.mega-menu{
  width: 500px;padding: 10px!important;
}
@media screen and (max-width: 600px){
  .mega-menu{
    width: 300px;padding: 10px!important;
  }
}
ul {
  text-decoration: none;
}
.menu-item {
  font-size: 85%
}

.line-break {
  margin: -8px auto
}
</style>