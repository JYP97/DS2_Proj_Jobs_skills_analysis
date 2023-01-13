<template>
  <div class="hello">
    <form>
      <transition-group
        name="animate__animated animate__bounce"
        leave-active-class="animate__fadeOutUp"
      >
        <el-input class="search_box" type="text" key="1" v-show="!searched" v-model="s.description" placeholder="Please input your skills in order of proficiency"></el-input>
        <el-button class="search_button" @click="search" type="primary" key="2" v-show="!searched" icon="el-icon-search">Search</el-button>
      </transition-group>
      <transition-group
        name="animate__animated animate__bounce"
        enter-active-class="animate__fadeInUp"
      >
        <el-input class="search_box_result" type="text" key="1" v-show="searched" v-model="s.description" placeholder="Please input your skills in order of proficiency"></el-input>
        <el-button class="search_button_result" @click="search" type="primary" key="2" v-show="searched" icon="el-icon-search">Search</el-button>
      </transition-group>
      <br/><br/>
      <transition
        name="animate__animated animate__bounce"
        leave-active-class="animate__fadeOut"
      >
        <div class="number_bar" v-show="!searched">
          <span class="desc_bar">Job Titles</span>
          <el-slider
            v-model="s.number"
            :step="1"
            :min="1"
            :max="10"
            show-stops>
          </el-slider>
        </div>
      </transition>
      <br/><br/>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
// import 'animate.css'
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
      searched: false,
      s: {
        description: '',
        number: 5
      }
    }
  },
  methods: {
    search () {
      this.searched = true

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
body{
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}
.search_box{
  width: 50%;
  max_width: 550px;
  position: absolute;
  left: 20%;
  top: 45%;
}
.search_box_result{
  width: 50%;
  max_width: 550px;
  position: absolute;
  left: 20%;
  top: 7%;
}
.search_button{
  position: absolute;
  left: 70%;
  top: 45%;
}
.search_button_result{
  position: absolute;
  left: 70%;
  top: 7%;
}
.search_cascader{
  max_width: 550px;
}
.number_bar{
  position: absolute;
  width: 45%;
  left: 30%;
  top: 53%;
}
.desc_bar{
  position: absolute;
  left: -17%;
  top: 25%;
  color: cornflowerblue;
}
</style>
