<template>
	<links-page>
		<card title="History">
		    <p style="text-align: justify;">
                        The National Institute of Technology, Durgapur (formerly Regional Engineering College, Durgapur), was established by an Act of Parliament in 1960 as one of the eight such colleges aimed to function as a pace setter for engineering education in the country and to foster national integration.It is a fully-funded premier Technological Institution of the Government of India and is administered by an autonomous Board of Governors. The Institute is a University which awards B.Tech., M.C.A., M.Sc., M.B.A.,M.Tech. and Ph.D. degrees to students after their successful completion of the specified courses. The Institute imparts education in the disciplines of Chemical Engineering, Civil Engineering, Computer Science and Engineering, Electrical Engineering, Electronics and Communication Engineering, Mechanical Engineering, Metallurgical and Materials Engineering,Information Technology, Biotechnology, Physics, Chemistry, Mathematics, Environmental science, Materials Science and Management Studies. As decided by the Ministry of Human Resource Development, Government of India, the procedure for selection of candidates for admission to the Bachelor Degree Courses in Engineering/Technology in National Institute of Technology Durgapur and in other NITs is on the basis of State Rank/ All India Rank (AIR) of AIEEE conducted by Central Board of Secondary Education, New Delhi, and the same is executed through counselling by Central Counselling Board, AIEEE under guidance from MHRD, GOI as per schedule notified by CCB. In addition to the normal intake, a few seats are reserved for Foreign Students who are nominated by the Ministry of External Affairs, Government of India, and the Indian Council for Cultural Relations, Government of India.
                    </p>
		</card>
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
  name: 'History',
  created () {
    this.$emit('hideloader', true)
  },
  components: {
  	LinksPage,
  	Card
  }
}
</script>
