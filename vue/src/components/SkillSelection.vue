<template>
  <div>
    <h3>{{info[0]}}</h3>
    <h4>{{info[1]}}</h4>
    <div v-for="(s, index) of s.skillList" :key="index" v-if="!s.selected">
      {{s.title}} - {{index}} <button @click="s.selected=true">select</button>
    </div>
    <h4>{{info[2]}}</h4>
    <div v-for="(s, index) of s.skillList" :key="index" v-if="s.selected">
      {{s.title}} - {{index}} <button @click="s.selected=false">delete</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SkillSelection',
  data () {
    return {
      info: [
        'Skill Selection',
        'Job Category',
        'selected'
      ],
      s: {
        category: 'c',
        skillList: [
          {id: '00', title: 's0', selected: false, priority: 0},
          {id: '01', title: 's1', selected: false, priority: 0},
          {id: '02', title: 's2', selected: false, priority: 0},
          {id: '03', title: 's3', selected: false, priority: 0},
          {id: '04', title: 's4', selected: false, priority: 0}
        ]
      }
    }
  },
  methods: {
    select () {

    }
  }
}
</script>

<style scoped>

</style>
