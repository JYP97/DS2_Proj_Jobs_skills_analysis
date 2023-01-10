<template>
  <div class="hello">
          <form>
            <input type="text" placeholder="Please input your skills" v-model="s.description">
            <button @click="searched"> search </button>  <br/>
          </form>
    <div v-show="this.s.searched">
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import Vue from 'vue'

export default {
  name: 'Search',
  data () {
    return {
      url_postman: 'https://bff6ffdf-132c-4abb-8ab3-f6b03dd94e5b.mock.pstmn.io/description',
      url_nameko: 'http://127.0.0.1:8000/skill',
      user_name: 'haozhe',
      password: 'haozhe',
      client: null,
      request: '',
      response: '',
      s: {
        description: '',
        searched: false
      }
    }
  },
  methods: {
    searched () {
      this.s.searched = true

      axios.post(this.url_nameko, {'request': this.s.description})
        .then((res) => {
          this.request = res.config.data
          this.response = res.data.response
          this.response = this.response.split(',')
          this.$emit('table', this.response)
          this.$emit('firstStep', this.s.searched)
        }).catch(err => {
          this.response = err
        })
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
