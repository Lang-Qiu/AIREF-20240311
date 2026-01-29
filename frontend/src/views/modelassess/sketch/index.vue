<template>
    <div>
        <div class="sketch">
            <div class="main">
                <div class="left">
                    <img src="../../../assets/sketch.jpg" alt="">
                    
                   
                </div>
                
                <!-- <div class="right">
                    <t-menu theme="light" defaultValue="dashboard" style="margin-right: 40px" height="550px" @change="changeHandler">
                        <template #logo>
                            <img height="28" src="../../../assets/logo.png" alt="logo" />
                        </template>
                        
                            <t-menu-item value="second" >
                                <template #icon>
                                    <icon name="image" />
                                </template>
                                图像模型评估
                            </t-menu-item>
                        
                        
                            <t-menu-item value="third" >
                                <template #icon>
                                <icon name="textbox" />
                                </template>
                                文本模型评估
                            </t-menu-item>
                        
                        
                            <t-menu-item value="fourth" >
                                <template #icon>
                                <icon name="audio" />
                                </template>
                                音频模型评估
                            </t-menu-item>
                        
                        
                            <t-menu-item value="fifth" >
                                <template #icon>
                                <icon name="play-rectangle" />
                                </template>
                                视频模型评估
                            </t-menu-item>
                        
                            <t-menu-item value="sixth" >
                                <template #icon>
                                <icon name="table" />
                                </template>
                                表格模型评估
                            </t-menu-item>
                        
                            <t-menu-item value="seventh" >
                                <template #icon>
                                <icon name="book-open" />
                                </template>
                                知识图谱评估
                            </t-menu-item>
                        
                            <t-menu-item value="eight" >
                                <template #icon>
                                <icon name="hotspot-wave" />
                                </template>
                                强化学习评估
                            </t-menu-item>
                        
                        
                    </t-menu>
                    
                </div> -->
            </div>
        </div>
        <div class="sketch_f">
            <h1 style="margin: 100px 0 50px 0;font-size: 40px;" >产品框架</h1>
            <img src="../../../assets/sketch_f.png" alt="" style="margin-bottom: 30px;">
        </div>
    </div>
  </template>
  
  <script>
//   import { Icon } from 'tdesign-icons-vue'
  export default {
    name: 'SketchIndex',
    components: {
        // Icon,
    },
    methods: {
       
        changeHandler(active) {
            console.log('change', active);
            this.$bus.$emit('changeActiveName', active)
            if (active === 'first') {
            this.$router.push('/modelassess/sketch')
            } else if (active === 'second') {
            this.$router.push('/modelassess/image/data')
            } else if (active === 'third') {
            this.$router.push('/modelassess/text/data')
            } else if (active === 'fourth') {
            this.$router.push('/modelassess/audio/data')
            } else if (active === 'fifth') {
            this.$router.push('/modelassess/visual/data')
            } else if (active === 'sixth') {
            this.$router.push('/modelassess/tab/data')
            } else if (active === 'seventh') {
            this.$router.push('/modelassess/knowledge/data')
            } else if (active === 'eight') {
            this.$router.push('/modelassess/reinforce/data')
            }
        },
    },
    mounted() {
                
    }
}
  </script>
  
  <style lang="less" scoped>
    .sketch {
        // background: url('../../../assets/guodu.jpg') no-repeat;
        background-size: 100% 100%;
        .main {
            // display: flex;
            // width: 1200px;
            // margin: 0 auto;
            .left {
                // width: 600px;
                // display: flex;
                // flex-direction: column;
                // justify-content: center;
                align-items: center;
                img {
                    width: 100%;
                    height: 500px;
                    // height: 400px;
                    // text-align: center;
                }
            }
            // .right {
            //     width: 600px;
            //     display: flex;
            //     flex-direction: column;
            //     justify-content: space-around;
            //     align-items: center;
            // }
        }
    }
    .common {
        width: 200px;
        height: 80px;
        text-align: center;
        line-height: 80px;
        color: #54a9ff;
        border-radius: 20px;
        border: 2px solid #54a9ff;
        margin: 15px 0;        
    }
    .middle_p {
        width: 150px;
        height: 150px;
        text-align: center;
        line-height: 150px;
        color: #54a9ff;
        border-radius: 75px;
        border: 2px solid #54a9ff;     
    }
    
  </style>