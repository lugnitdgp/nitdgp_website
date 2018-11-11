<template>
  <links-page>
    <card title="Live Convocation">
      <div align="center">
      <iframe width="1280" height="720" src="https://youtu.be/C1_mK81r7jA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
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
