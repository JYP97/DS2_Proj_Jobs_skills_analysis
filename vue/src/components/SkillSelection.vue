<template>
  <div>
    <h3>{{info[0]}}</h3>
    <h4>{{info[1]}}</h4>
    <div v-for="(skill) of skillList" :key="skill.id" v-if="!skill.selected">
      {{skill.title}} <button @click="selectSkill($event, skill.id)">select</button>
    </div>
    <h4>{{info[2]}}</h4>
    <div v-for="(skill) of filSkillList" :key="skill.id" v-if="skill.selected">
      {{skill.title}} <button @click="deleteSkill($event, skill.id)">delete</button>
    </div>
    <h2>{{s.selectedNum}}</h2>
    <button @click="clean">clean</button>  <button @click="confirm">confirm</button>
    <h3>request: {{request}}</h3>
    <h3>response: {{response}}</h3>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SkillSelection',
  data () {
    return {
      url_postman: 'https://9a34e925-01f5-470d-a68c-9fa1159931a4.mock.pstmn.io/selection',
      url_nameko: 'http://127.0.0.1:8000/job',
      request: null,
      response: null,
      info: [
        'Skill Selection',
        'Skill Category',
        'selected'
      ],
      s: {
        category: 'c',
        selectedNum: 0
      }
    }
  },
  methods: {
    selectSkill (event, index) {
      this.skillList[index].selected = true
      this.s.selectedNum++
      this.skillList[index].priority = this.s.selectedNum
    },
    deleteSkill (event, index) {
      this.skillList[index].selected = false
      this.s.selectedNum--
      var priority = this.skillList[index].priority
      console.log(priority)
      this.skillList[index].priority = 0
      for (let i in this.skillList) {
        if (this.skillList[i].priority > priority) this.skillList[i].priority--
      }
    },
    clean () {
      for (let i in this.skillList) {
        this.skillList[i].priority = 0
        this.skillList[i].selected = false
        this.s.selectedNum = 0
      }
    },
    confirm () {
      axios.post(this.url_nameko, {'request': JSON.stringify(this.filSkillList)})
        .then((res) => {
          this.request = res.config.data
          this.response = res.data.response
        }).catch(err => {
          this.response = err
        })
    }
  },
  computed: {
    // selectedList: [],
    skillList () {
      var arr = []
      for (const i in this.skills) {
        // var idx = new Number(i)
        arr.push({id: parseInt(i), title: this.skills[i], selected: false, priority: 0})
      }
      return arr
    },
    filSkillList () {
      const arr = this.skillList.filter((skill) => {
        return skill.priority > 0
      })

      console.log(this.s.selectedNum)

      arr.sort((s1, s2) => {
        return s1.priority - s2.priority
      })

      return arr
    }
  },
  props: ['skills']
}
</script>

<style scoped>

</style>
