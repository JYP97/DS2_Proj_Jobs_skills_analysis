<template>
  <div class="hello">
    <h1>{{ msg[0] }}</h1>
    <h1>{{ msg[1] }}</h1>
    <h2>Powered by Vue.js</h2>
  </div>
</template>

<script>
export default {
  name: 'Welcome',
  data () {
    return {
      msg: [
        'Welcome to YYDS',
        'Job Recommendation APP'
      ]
    }
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
