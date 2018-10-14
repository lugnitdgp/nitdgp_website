<template>
  <links-page>
    <card title="Visitors">
      <div class="row">
        <card-testimonial v-for="(visitor, i) in visitors" :key="i"
          class="card-visitors black-text"
          :image="visitor.image"
          :name="visitor.name"
          :desig="visitor.designation">
          <strong>{{ visitor.event_name }}</strong><br>
        </card-testimonial>
      </div>
    </card>
  </links-page>
</template>

<script>
import axios from "axios";
import LinksPage from "@/components/LinksPage";
import Card from "@/components/Card";
import CardTestimonial from "@/components/CardTestimonial";
import { range, genBackendURL } from "@/common.js";

export default {
  name: "Visitors",
  data() {
    return {
      visitors: {}
    };
  },
  created() {
    axios
      .get(genBackendURL("activities/visitors/"))
      .then(response => {
        this.visitors = response.data.results;
        this.$emit("hideloader", true);
      })
      .catch(e => {
        console.log(e);
      });
  },
  methods: {
    range: range
  },
  components: {
    LinksPage,
    Card,
    CardTestimonial
  }
};
</script>

<style>
  .card-visitors {
    min-width: 230px !important;
    min-height: 200px !important;
    max-width: 500px !important;
    max-height: 500px !important;
    padding: 10px !important;
  }
</style>
