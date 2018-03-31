<template>
  <links-page>
    <card title="Right to Information">
      <ul>
        <li v-for="rti in rtis">
          <a target="new" :href="rti.link">
            {{ rti.title }}
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
  name: "Rti",
  data () {
    return {
      rtis: [
        {
          link: "http://nitdgp.ac.in/information/Institute%20Information%20Officer/RTI%20Act%202005.pdf",
          title: "Institute Information Officer"
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
