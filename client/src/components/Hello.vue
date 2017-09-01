<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <el-input placeholder="请输入username" icon="search" v-model="username" @keydown.enter.native="handleMsg" :on-icon-click="handleMsg">
    </el-input>
  </div>
</template>

<script>
export default {
  name: 'hello',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
      username: ''
    }
  },
  methods: {
    handleMsg() {
      this.axios.get(this.api.account.welcome, {
        params: {
          username: this.username
        }
      })
        .then((response) => {
          this.$message.success(response.data.msg)
          this.msg = response.data.msg;
        })
        .catch((error) => {
          this.$message.error(error.toString());

        });
    }
  }, mounted() {
    // this.handleMsg();
    this.$nextTick(function() {
    });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
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
.hello .el-input{
  width: 400px
}
</style>
