<template>
	<div class="l1 page-type-links">
    <div class="card">
      <a class="card-header white-text">Policies</a>
      <div class="card-body content">
        <ul>
          <li><a href="#" target="new">Copyright Policy</a></li>
          <li><a href="#" target="new">Privacy Policy</a></li>
          <li><a href="#" target="new">Hyperlinking Policy</a></li>
          <li><a href="#" target="new">Monitoring Policy</a></li>
          <li><a href="#" target="new">Web manager Policy</a></li>
          <li><a href="#" target="new">Terms and Conditions</a></li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Policies',
  data () {
  },
  created () {
    this.$emit('hideloader', true)
  },
  components: {
  }
}
</script>
