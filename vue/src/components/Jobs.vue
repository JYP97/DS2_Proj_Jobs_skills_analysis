<template>
  <div class="job">
    <h2>{{test}}</h2>
    <transition
      name="animate__animated animate__bounce"
      enter-active-class="animate__fadeInLeft"
    >
      <div class="job_titles" v-show="searched">
        <el-table
          :data="jobDict"
          border
          style="width: 100%">
          <el-table-column
            prop="id"
            label="No."
            width="60">
          </el-table-column>
          <el-table-column
            prop="title"
            label="Job Title">
<!--            width="350">-->
          </el-table-column>
          <el-table-column
            label="Detail"
            width="63">
            <template slot-scope="scope">
              <el-button @click="getCard(scope.row)" type="text" size="small">Check</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </transition>
      <div>
        <transition
          name="animate__animated animate__bounce"
          enter-active-class="animate__fadeInRight"
          leave-active-class="animate__fadeOut"
        >
          <el-card class="job_card" v-show="searched & check">
            <div slot="header" class="clearfix">
              <span class="card_title">{{card['Title']}}</span>
              <el-button style="float: right; padding: 3px 0" type="text">Visit</el-button>
            </div>
            <div v-for="(k, v) in card" :key="v" class="text item">
              <!--          {{v}} &#45;&#45; {{k}}-->
              <el-divider v-if="v !== 'Title'" content-position="left">{{v}}</el-divider>
              <div v-if="v !== 'Title'" class="card_content">{{k}}</div>
            </div>
          </el-card>
        </transition>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Jobs',
  data () {
    return {
      url_nameko: 'http://127.0.0.1:8000/job',
      test: null,
      check: false,
      card: {'Title': '',
        'Description': '',
        'Skills': '',
        'Company': '',
        'Locality': '',
        'Address': '',
        'Salary': ''}
    }
  },
  methods: {
    getCard (data) {
      this.check = false
      axios.post(this.url_nameko, {'request': data.title})
        .then((res) => {
          this.request = res.config.data
          this.card = res.data.response
          this.check = true
          // this.response = this.response.split(',')
        }).catch(err => {
          this.response = err
        })
    }
  },
  computed: {
    jobDict () {
      var arr = []
      for (const i in this.jobList) {
        arr.push({id: parseInt(i) + 1, title: this.jobList[i]})
      }
      return arr
    }
  },
  props: ['searched', 'jobList']
}
</script>

<style scoped>
.job{
  background-color: #b7ffff;
  width: 90%;
  height: 50%;
  max-width:100%
}
body{
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}
/*div{*/
/*  background-color: #42b983;*/
/*}*/
.job_titles{
  position: absolute;
  height: 70%;
  width: 35%;
  top: 20%;
  left: 5%;
}
.job_card{
  position: absolute;
  height: 70%;
  width: 35%;
  top: 20%;
  right:15%;
}
.card_title{
  color: cornflowerblue;
  font-style: normal;
  font-weight: bold;
}
.card_content{
  color: #475669;
  font-style: normal;
  font-size: small;
}
</style>
