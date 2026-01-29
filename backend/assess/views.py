from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DataView(APIView):
    """
    Handle data upload and verification
    """
    def post(self, request):
        return Response({"status": "Not Implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)

class ModelView(APIView):
    """
    Handle model loading
    """
    def post(self, request):
        return Response({"status": "Not Implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)

class AttackView(APIView):
    """
    Handle attack execution
    """
    def post(self, request):
        return Response({"status": "Not Implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)

class EvalView(APIView):
    """
    Handle evaluation history/results
    """
    def get(self, request):
        return Response({"status": "Not Implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)
