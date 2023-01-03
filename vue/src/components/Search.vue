<template>
  <div class="hello">
          <form>
            <input type="text" placeholder="Please input your description" v-model="s.description">
            <button @click="searched"> search </button>  <br/>
          </form>
  </div>
</template>

<script>
export default {
  name: 'Search',
  data () {
    return {
      s: {
        description: '',
        searched: false
      }
    }
  },
  methods: {
    searched () {
      this.s.searched = true
      this.$emit('firstStep', this.s.searched)
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
