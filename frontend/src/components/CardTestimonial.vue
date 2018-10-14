<template>
  <div class="col testimonial">
    <div class="card testimonial-card text-center">
      <div class="card-up">
      </div>
      <a v-if="id" align="center" :href="'/faculty/' + id">
        <img :src="imageModified" class="avatar mx-auto rounded-circle img-fluid">
      </a>
      <div v-if="!id" align="center">
        <img :src="imageModified" class="avatar mx-auto rounded-circle img-fluid">
      </div>
      <div class="card-body-in">
        <p v-if="id" class="card-title">
          <strong>
            <a class="blue-text notranslate" :href="'/faculty/' + id">
              {{ name }}
            </a>
          </strong>
        </p>
        <p v-if="!id" class="card-title notranslate">
          {{ name }}
        </p>
        <h6 class="black-text">{{ desig }}</h6>
        <hr>
        <p class="min-profile">
          <slot></slot>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CardTestimonial",
  data() {
    return {
      imageModified: this.image === null ? 'https://newsdesk.si.edu/sites/default/files/imagecache/photo_pagewidth/photos/anonymous_silhouette.jpg' : this.image
    }
  },
  props: ['image', 'name', 'desig', 'id'],
}
</script>

<style>
  .col.testimonial {
    min-width: 200px;
    min-height: 100px;
    max-width: 320px;
    max-height: 500px;
    padding: 7px;
  }
  .min-profile {
    font-size: 72% !important;
  }
  hr {
    margin-left: 2em !important;
    margin-right: 2em !important;
  }
  .card-body-in .card-title .notranslate {
    font-size: 88% !important;
  }
  .card-body-in h6{
    font-size: 80% !important;
  }
  .testimonial-card .desig{
    font-size: 100%;
  }
  .testimonial-card .card-title{
    font-size: 100%;
  }
  .testimonial-card {
    min-height: 100% !important;
    min-width: 100% !important;
  }
  .card-up {
    height: 80px !important;
  }
  .card-up {
    background: linear-gradient(to right,#001333,#324e7d) !important;
  }
  .avatar {
    height: 100px !important;
    width: 100px !important;
  }
</style>
