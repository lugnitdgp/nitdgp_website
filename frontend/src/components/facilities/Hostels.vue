<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text">Hostels</a>
      <div class="card-body">
      	<ul>
          <li v-for="hostel in hostels"><a href="#">{{hostel.name}}</a></li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { range, genBackendURL } from "@/common.js";
export default {
  name: "Hostels",
  data() {
    return {
      hostels: {}
    };
  },
  created() {
    axios
      .get(genBackendURL("facilities/hostels/"))
      .then(response => {
        this.hostels = response.data.results;
        this.$emit("hideloader", true);
      })
      .catch(e => {
        console.log(e);
      });
  },
  methods: {
    range: range
  }
};
</script>