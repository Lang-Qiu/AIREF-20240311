<template>
  <div id="scroll-board">
    <dv-scroll-board :config="config" />
  </div>
</template>

<script>
export default {
  name: 'ScrollBoard',
  data() {
    return {
      config: {
        header: ['时间', '检测信息', '数量', '备注'],
        data: [
          ['2023-10-22 19:25:00', 'User1-WaNet', '5', '已处理'],
          ['2023-10-22 20:06:00', 'User2-BadNet', '1', '已处理'],
          ['2023-10-23 00:25:00', 'User3-BadNet', '6', '发现异常'],
          ['2023-10-22 16:25:00', 'User4-C&W', '1', '已处理'],
        ],
        index: true,
        columnWidth: [50, 170, 150],
        align: ['center'],
        rowNum: 7,
        headerBGC: '#1981f6',
        headerHeight: 45,
        oddRowBGC: 'rgba(0, 44, 81, 0.8)',
        evenRowBGC: 'rgba(10, 29, 50, 0.8)'
      }
    }
  }
}
</script>

<style lang="less">
#scroll-board {
  width: 50%;
  box-sizing: border-box;
  margin-left: 20px;
  height: 100%;
  overflow: hidden;
}
</style>
