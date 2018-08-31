<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text">Quick Links</a>
      <div class="card-body">
        <div class="row">
          <div class="col">
            <h3>Admissions</h3>
            <ul>
              <li><a href="/admission">DASA</a></li>
              <li><a href="/admission">ICCR</a></li>
              <li><a href="/admission">MEA</a></li>
              <li><a href="/admission">GATE</a></li>
              <li><a href="/admission">JEE Main</a></li>
              <li><a href="/admission">JAM</a></li>
              <li><a href="/admission">PhD</a></li>
              <li><a href="/admission">MBA</a></li>
            </ul>
          </div>
          <div class="col">
            <h3>Others</h3>
            <ul>
              <li><a href=""></a></li>
              <li><a href=""></a></li>
            </ul>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'QuickLinks',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>
<style scoped>
ul {
  text-decoration: none;
}
</style>