<template>
  <div class="hello">
    <welcome></welcome>
    <search @table="getSkills" @firstStep="next"></search>
    <SkillSelection v-show="first" :skills="skills"></SkillSelection>
  </div>
</template>

<script>
/* eslint-disable */
import Welcome from "../components/Welcome.vue";
import Search from "../components/Search.vue";
import SkillSelection from "./SkillSelection.vue";

export default {
  name: 'HelloWorld',
  data () {return {
    first: false,
    skills: null
  }},
  methods: {
    next(){
      this.first = true
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
</style>
