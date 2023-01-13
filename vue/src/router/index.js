import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
// import MainPage from '@/pages/MainPage'
// import Result from "@/pages/Result.vue"

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }
    // {
    //   path: '/main',
    //   name: 'MainPage',
    //   component: MainPage
    // }
    // {
    //   path: '/result',
    //   name: 'Result',
    //   component: Result
    // }
  ]
})
