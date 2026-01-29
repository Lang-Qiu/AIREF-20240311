<template>
  <div class="banner">
      <div class="content clearfix">
        <div class="left">
          <slot name="title"></slot>
          <slot name="text"></slot>
          <router-link to="/modelassess/sketch">
            <slot name="btn"></slot>
          </router-link>
        </div>
        <div class="right">
          <slot name="image"></slot>
        </div>
      </div>
    </div>
</template>

<script>
export default {
    name: 'BannerIndex'
}
</script>

<style lang="less" scoped>
.clearfix::after {
  content: "";
  display: table;
  clear: both;
}
.banner {
  height: 300px;
  .content {
    width: 1200px;
    margin: 0 auto;
    .left {
      width: 600px;
      float: left;
      text-align: left;
      h1 {
        padding-top: 80px;
      }
      p {
        line-height: 25px;
        padding-top: 30px;
      }
      a {
        text-decoration: none;
      }
      
    }
    .right {
      width: 600px;
      float: left;
      img {
        width: 300px;
        margin: 28px auto;
      }
    }
  }
}
</style>