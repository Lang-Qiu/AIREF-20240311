<template>
  <div>
    <div class="report">
      <Banner>
        <h1 slot="title">测评报告</h1>
        <p slot="text">这里提供了各种关于模型性能和数据集分析的详细报告。我们的测评报告将帮助您了解不同模型的性能、数据集的特点，以及如何选择最适合您需求的解决方案。</p>
        <img slot="image" src="../../assets/xtys4.png" alt="" style="width: 240px;">
      </Banner>
    </div>
    <el-table
      :data="tableData"
      style="width: 810px; margin: 100px auto"
      >
      <el-table-column
        prop="submit_time"
        label="提交时间"
        width="180">
      </el-table-column>

      <el-table-column
        prop="submit_type"
        label="评估类型"
        width="180">
      </el-table-column>

      <el-table-column
        prop="submit_status"
        label="评估状态"
        width="180">
      </el-table-column>
      
      <el-table-column
        prop="submit_pic"
        label="评估报告"
        width="270">
        <template slot-scope="scope">
        <a :href="scope.row.path" download style="color: #606266;" @click="downloadFile(scope.row.submit_pic)" target='_blank'>
          <div style="cursor: pointer;">
            {{ scope.row.submit_pic }}
          </div>
        </a>
      </template>
      </el-table-column>
  </el-table>
  </div>
</template>

<script>
import { saveAs as FileSaver } from 'file-saver';
export default {
  
    name: 'ReportIndex',
    data() {
      return {
        // tableData: [
        //    // 存储后台返回的文件信息数组
        //   {
        //   date: '2016-05-02',
        //   name: '图像分类模型评估',
        //   status: '排队中',
        //   report: '',
        //   path: '/path-to-your-pdf/file1.pdf'
        // }, {
        //   date: '2016-05-02',
        //   name: '图像分类模型评估',
        //   status: '评估中',
        //   report: '',
        //   path: '/path-to-your-pdf/file1.pdf'
        // }, {
        //   date: '2016-05-02',
        //   name: '图像分类模型评估',
        //   status: '评估完成',
        //   report: '图像分类测评报告.pdf',
        //   path: 'https://zilongv.com/t.pdf'
        // }],
      }      
    },
    computed: {
      tableData() {
        return this.$store.state.submitList
      }
    },
    mounted() {
      console.log(this.tableData, '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    },
    methods: {
    // downloadFile(path, report) {  
    //   // 创建一个临时文件名  
    //   const tempFileName = path;
    //   // 使用 fetch 获取文件内容  
    //   fetch(path)  
    //     .then((res) => res.arrayBuffer())  
    //     .then((buffer) => {  
    //       // 创建一个 Blob 对象  
    //       const blob = new Blob([buffer], { type: 'application/png' });
    //       // 创建一个隐藏的 a 标签，用于触发下载  
    //       const link = document.createElement('a');  
    //       link.href = URL.createObjectURL(blob);  
    //       link.download = tempFileName;  
    //       link.style.display = 'none';
    //       // 将隐藏的 a 标签添加到文档中，然后触发点击事件  
    //       document.body.appendChild(link);  
    //       link.click();
    //       // 等待一段时间以确保下载完成  
    //       setTimeout(() => {  
    //         // 移除隐藏的 a 标签  
    //         document.body.removeChild(link);
    //       }, 1); // 这里可以适当增加等待时间
    //     })  
    //     .catch((err) => {  
    //       console.error('下载文件时发生错误：', err);  
    //     });  
    // }
//  downloadFile(path, report3) {  
//   // 创建一个临时文件名  
//   const tempFileName = path;
//   // 使用 fetch 获取文件内容  
//   fetch(path)  
//     .then((res) => res.arrayBuffer())  
//     .then((buffer) => {  
//       // 创建一个 Blob 对象  
//       const blob = new Blob([buffer], { type: 'application/pdf' });
//       // 创建一个隐藏的 a 标签，用于触发下载  
//       const link = document.createElement('a');  
//       link.href = URL.createObjectURL(blob);  
//       link.download = tempFileName;  
//       link.style.display = 'none';
//       // 将隐藏的 a 标签添加到文档中，然后触发点击事件  
//       document.body.appendChild(link);  
//       link.click();
//       // 使用 Promise.all() 等待文件下载完成  
//       return new Promise((resolve) => {  
//         link.addEventListener('load', () => {  
//           // 创建一个新窗口  
//           const newWindow = window.open(tempFileName, '_blank');
//           // 等待文件加载完成后，关闭新窗口  
//           resolve(newWindow);  
//         });  
//       });  
//     })  
//     .then((newWindow) => {  
//       // 等待新窗口关闭  
//       return newWindow.closed;  
//     })  
//     .catch((err) => {  
//       console.error('下载文件时发生错误：', err);  
//     });  
// }

// downloadPDF(url, filename) {  
//   fetch(url)  
//     .then((response) => response.arrayBuffer())  
//     .then((arrayBuffer) => {  
//       const reader = new FileReader();  
//       reader.onload = function (e) {  
//         const pdfData = e.target.result;
//         // 生成 PDF 文件的 Blob 对象  
//         const blob = new Blob([pdfData], { type: 'application/pdf' });
//         // 下载 PDF 文件  
//         downloadFile(blob, filename);  
//       };
//       reader.readAsArrayBuffer(arrayBuffer);  
//     });  
// }
downloadFile(report) {
  console.log(report, 'report')
      const oReq = new XMLHttpRequest()
      // const URL = 'http://localhost:8080/download/t.pdf' // URL 为下载的URL地址
      oReq.open('GET', report, true)
      oReq.responseType = 'blob'
      oReq.onload = function () {
        const file = new Blob([oReq.response], {
          type: 'blob'
        })
        FileSaver.saveAs(file, 'psreport.pdf') // fileName为文件名
      }
      oReq.send()
    }


  },
}
</script>

<style>
.report {
  background: url('../../assets/duanshipinbk.png') no-repeat;
  background-size: 100% 100%;
}
.el-table .cell {
  text-align: center;
}
.el-table th {
  text-align: center;
}
</style>