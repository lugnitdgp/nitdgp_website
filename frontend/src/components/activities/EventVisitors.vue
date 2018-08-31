<template>
  <links-page>
    <card title="Visitors">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row">
            <div class="col black-text" v-for="visitor in visitors">
              <card-testimonial :image="visitor.image" :name="visitor.name"
                :desig="visitor.designation">
                <strong>{{ visitor.event_name }}</strong><br>
              </card-testimonial>
            </div>
          </div>
        </div>
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