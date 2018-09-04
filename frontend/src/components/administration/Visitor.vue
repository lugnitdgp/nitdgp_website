<template>
  <links-page>
    <card title="Visitor">
      <div align="center">         
        <h5 style="color:black;">You are leaving www.nitdgp.ac.in</h5>
        Are you sure you want to go to {{visitor.name}}<br/>
        <a href='/' class="btn btn-primary">Stay Here</a>
        <a :href="visitor.link" class="btn btn-danger">Go There</a>
      </div>
    </card>
  </links-page>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'

export default {
  name: 'Visitor',
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
