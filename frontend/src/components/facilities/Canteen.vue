<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text">Canteens &amp; Cafes</a>
      <div class="card-body">
        <ul>
          <li><a href="#">Hall 5 Canteen</a></li>
          <li><a href="#">B/L Cafe</a></li>
          <li><a href="#">Wonder Cafe</a></li>
          <li><a href="#">Nescafe</a></li>
          <li><a href="#">Roy Resteraunt</a></li>
          <li><a href="#">Chitrangani</a></li>
          <li><a href="#">Chandu Tea Stall</a></li>
          <li><a href="#">Techno</a></li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Canteen',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>