<template>
  <div class="hello">
    <welcome :searched="searched"></welcome>
    <search @table="getSkills" @firstStep="next"></search>
    <!--    <SkillSelection v-show="searched" :skills="skills"></SkillSelection>-->
  </div>
</template>

<script>
/* eslint-disable */
import Welcome from "../components/Welcome.vue";
import Search from "../components/Search.vue";
import SkillSelection from "./SkillSelection.vue";

export default {
  name: 'MainPage',
  data () {return {
    searched: false,
    skills: null
  }},
  methods: {
    next(){
      this.searched = true
    },
    getSkills(data){
      this.skills = data
    }
  },
  components: {
    Welcome,
    Search,
    SkillSelection
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
body{
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}
</style>
