from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import os
import json
import datetime
from multiprocessing import Process
from utils.task import task_wrapper

class DataView(APIView):
    """
    Handle data upload and verification
    """
    def post(self, request):
        data_url = request.data.get('data_url')
        data_token = request.data.get('data_token')
        username = request.data.get('username')

        if not data_url:
            return Response(
                {"error": "Missing data_url"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if file exists in UserData
        if username:
            file_path = os.path.join(settings.BASE_DIR, "UserData", username, "DataSet", data_url)
            if os.path.exists(file_path):
                # Real file exists
                return Response({
                    "status": "verified",
                    "data_pic": "Verified Local File: " + data_url,
                    "preview": {"name": data_url, "exists": True}
                }, status=status.HTTP_200_OK)

        # Fallback / Remote URL Mock
        return Response({
            "status": "verified",
            "data_pic": "Remote/Mock Data Verified",
            "preview": {
                "name": "CIFAR-10 (Mock)",
                "size": 1000,
                "classes": ["airplane", "automobile", "bird", "cat"],
            }
        }, status=status.HTTP_200_OK)

class ModelView(APIView):
    """
    Handle model loading
    """
    def post(self, request):
        model_url = request.data.get('model_url')
        username = request.data.get('username')
        
        if not model_url:
            return Response(
                {"error": "Missing model_url"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if file exists in UserData
        if username:
            file_path = os.path.join(settings.BASE_DIR, "UserData", username, "Model", model_url)
            if os.path.exists(file_path):
                return Response({
                    "status": "loaded",
                    "model_pic": "Verified Local Model: " + model_url,
                    "structure": "Custom Model"
                }, status=status.HTTP_200_OK)

        return Response({
            "status": "loaded",
            "model_pic": "ResNet18 (Mock)",
            "structure": "ResNet18",
            "layers": ["Conv2d", "BatchNorm2d", "ReLU"]
        }, status=status.HTTP_200_OK)

class AttackView(APIView):
    """
    Handle attack execution
    """
    def post(self, request):
        attack_list = request.data.get('attack_list')
        username = request.data.get('username')
        
        # Default mock values if missing
        if not username:
             username = "default_user"
        
        if not attack_list or not isinstance(attack_list, list):
            return Response(
                {"error": "Missing or invalid attack_list"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Construct Task Dict (reusing UploadText logic)
        time_str = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Ensure directories exist
        dataset_path = os.path.join(settings.BASE_DIR, "UserData", username, "DataSet")
        model_path = os.path.join(settings.BASE_DIR, "UserData", username, "Model", "model.pth") # Default model name assumption?
        
        # Check if user provided specific model/data in previous steps?
        # Frontend passes model_url/data_url here too!
        data_url = request.data.get('data_url')
        model_url = request.data.get('model_url')
        
        if data_url and os.path.exists(os.path.join(settings.BASE_DIR, "UserData", username, "DataSet", data_url)):
             dataset_path = os.path.join(settings.BASE_DIR, "UserData", username, "DataSet", data_url)
        
        if model_url and os.path.exists(os.path.join(settings.BASE_DIR, "UserData", username, "Model", model_url)):
             model_path = os.path.join(settings.BASE_DIR, "UserData", username, "Model", model_url)

        task_dict = {
            "task_type": "adv_white", # Default to whitebox
            "attack_list": attack_list,
            "record": {
                "username": username,
                "create_time": time_str,
                "dataname": data_url or "MNIST",
                "modelname": model_url or "model.pth",
            },
            "dataset": dataset_path,
            "model": model_path,
        }
        
        # Save task_dict
        task_dict_dir = os.path.join(settings.BASE_DIR, "UserData", username)
        if not os.path.exists(task_dict_dir):
            os.makedirs(task_dict_dir)
            
        task_dict_path = os.path.join(task_dict_dir, "task_dict.json")
        with open(task_dict_path, "w") as f:
            json.dump(task_dict, f)

        # Start Async Task
        p = Process(target=task_wrapper, args=(task_dict,))
        p.start()

        # Return Mock Result for Frontend Display
        # In real system, this should probably use WebSocket or Polling
        results = []
        for attack_method in attack_list:
            results.append({
                "method": attack_method,
                "status": "processing"
            })

        return Response({
            "status": "processing",
            "attack_pic": "Task Started. Check Report later.", 
            "results": results
        }, status=status.HTTP_200_OK)

class EvalView(APIView):
    """
    Handle evaluation history/results
    """
    def get(self, request):
        return Response({"status": "Not Implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)
