<template>
	<div class="l1 page-type-links">
    <div class="card">
        <a class="card-header white-text">Minutes of IFC Meeting</a>
        <div class="card-body">
            <div class="card-text">
              <ul>
                <li> <a href="http://nitdgp.ac.in/information/FC_Meetings/Minutes of 43rd FC meeting.pdf" target=_blank> Minutes of the 43rd FC Meeting</a></li>
                <li> <a href="http://nitdgp.ac.in/information/FC_Meetings/Agenda of 43rd FC Meeting.pdf" target=_blank> Agenda of the 43rd FC Meeting</a></li>
              </ul>
            </div>
        </div>
    </div>
    <div class="card">
        <a class="card-header white-text">Minutes of BWC Meeting</a>
        <div class="card-body">
            <div class="card-text">
                <ul>
                    <li> <a href="http://nitdgp.ac.in/information/BWC_Meetings/BWC_3_MINUTES.pdf" target=_blank>Minutes of the 3rd BWC Meeting</a></li>
                    <li> <a href="http://nitdgp.ac.in/information/BWC_Meetings/BWC_1_MINUTES.pdf" target=_blank>Minutes of the 1st BWC Meeting</a></li>
                </ul>
            </div>
        </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Bwcifc',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>