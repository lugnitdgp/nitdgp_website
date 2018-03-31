<template>
  <links-page>
    <card title="National Board of Accreditation">
      <ul>
        <li v-for="nba in nbas">
          <a target="new" :href="nba.link">
            {{ nba.title }}
          </a>
        </li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import Card from "@/components/Card"
import LinksPage from "@/components/LinksPage"

export default {
  name: "Nba",
  data () {
    return {
      nbas: [
        {
          link: "http://http//nitdgp.ac.in/information/NBA%20Data.doc",
          title: "NBA Accreditation Data"
        }
      ]
    }
  },
  created () {
    this.$emit('hideloader', true)
  },
  components: {
    Card,
    LinksPage
  }
}
</script>
