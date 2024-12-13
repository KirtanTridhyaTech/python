from django.shortcuts import render
import cv2
import numpy as np
from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ImageUpload
from .serializers import ImageUploadSerializer

@api_view(['POST'])
def upload_image(request):
    serializer = ImageUploadSerializer(data=request.data)
    if serializer.is_valid():
        image_instance = serializer.save()
        image_path = image_instance.image.path
        
        # Load the image using OpenCV
        image = cv2.imread(image_path)

        # Get the filter type from the request
        filter_type = request.data.get('filter')

        # Apply the selected filter
        if filter_type == "grayscale":
            processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        elif filter_type == "blur":
            processed_image = cv2.GaussianBlur(image, (15, 15), 0)
        elif filter_type == "edge":
            processed_image = cv2.Canny(image, 100, 200)
        else:
            return Response({"error": "Invalid filter"}, status=status.HTTP_400_BAD_REQUEST)

        # Save the processed image to a file
        processed_image_path = f'uploads/processed_{filter_type}.jpg'
        cv2.imwrite(processed_image_path, processed_image)

        # Create response data as base64 encoded string
        response_data = {'saved_image_path': processed_image_path  # Return the path of the saved image
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)