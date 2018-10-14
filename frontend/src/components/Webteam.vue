<template>
  <links-page>
    <card title="Web Team">
      <div class="row">
        <card-testimonial v-for="(person, i) in webteam.people" :key="i"
          class="card-webteam"
          :name="person.name"
          :image="person.image"
          :desig="'Batch of '+person.passing_year">
          <!-- <i class="fa fa-github fa-lg"></i> -->
          <!-- <a :href="'https://github.com/' + person.github_id">{{ person.github_id }}</a> -->
          GLUG Member
        </card-testimonial>
      </div>
    </card>
  </links-page>
</template>

<script>
import axios from 'axios'
import Card from '@/components/Card'
import CardTestimonial from '@/components/CardTestimonial'
import LinksPage from '@/components/LinksPage'

export default {
  name: 'Webteam',
  data () {
    return {
      webteam: {
        people: [
          {
            name: "Adarsh Singh",
            image: "static/img/adarsh-singh.jpg",
            github_id: "nxtbig",
            passing_year: 2018
          },
          {
            name: "Arka Roy",
            image: "static/img/arka-roy.jpeg",
            github_id: "arka-nitd",
            passing_year: 2018
          },
          {
            name: "Bishakh Ghosh",
            image: "static/img/bishak-ghosh.jpeg",
            github_id: "ghoshbishakh",
            passing_year: 2018
          },
          {
            name: "Abhishek Prasad",
            image: "static/img/abhishek_prasad.jpg",
            github_id: "Compro-Prasad",
            passing_year: 2019
          },
          {
            name: "Arnav",
            image: "static/img/arnav_kumar.jpg",
            github_id: "arnav-amb",
            passing_year: 2019
          },
          {
            name: "Devansh Goenka",
            image: "static/img/devansh_goenka.jpeg",
            github_id: "devanshgoenka97",
            passing_year: 2019
          },
          {
            name: "Divyanshu Mehta",
            image: "static/img/divyanshu_mehta.jpg",
            github_id: "divyanshumehta",
            passing_year: 2019
          },
          {
            name: "Vivek Modi",
            image: "static/img/vivek_modi.jpg",
            github_id: "modihere",
            passing_year: 2019
          },
          {
            name: "Ankan Poddar",
            image: "static/img/ankan_poddar.jpg",
            github_id: "ankan17",
            passing_year: 2020
          },
          {
            name: "Parul Chandel",
            image: "static/img/parul-chandel.jpeg",
            github_id: "Deathrow77",
            passing_year: 2020
          }
        ]
      }
    }
  },
  created () {
    this.$emit('hideloader', true)
  },
  components: {
    Card,
    CardTestimonial,
    LinksPage
  }
}
</script>

<style>
  .card-webteam {
    min-width: 250px !important;
    min-height: 200px !important;
    max-width: 500px !important;
    max-height: 400px !important;
    padding: 10px !important;
  }
</style>
