<template>
  <links-page>
    <card title="Deans">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row">
            <div style="min-width:100%;"><h1>Deans</h1></div>
            <card-testimonial v-for="(dean, i) in deans.deans" :key="i"
              class="black-text"
              :image="dean.image"
              :name="dean.name"
              :desig="dean.role + ' ' + dean.designation">
              <i class="fa fa-envelope"></i><br>
              <strong>{{ dean.email }}</strong><br>
              <i class="fa fa-address-book"></i><br>
              <strong>+91-{{ dean.mobile }}</strong></br>
            </card-testimonial>
          </div>
          <div class="row">
            <div style="min-width:100%;"><h1>Associate Deans</h1></div>
            <card-testimonial v-for="(dean, i) in deans.associate_deans" :key="i"
              class="black-text"
              :image="dean.image"
              :name="dean.name"
              :desig="dean.role + ' ' + dean.designation">
              <i class="fa fa-envelope"></i><br>
              <strong>{{ dean.email }}</strong><br>
              <i class="fa fa-address-book"></i><br>
              <strong>+91-{{ dean.mobile }}</strong></br>
            </card-testimonial>
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
  name: "Deans",
  data() {
    return {
      deans: {}
    };
  },
  created() {
    axios
      .get(genBackendURL("administration/deans"))
      .then(response => {
        this.deans = response.data;
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
