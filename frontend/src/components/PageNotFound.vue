<template>
  <div style="margin-top: 120px;min-height: 420px;">
    <div class="img-container">
      <img alt="NIT Durgapur Logo" src="/static/img/nitdgp_logo.png" />
    </div>
    <h4 align="center">Oops! Seems like you are at a wrong page!</h4>
    <h4 align="center">Head back to <a href="/">home.</a></h4>
  </div>
</template>

<script>
export default {
  name: 'PageNotFound',
  created() {
    this.$emit('hideloader', true)
  }
}
</script>

<style scoped>
  div.img-container {
    text-align: center;
    margin-top: 1em;
    margin-bottom: 2.5em;
  }
  img {
    height: 120px;
  }
  h4 {
    margin-top: 0.8em;
    margin-bottom: 0;
  }
  a {
    /* color:#111; */
  }
</style>
