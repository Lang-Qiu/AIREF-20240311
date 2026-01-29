import clonedeep from "lodash/cloneDeep"

export const putFileInFolder = (folderList, fileList) => {
    // 这里获得folder-tree中获取到的两个数组
    // 数组也是对象，在js中对象使用引用赋值，当我们修改变量的时候其实修改的是这个地址所引用的对象
    // 所以我们要进行深拷贝
    const folderListCloned = clonedeep(folderList)
    const fileListCloned = clonedeep(fileList)
    // 接下来遍历文件夹
    // map方法对数组进行映射，里面有三个参数，当前遍历的项，当前遍历的索引以及当前遍历的数组
    return folderListCloned.map(folderItem => {
        // 我们每遍历一个folderitem，都要判断一下文件列表下的哪些文件的id与文件夹的相同
        // 所以我们先获取一下当前文件夹的id(可以对照控制台输出的res数据结构进行配置)
        const folderId = folderItem.id
        // 避免已归属文件的重复，这里我们使用length是可以从数组后面删除元素，从而不改变数组的索引
        // 对前面的元素没有影响
        let index = fileListCloned.length
        while (--index >= 0) {
            // 获取当前遍历到的文件对象
            // 第一次遍历的时候这里代表最后一个文件对象
            const fileItem = fileListCloned[index]
            // 判断当前文件是否属于遍历到的文件夹
            if (fileItem.folder_id === folderId) {
                // 使用splice方法我们既能删除也能添加，这里我们只需要删除
                // splice第一个参数表示索引号，1表示删除几个元素，返回值为一个数组
                const file = fileListCloned.splice(index, 1)[0]
                // 有时候后端传来的数据可能和我们需要的属性名不对称，我们需要加一个属性名
                file.title = file.name
                // 接下来把文件放到文件夹里
                // 判断是否有children属性
                if (folderItem.children) folderItem.children.push(file)
                else folderItem.children = [file]
            }
        }
        // 为了方便我们在后面做render的时候加一些定制化的东西
        // 这里我们给folderItem加一个类型,方便我们后面判断渲染的是文件夹还是文件
        folderItem.type = 'folder'
        // 一定要记住return出去
        return folderItem
    })
}
export const transferFolderToTree = folderList => {
    // 如果这个文件夹列表为空
    if (!folderList.length) return []
    // 这里不用else也可以
    // 把folderListCloned深拷贝一份，以免操作原数组
    const folderListCloned = clonedeep(folderList)
    // 由于文件夹下有很多层级，所以这里我们要使用递归函数
    // 在内部定义一个方法，id为当前文件夹的id
    const handle = id => {
        // 创建一个空数组用来放文件夹
        let arr = []
        // 遍历拷贝的文件夹列表，参数为我们当前遍历的文件夹对象
        folderListCloned.forEach(folder => {
            // 如果条件成立，则表示当前文件夹是id值为当前参数id的文件夹的子集文件夹
            if (folder.folder_id === id) {
                // 递归操作
                const children = handle(folder.id)
                // 如果有children则直接拼接起来
                if (folder.children) folder.children = [].concat(folder.children, children)
                // 如果没有children直接让children等于获取到的children
                else folder.children = children
                folder.title = folder.name
                arr.push(folder)
            }
        })
        return arr
    }
    return handle(0)
}