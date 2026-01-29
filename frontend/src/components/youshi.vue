<template>
  <div class="youshi">
    <div class="youshi_content">
        <h1>产品优势</h1>
        <div class="youshi_main">
            <ul>
                <li>
                    <h2>开箱及用</h2>
                    <p>门槛低，用户无需具备专业的人工智能模型安全知识，全界面化操作</p>
                </li>
                <li>
                    <h2>评估科学</h2>
                    <p>综合多维度攻击下模型的性能指标变化情况</p>
                </li>
                <li>
                    <h2>场景广泛</h2>
                    <p>平台支持多种数据类型，比如文本，图像，语音，图谱</p>
                </li>
            </ul>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'YouShi'
}
</script>

<style lang="less" scoped>
.youshi {
    background-color: #fff;
    height: 500px;
    .youshi_content {
        width: 1200px;
        margin: 0 auto;
        h1 {
            padding: 80px 0 30px;
        }
        ul {
            display: flex;
            li {
                width: 30%;
                padding: 20px;
                margin: 0 40px;
                box-shadow: 0 0 30px rgba(0,75,162,.09);
                height: 170px;
                list-style: none;
                h2 {
                    margin: 20px 0;
                }
                p {
                    text-align: left;
                    padding: 0 20px;
                    color: #666;
                }
            }
        }
    }
}
</style>