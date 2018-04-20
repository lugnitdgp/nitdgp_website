<template>
  <div class="card testimonial-card">
    <div class="card-up">
    </div>
    <a :href="'/faculty/' + id">
      <img :src="imageModified" class="avatar mx-auto rounded-circle img-fluid">
    </a>
    <div class="card-body-in">
      <p class="card-title">
        <a class="black-text" :href="'/faculty/' + id">
          {{ name }}
        </a>
      </p>
      <h6 class="blue-text"><strong>{{ desig }}</strong></h6>
      <hr>
      <p class="min-profile">
        <slot></slot>
      </p>
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
