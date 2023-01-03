<template>
  <div class="hello">
    <welcome></welcome>
    <search></search>
<!--    <AdvanceSearch></AdvanceSearch>-->
  </div>
</template>

<script>
  import Welcome from "../components/Welcome.vue";
  import Search from "../components/Search.vue";
  import AdvanceSearch from "../components/AdvanceSearch.vue";

  export default {
    name: 'MainPage',
    data () {return {
      firstStep: false
    }},
    components: {
      Welcome,
      Search,
      AdvanceSearch
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
