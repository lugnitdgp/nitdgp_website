<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text">NIT Durgapur Post Office</a>
      <div class="card-body">
        Address - Address: A-Zone, Durgapur, West Bengal 713209
        Phone: 1800 11 2011
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Po',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>
