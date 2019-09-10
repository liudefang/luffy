<template>
    <div>
      <h1>课程列表</h1>
      <ul v-for="row in courseList">
        <li>{{row.title}}</li>
      </ul>
    </div>
</template>

<script>
    export default {
        name: "course",
        data(){
          return {
            msg:'course',
            courseList:[

            ]
          }
        },
      // 页面加载时自动执行
      mounted:function () {
          this.initCourse()

      },
      methods:{
          initCourse:function () {
            // 通过ajax向接口发动请求，并获取课程列表
            // axios 可以发ajax请求 npm install axios --save
            // 1. 在main.js中配置
            // 2. 使用axios发送请求
          var that = this


          this.$axios.request({
            url: 'http://127.0.0.1:8000/api/v1/course/',
            method: 'GET'

          }).then(function (ret) {
            // ajax请求发送成功后，获得的响应内容
            // ret.data
            if(ret.data.code==0){
              that.courseList = ret.data.data

            }
            else {
              alert('获取数据失败')
            }

          }).catch(function (ret) {
            // ajax请求失败后，获取响应的内容

          })

          }
      }
    }
</script>

<style scoped>

</style>
