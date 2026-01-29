<template>
  <div id="rose-chart">
    <div class="rose-chart-title">攻击方法分布</div>
    <dv-charts :option="option" />
  </div>
</template>

<script>
export default {
  name: 'RoseChart',
  data() {
    return {
      option: {}
    }
  },
  methods: {
    createData() {
      const { randomExtend } = this

      this.option = {
        series: [
          {
            type: 'pie',
            radius: '50%',
            roseSort: false,
            data: [
              { name: 'FGM', value: randomExtend(40, 70) },
              { name: 'BIM', value: randomExtend(20, 30) },
              { name: 'PGD', value: randomExtend(10, 50) },
              { name: '随机剪裁', value: randomExtend(5, 20) },
              { name: '随机旋转', value: randomExtend(40, 50) },
              { name: '失真', value: randomExtend(20, 30) },
              { name: '噪声变换', value: randomExtend(5, 10) },
              { name: 'C&W', value: randomExtend(20, 35) },
              { name: 'Deepfool', value: randomExtend(5, 10) }
            ],
            insideLabel: {
              show: false
            },
            outsideLabel: {
              formatter: '{name} {percent}%',
              labelLineEndLength: 20,
              style: {
                fill: '#fff'
              },
              labelLineStyle: {
                stroke: '#fff'
              }
            },
            roseType: true
          }
        ],
        color: ['#da2f00', '#fa3600', '#ff4411', '#ff724c', '#541200', '#801b00', '#a02200', '#5d1400', '#b72700']
      }
    },
    randomExtend(minNum, maxNum) {
      if (arguments.length === 1) {
        return parseInt(Math.random() * minNum + 1, 10)
      } else {
        return parseInt(Math.random() * (maxNum - minNum + 1) + minNum, 10)
      }
    }
  },
  mounted() {
    const { createData } = this

    createData()

    setInterval(createData, 30000)
  }
}
</script>

<style lang="less">
#rose-chart {
  width: 30%;
  height: 100%;
  background-color: rgba(6, 30, 93, 0.5);
  border-top: 2px solid rgba(1, 153, 209, .5);
  box-sizing: border-box;

  .rose-chart-title {
    height: 50px;
    font-weight: bold;
    text-indent: 20px;
    font-size: 20px;
    display: flex;
    align-items: center;
  }

  .dv-charts-container {
    height: calc(~"100% - 50px");
  }
}
</style>
