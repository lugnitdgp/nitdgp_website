<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text">Centre of Excellence in Advanced Materials</a>
      <div class="card-body">
        <div class="card-text">
          <ul>
            <li><a target="new" href="http://nitdgp.ac.in/all_pdf17/Centre%20of%20Excellence%20in%20Advanced%20Materials-home.pdf">CEAM home</a></li>
            <li><a target="new" href="http://nitdgp.ac.in/research/coe/images/coe.doc">CEAM Doc</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Ceam',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>