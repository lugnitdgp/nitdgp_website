<template>
  <links-page>
    <card title="Information">
      <ul>
        <li v-for="info in infos">
          <a target="new" :href="info.link">
            {{ info.title }}
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
  name: "Moreinfo",
  data () {
    return {
      infos: [
        {
          link: "http://nitdgp.ac.in/information/List%20of%20MoUs%20all-1.xlsx",
          title: "List of MoUs"
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
