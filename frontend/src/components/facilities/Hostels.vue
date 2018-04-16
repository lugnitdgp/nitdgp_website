<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text">Hostels</a>
      <div class="card-body">
      	<ul>
          <li><a href="#">Hall 1 - Netaji Subhas Hall</a></li>
          <li><a href="#">Hall 2 - J.C. Bose Hall</a></li>
          <li><a href="#">Hall 3 - Tagore Hall </a></li>
          <li><a href="#">Hall 4 - C.V. Raman Hall</a></li>
          <li><a href="#">Hall 5 - Vivekananda Hall</a></li>
          <li><a href="#">Hall 6 - Aurobindo Hall</a></li>
          <li><a href="#">Hall 7 - Sister Nivedita Hall</a></li>
          <li><a href="#">Hall 8 - Preetilata Hall</a></li>
          <li><a href="#">Hall 9 - Satyendra Nath Bose Hall</a></li>
          <li><a href="#">Hall 10 - XXX HALL</a></li>
          <li><a href="#">Hall 11 - XXX HALL</a></li>
          <li><a href="#">Hall 12 - XXX HALL</a></li>
          <li><a href="#">Hall 13 - XXX HALL</a></li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Hostels',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>