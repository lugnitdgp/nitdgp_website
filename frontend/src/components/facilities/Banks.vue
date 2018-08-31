<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text">Banks</a>
      <div class="card-body">
        <ul>
          <li><a href="#">State Bank of India NIT Durgapur Branch</a></li>
          <li><a href="#">Canara Bank</a></li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Banks',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>
