<template>
	<links-page>
		<card title="Location">
			<p style="text-align: justify;">
        The Institute is located about 160 KMs north-west of Kolkata on the Howrah-Delhi main railway route and overlooking the National Highway No. 2(the great Grand- Trunk Road). The Institute spreads over an area of 187 acres of land. It is fully residential and co-educational. At present about 2500 boys and 500 girls reside in seven boys' hostels and two girls' hostels. The annual undergraduate intake is more than 1000 students.
      </p>
		</card>
	</links-page>
</template>

<script>

import Card from "@/components/Card"
import LinksPage from "@/components/LinksPage"

export default {
  name: 'Location',
  created () {
    this.$emit('hideloader', true)
  },
  components: {
  	LinksPage,
  	Card
  }
}
</script>
