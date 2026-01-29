<template>
  <div class="gongneng">
    <h1>产品功能</h1>
    <div class="gongneng_main">
        <ul>
            <li>
                <img src="https://www.real-ai.cn/media/upload/products/icon/AutoML.svg" alt="">
                <div class="right">
                    <h1 class="title">模型综合安全评估</h1>
                    <p class="right_content">从后门攻击和对抗攻击两个方面，利用我们提出的内置的综合评估算法，给AI模型的安全综合态势打分</p>
                </div>
            </li>
            <li>
                <img src="https://www.real-ai.cn/media/upload/products/icon/AutoML.svg" alt="">
                <div class="right">
                    <h1 class="title">对抗攻击测评</h1>
                    <p class="right_content">评估ai模型在受到对抗攻击时的表现，并生成测评报告</p>
                </div>
            </li>
            <li>
                <img src="https://www.real-ai.cn/media/upload/products/icon/AutoML.svg" alt="">
                <div class="right">
                    <h1 class="title">后门检测</h1>
                    <p class="right_content">支持易于部署的模型后门检测解决方案，能够有效的检测文本，图像，语音，图谱AI模型的后门并给出检测报告</p>
                </div>
            </li>
            <li>
                <img src="https://www.real-ai.cn/media/upload/products/icon/AutoML.svg" alt="">
                <div class="right">
                    <h1 class="title">模型安全加固</h1>
                    <p class="right_content">支持用户对模型进行模型后门的清除和对抗样本的防御，提升模型的安全性能</p>
                </div>
            </li>
        </ul>
    </div>
  </div>
</template>

<script>
export default {
    name: 'GongNeng'
}
</script>

<style lang="less" scoped> 
.gongneng {
    h1 {
        margin: 50px 0;
    }
    .gongneng_main {
        ul {
            width: 1200px;
            margin: 0 auto;
            display: flex;
            flex-wrap: wrap;
            li {
                width: 540px;
                background-color: #fff;
                display: flex;
                padding: 60px;
                margin: 30px;
                img {
                    width: 80px;
                }
            }
        }
        .right {
            margin-left: 20px;
            h1 {
                margin: 20px 0;
                text-align: left;
            }
            p {
                text-align: left;
                color: #666;
            }
        }
    }
}
</style>