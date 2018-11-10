<template>
  <links-page>
    <card title="Live Convocation">
      <div align="center">
      <iframe width="1280" height="720" src="https://www.youtube.com/embed/p1vteg3c4zo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
      </div>
    </card>
  </links-page>
</template>

<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'

export default {
  name: 'Liveconvocation',
  data() {
    return {
      
    }
  },
  created () {
    this.$emit('hideloader', true)
    
  },
  components: {
    LinksPage,
    Card,
  }
}
</script>
