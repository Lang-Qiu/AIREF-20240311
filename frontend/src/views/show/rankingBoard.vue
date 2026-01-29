<template>
  <div id="ranking-board">
    <div class="ranking-board-title">后门网络记录数量</div>
    <dv-scroll-ranking-board :config="config" />
  </div>
</template>

<script>
export default {
  name: 'RankingBoard',
  data() {
    return {
      config: {
        data: [
          {
            name: 'Blend',
            value: 55
          },
          {
            name: 'BadNet',
            value: 120
          },
          {
            name: 'WaNet',
            value: 78
          },
          {
            name: 'SIG',
            value: 66
          },
          {
            name: 'Label Consistent',
            value: 80
          },
          {
            name: 'Refool',
            value: 45
          },
          {
            name: 'SSBA',
            value: 29
          },
          {
            name: 'Low Frequency',
            value: 29
          },
        ],
        rowNum: 8
      }
    }
  }
}
</script>

<style lang="less">
#ranking-board {
  width: 20%;
  box-shadow: 0 0 3px blue;
  display: flex;
  flex-direction: column;
  background-color: rgba(6, 30, 93, 0.5);
  border-top: 2px solid rgba(1, 153, 209, .5);
  box-sizing: border-box;
  padding: 0px 30px;

  .ranking-board-title {
    font-weight: bold;
    height: 50px;
    display: flex;
    align-items: center;
    font-size: 20px;
  }

  .dv-scroll-ranking-board {
    flex: 1;
  }
}
</style>
