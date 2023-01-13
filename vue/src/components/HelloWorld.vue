<template>
  <div class="hello">
    <welcome :searched="searched"></welcome>
    <search @table="getJobs" @firstStep="next"></search>
    <jobs :searched="searched" :jobList="jobList"></jobs>
  </div>
</template>

<script>
/* eslint-disable */
import Welcome from "../components/Welcome.vue";
import Search from "../components/Search.vue";
import SkillSelection from "./SkillSelection.vue";
import Jobs from "./Jobs.vue";

export default {
  name: 'HelloWorld',
  data () {return {
    searched: false,
    jobList: null
  }},
  methods: {
    next(){
      this.searched = true
    },
    getJobs(data){
      this.jobList = data
    }
  },
  components: {
    Jobs,
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
