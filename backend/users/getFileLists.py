import re, os, time


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)


def get_all_files(path, ID, folderList, fileList):
    all_file_list = os.listdir(path)
    # 遍历该文件夹下的所有目录或文件
    for file in all_file_list:
        file_path = os.path.join(path, file)
        # 如果是文件夹，递归调用当前函数
        if os.path.isdir(file_path):
            folderListItem = dict()
            folderListItem["name"] = file
            folderListItem["create_time"] = str(
                TimeStampToTime(os.path.getmtime(file_path))
            )
            folderListItem["id"] = ID["id"]
            folderListItem["folder_id"] = ID["folder_id"]
            folderListItem["file_path"] = file_path
            folderList.append(folderListItem)
            t = ID["folder_id"]
            ID["folder_id"] = ID["id"]
            ID["id"] += 1
            get_all_files(file_path, ID, folderList, fileList)
            ID["folder_id"] = t

        # 如果不是文件夹，保存文件路径及文件名
        elif os.path.isfile(file_path):
            fileListItem = dict()
            fileListItem["name"] = file
            fileListItem["create_time"] = str(
                TimeStampToTime(os.path.getmtime(file_path))
            )
            fileListItem["id"] = ID["id"]
            fileListItem["folder_id"] = ID["folder_id"]
            fileListItem["file_path"] = file_path
            fileList.append(fileListItem)
            ID["id"] += 1


def get_file_lists(path):
    ID = {"id": 1, "folder_id": 0}
    folderList = []
    fileList = []
    folderListItem = dict()
    folderListItem["name"] = path.split("/")[-1]
    folderListItem["create_time"] = str(TimeStampToTime(os.path.getmtime(path)))
    folderListItem["id"] = ID["id"]
    folderListItem["folder_id"] = ID["folder_id"]
    folderListItem["file_path"] = path
    folderList.append(folderListItem)
    ID["folder_id"] = ID["id"]
    ID["id"] += 1
    get_all_files(path, ID, folderList, fileList)
    # print('-'*12)
    # print(fileList)
    # print(folderList)
    # print('-'*12)
    return fileList, folderList


def test():
    path_list, file_name_list = get_file_lists("./PublicFolder")
    print("file:\n", path_list)
    print("folder:\n", file_name_list)


if __name__ == "__main__":
    test()
