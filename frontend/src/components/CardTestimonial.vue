<template>
  <div class="card testimonial-card">
    <div class="card-up">
    </div>
    <img :src="image" class="avatar mx-auto rounded-circle img-fluid">
    <div class="card-body-in">
      <h4 class="card-title mt-1"><strong>{{ name }}</strong></h4>
      <strong>{{ desig }}</strong>
      <br>
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
  props: {
    image: {
      type: String,
      required: true,
      default: "https://google.com/logo.png"
    },
    name: {
      type: String,
      required: true,
      default: "Ram Potter"
    },
    desig: {
      type: String,
      required: false,
      default: ""
    }
  }
}
</script>
