from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.conf import settings
import sys
from multiprocessing import Process
from utils.task import task_wrapper

from rest_framework.authtoken.views import APIView, AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import shutil
from pathlib import Path
import os
import json
import zipfile
from .models import UserInfo
from .decrypt import decrypt
from .getFileLists import get_file_lists
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


class Register(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = decrypt(request.data.get("password"))
        # username, email=None, password=None, **extra_fields

        if UserInfo.objects.filter(username=username).exists():
            resp = {"status": False, "data": "用户名已被注册"}
        else:
            print(username)
            user = UserInfo.objects.create_user(username=username, password=password)
            
            # Use os.path.join and settings.BASE_DIR for robust paths
            userFolder = os.path.join(settings.BASE_DIR, "UserData", username)
            envFolder = os.path.join(userFolder, "Env")
            modelFolder = os.path.join(userFolder, "Model")
            datasetFolder = os.path.join(userFolder, "DataSet")
            
            os.makedirs(userFolder, exist_ok=True)
            os.makedirs(envFolder, exist_ok=True)
            os.makedirs(modelFolder, exist_ok=True)
            os.makedirs(datasetFolder, exist_ok=True)
            
            print(user)
            token, created = Token.objects.get_or_create(user=user)
            resp = {
                "status": True,
                "token": token.key,
                "user_id": user.pk,
                "user_name": user.username,
            }
        return Response(resp)


class Login(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        userpwd = decrypt(request.data.get("password"))
        user = UserInfo.objects.filter(username=username).first()
        if user != None and check_password(userpwd, user.password):
            token, created = Token.objects.get_or_create(user=user)
            resp = {
                "status": 200,
                "token": token.key,
                "user_id": user.pk,
                "user_name": user.username,
            }
        else:
            resp = {"status": False, "data": "登录失败，用户名或密码错误"}
        print(resp)
        return Response(resp)


class Logout(APIView):
    """退出登录"""

    print("***")

    def logout(request):
        response = HttpResponseRedirect("/account/login/")
        response.delete_cookie("ticket")
        return response


# 实现上传功能的upload


class Upload(APIView):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            # 请求方法为POST时，执行文件上传
            username = request.POST.get("userName")
            # subfolder = request.POST.get('subfolder')
            print(username)
            subfolder = request.POST.get("fileType")
            print(subfolder)
            myFile = request.FILES.get(subfolder)
            if not myFile:
                resp = {"status": False}
            else:
                # 打开特定的文件进行二进制的写操作
                # Fix path
                dir_path = os.path.join(settings.BASE_DIR, "UserData", username, subfolder)
                print(dir_path)
                if os.path.exists(dir_path) == False:
                    os.makedirs(dir_path)
                file_path = os.path.join(dir_path, myFile.name)
                print(file_path)
                
                with open(file_path, "wb+") as f:
                    for chunk in myFile.chunks():
                        f.write(chunk)
                
                if subfolder == "dataset":
                    # Use zipfile instead of unzip command
                    try:
                        with zipfile.ZipFile(file_path, 'r') as zip_ref:
                            zip_ref.extractall(dir_path)
                        dataset_path = dir_path
                    except Exception as e:
                        print(f"Error extracting zip: {e}")
                else:
                    model_path = file_path
                resp = {"status": True}
            return Response(resp)
        else:
            resp = {"status": False}
            return Response(resp)


class UploadText(APIView):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            print(request.data)
            username = request.data.get("username")
            attack = request.data.get("attack")
            time = request.data.get("time")
            print(username)
            print(attack)
            print(time)

            resp = {"status": True}
        else:
            resp = {"status": False}
            
        # Fix paths
        dataset_path = os.path.join(settings.BASE_DIR, "UserData", username, "dataset")
        model_path = os.path.join(settings.BASE_DIR, "UserData", username, "model", "model.pth")
        
        task_dict = {
            "task_type": "FGM",
            "attack_list": attack,
            "record": {
                "username": username,
                "create_time": time,
                "dataname": "MNIST",
                "modelname": "model.pth",
            },
            "dataset": dataset_path,
            "model": model_path,
        }
        task_dict_path = os.path.join(settings.BASE_DIR, "UserData", username, "task_dict.json")
        with open(task_dict_path, "w") as f:
            json.dump(task_dict, f)
            
        # Execute task in background process
        print(f"Starting task for user {username}")
        p = Process(target=task_wrapper, args=(task_dict,))
        p.start()
        
        return Response(resp)


class GetEvalHistory(APIView):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            print(request.data)
            username = request.data.get("username")
            time = "2023-03-13"
            # Fix report path
            report = os.path.join(settings.BASE_DIR, "UserData", username, "report.pdf")
            
            task_dict_path = os.path.join(settings.BASE_DIR, "UserData", username, "task_dict.json")
            if os.path.exists(task_dict_path):
                with open(task_dict_path, "r") as f:
                    task_dict = json.load(f)
                
                if os.path.isfile(report) == False:
                    report = "正在评估"
                resp = {
                    "status": True,
                    "createTime": task_dict["record"]["create_time"],
                    "TaskInfo": task_dict["attack_list"],
                    "EvalState": report,
                }
            else:
                 resp = {"status": False, "msg": "No task history"}
        else:
            resp = {"status": False}
        return Response(resp)


class GetFolderList(APIView):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            username = request.data.get("username")
            print(username)
            # Fix path
            user_path = os.path.join(settings.BASE_DIR, "UserData", username)
            public_path = os.path.join(settings.BASE_DIR, "UserData", "PublicFolder")
            
            if not os.path.exists(user_path): os.makedirs(user_path)
            if not os.path.exists(public_path): os.makedirs(public_path)

            __, folderList = get_file_lists(user_path)
            __, publicFolderList = get_file_lists(public_path)
            resp = {"folderList": folderList, "publicFolderList": publicFolderList}
            return Response(resp)


class GetFileList(APIView):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            username = request.data.get("username")
            user_path = os.path.join(settings.BASE_DIR, "UserData", username)
            public_path = os.path.join(settings.BASE_DIR, "UserData", "PublicFolder")
            
            if not os.path.exists(user_path): os.makedirs(user_path)
            if not os.path.exists(public_path): os.makedirs(public_path)

            fileList, __ = get_file_lists(user_path)
            publicFileList, __ = get_file_lists(public_path)
            resp = {"fileList": fileList, "publicFileList": publicFileList}
            return Response(resp)


class DeleteFile(APIView):
    def post(self, request, *args, **kwargs):
        DeleteFileList = request.data.get("DeleteFileList")
        print(DeleteFileList)
        rPath = os.path.join(settings.BASE_DIR, "UserData")
        for path in DeleteFileList:
            # Simple security check, should be improved
            if os.path.abspath(path).startswith(os.path.abspath(rPath)):
                print(path)
                print(os.path.exists(path))
                if os.path.exists(path):
                    if os.path.isfile(path):
                        os.remove(path)
                    else:
                        shutil.rmtree(path)
        return Response(DeleteFileList)


class ShareFile(APIView):
    def post(self, request, *args, **kwargs):
        ShareFileList = request.data.get("ShareFileList")
        username = request.data.get("username")
        
        # This implementation logic is complex and might be fragile. 
        # Simplified to copying for Windows compatibility (symlinks require admin)
        
        rPath = str(settings.BASE_DIR)
        
        for path in ShareFileList:
            # Assuming path is relative or absolute, need to be careful
            # Original code logic was very specific to its directory structure
            # Attempting to replicate logic safely
            
            if "UserData" in path:
                rel_path = path.split("UserData")[1].lstrip(os.sep).lstrip('/')
                src_path = os.path.join(settings.BASE_DIR, "UserData", rel_path)
                
                # Construct dest path in PublicFolder
                # path structure: .../UserData/username/...
                # target: .../UserData/PublicFolder/username/...
                
                dest_rel = rel_path.replace(username, os.path.join("PublicFolder", username), 1)
                dst_path = os.path.join(settings.BASE_DIR, "UserData", dest_rel)
                
                dst_dir = os.path.dirname(dst_path)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                
                if os.path.exists(src_path):
                     if os.path.isfile(src_path):
                        if not os.path.exists(dst_path):
                            shutil.copy2(src_path, dst_path) # Copy instead of symlink
                            
        return Response(ShareFileList)


class UnshareFile(APIView):
    def post(self, request, *args, **kwargs):
        UnshareFileList = request.data.get("UnshareFileList")
        print(UnshareFileList)
        username = request.data.get("username")
        rPath = os.path.join(settings.BASE_DIR, "UserData", "PublicFolder")
        
        for path in UnshareFileList:
            if username in path and os.path.abspath(path).startswith(os.path.abspath(rPath)):
                if os.path.exists(path):
                    if os.path.isfile(path):
                        os.remove(path)
                    else:
                        shutil.rmtree(path)
        return Response(UnshareFileList)
