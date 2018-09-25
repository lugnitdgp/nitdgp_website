<template>
	<div class="l1 page-type-links">
    <div class="card">
      <a class="card-header white-text">Holidays</a>
      <div class="card-body content">
        <ul>
          <li><a href="https://old.nitdgp.ac.in/information/Office%20Notice/Holidays_2018.pdf" target="new">List of holidays in the year 2018</a></li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Holidays',
  data () {
  },
  created () {
    this.$emit('hideloader', true)
  },
  components: {
  }
}
</script>
