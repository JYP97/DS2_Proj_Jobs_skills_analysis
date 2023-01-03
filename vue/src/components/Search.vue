<template>
  <div class="hello">
          <form>
            <input type="text" placeholder="Please input your description" v-model="s.description">
            <button @click="searched"> search </button>  <br/>
          </form>
    <div v-show="this.s.searched">
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Search',
  data () {
    return {
      url: 'https://bff6ffdf-132c-4abb-8ab3-f6b03dd94e5b.mock.pstmn.io/description',
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
      axios.get(this.url, {params: {description: this.s.description}})
        .then(res => {
          this.request = res.config.params.description
          this.response = res.data.split(',')
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
