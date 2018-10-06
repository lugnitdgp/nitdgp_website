<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text">Centre of Excellence in Advanced Materials</a>
      <div class="card-body">
        <div class="card-text">
          <ul>
            <li><a target="new" href="http://nitdgp.ac.in/AllPDF/Centre of Excellence in Advanced Materials-home.pdf">CEAM home</a></li>
            <li><a target="new" href="http://nitdgp.ac.in/AllPDF/coe-converted.pdf">CEAM Doc</a></li>
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
