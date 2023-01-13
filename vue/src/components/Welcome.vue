<template>
  <div class="hello">
    <transition
      name="animate__animated animate__bounce"
      leave-active-class="animate__fadeOutUp"
    >
      <img class="logo" v-show="!searched" src="../assets/yyds_tb.png">
    </transition>
    <transition
      name="animate__animated animate__bounce"
      enter-active-class="animate__fadeInUp"
    >
      <img class="logo_mini" v-show="searched" src="../assets/yyds_tb.png">
    </transition>

    <transition
      name="animate__animated animate__bounce"
      enter-active-class=animate__fadeIn
    >
      <div v-show="searched">
        <el-divider class="line"></el-divider>
      </div>
    </transition>

    <h4 class="powered">Powered by Vue.js</h4>
    <transition-group
      name="animate__animated animate__bounce"
      leave-active-class="animate__fadeOut"
    >
      <img class="find" key="1" v-show="!searched" src="../assets/find.png">
      <el-carousel class="ads" key="2" v-show="!searched" :interval="4000" type="card" height="280px">
        <el-carousel-item v-for="(image, index) in ad" :key="index">
          <div>
            <img class="ad" :src="image.img"/>
            <div class="ad_title">{{image.title}}</div>
          </div>
        </el-carousel-item>
      </el-carousel>
    </transition-group>
  </div>

</template>

<script>
export default {
  name: 'Welcome',
  data () {
    return {
      msg: [
        'Find',
        'in the YYDS portal'
      ],
      ad: [
        {
          img: require('../assets/ASQ_Certified.png'),
          title: 'ASQ Certified'
        },
        {
          img: require('../assets/NET_Framework.png'),
          title: '.NET Framework'
        },
        {
          img: require('../assets/24-7_Services.jpg'),
          title: '24/7 Services'
        },
        {
          img: require('../assets/3D_Modeling.jpeg'),
          title: '3D Modeling'
        },
        {
          img: require('../assets/A-B_Testing.png'),
          title: 'A/B Testing'
        },
        {
          img: require('../assets/AMT_Asset_Management_Software.jpg'),
          title: 'AMAP'
        }
      ]
    }
  },
  props: ['searched']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/*div{*/
/*  background-color: darkorange;*/
/*}*/
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
.hello{
  width: 70%;
}
.logo{
  position: absolute;
  height: 400px;
  width: 400px;
  top: 0%;
  left: 37%;
}
.logo_mini{
  position: absolute;
  height: 200px;
  width: 200px;
  top: -3%;
  left: 5%;
}
.line{
  position: absolute;
  width: 80%;
  top: 13%;
}
.powered{
  position: absolute;
  left: 45%;
  top: 94%;
  color: darkgray;
}
.find{
  position: absolute;
  left: 41%;
  top: 35%;
  color: cornflowerblue ;
}

.ads{
  position: absolute;
  left: 23%;
  top: 60%;
  width: 50%;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}
.el-carousel__item:nth-child(2n) {
  background-color: #aec6ff;
}
.el-carousel__item:nth-child(2n+1) {
  background-color: #b7ffff;
}
.ad{
  position: absolute;
  height: 90%;
  width: 96%;
  top: 3%;
  left: 2%;
}
.ad_title{
  position: absolute;
  height: 60%;
  width: 80%;
  top: 93%;
  left: 10%;
  color: cornflowerblue;
}
</style>
