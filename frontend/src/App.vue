<template>
<div id="app">
  <Headr/>
  <router-view/>
  <Footr/>
</div>
</template>

<script>
import Headr from './components/Headr'
import Footr from './components/Footr'

export default {
    name: 'App',
    components: {
        Headr,
        Footr
    }
}
</script>

<style>
</style>
