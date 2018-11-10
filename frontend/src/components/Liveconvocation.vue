<template>
  <links-page>
    <card title="Liveconvocation">
      <div align="center">
      <iframe width="1280" height="720" src="https://www.youtube.com/embed/p1vteg3c4zo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
      </div>
    </card>
  </links-page>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'

export default {
  name: 'Liveconvocation',
  data() {
    return {
      visitor: {
      name: 'President of India page',
      link: 'http://presidentofindia.nic.in/profile.htm'
      }
    }
  },
  created () {
    this.$emit('hideloader', true)
    // window.location = 'http://presidentofindia.nic.in/profile.htm'
  },
  components: {
    LinksPage,
    Card,
  }
}
</script>
