<template>
  <links-page>
    <card title="Continuing Education Cell">
      <div>
        <h3><p class="text-center"> Page Under Constraction</p></h3>
      </div>
    </card>
    <card title="Contact">
      <div class="text-center" style="line-height: .5em;">
        <h3  style="line-height: .5em;">Prof. Kartik Chandra Ghanta</h3> <br>
        <h5  style="line-height: .5em;">kartik.ghanta@che.nitdgp.ac.in</h5><br>
        <h5  style="line-height: .5em;">+91-9434788020</h5><br>
      </div>
    </card>
    <card title="TEQIP">
      <div>
        <ul class="list-group list-gr">
          <li><a href="/teqip" class="list-group-item">Click here...</a></li>
        </ul>
      </div>
    </card>
    
  </links-page>
</template>
<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'

export default {
  name: 'Cec',
  data () {
    return {
      
    }
  },
  created () {
    this.$emit('hideloader', true)
  },
  components: {
    LinksPage,
    Card
  }

}
</script>
