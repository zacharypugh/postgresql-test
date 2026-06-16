from django.shortcuts import render
from django.http import JsonResponse
from .models import Sale
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def sales_summary(request):

    sales = Sale.objects.all()

    data = [
        {
            "id": s.id,
            "customer": s.customer_name,
            "amount": float(s.amount)
        }
        for s in sales
    ]

    return JsonResponse(data, safe=False)

# @csrf_exempt  # Exempting for simplicity; use standard token auth or DRF permissions in production
# def run_analysis(request):
#     if request.method == 'POST':
#         try:
#             # Parse the JSON payload sent from React
#             data = json.loads(request.body)
#             category = data.get('category')

#             # Filter the PostgreSQL database based on the selected category
#             if category == "< 100":
#                 count = Sale.objects.filter(amount__lt=100).count()
#             elif category == ">= 100":
#                 count = Sale.objects.filter(amount__gte=100).count()
#             else:
#                 return JsonResponse({'error': 'Invalid category selected.'}, status=400)

#             # Return the result to React
#             return JsonResponse({'count': count})
            
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
            
#     return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
# @csrf_exempt  
# def run_analysis(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             category = data.get('category')

#             # Match against the new safe string keys
#             if category == "less_than_100":
#                 count = Sale.objects.filter(amount__lt=100).count()
#             elif category == "greater_or_equal_100":
#                 count = Sale.objects.filter(amount__gte=100).count()
#             else:
#                 return JsonResponse({'error': f'Invalid category selected: {category}'}, status=400)

#             return JsonResponse({'count': count})
            
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
            
#     return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

# @csrf_exempt  
# def run_analysis(request):
#     if request.method == 'POST':
#         try:
#             # Check if body exists
#             if not request.body:
#                 print("🚨 RENDER LOG: The request body is completely empty!")
#                 return JsonResponse({'error': 'Empty request body sent from frontend.'}, status=400)
            
#             # Print raw payload to Render Logs so we can read it
#             print(f"📁 RENDER LOG Raw Body: {request.body.decode('utf-8')}")

#             try:
#                 data = json.loads(request.body)
#             except json.JSONDecodeError as json_err:
#                 print(f"❌ RENDER LOG JSON Decode Error: {str(json_err)}")
#                 return JsonResponse({'error': f'Invalid JSON format: {str(json_err)}'}, status=400)

#             category = data.get('category')
#             print(f"🔍 RENDER LOG Extracted Category: {category}")

#             # Your matching text keys
#             if category == "less_than_100":
#                 count = Sale.objects.filter(amount__lt=100).count()
#             elif category == "greater_or_equal_100":
#                 count = Sale.objects.filter(amount__gte=100).count()
#             else:
#                 print(f"⚠️ RENDER LOG: Fell into else block with category: {category}")
#                 return JsonResponse({'error': f'Invalid category: {category}'}, status=400)

#             return JsonResponse({'count': count})
            
#         except Exception as e:
#             print(f"💥 RENDER LOG Global Exception: {str(e)}")
#             return JsonResponse({'error': str(e)}, status=500)
            
#     return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

@csrf_exempt  
def run_analysis(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            category = data.get('category', '')

            # 1. Strip all whitespaces (normal or hidden) to prevent matching errors
            # This turns "< 100" or "<  100" into "<100"
            clean_category = "".join(category.split())

            # 2. Check the cleaned values
            if "100" in clean_category and "<" in clean_category:
                count = Sale.objects.filter(amount__lt=100).count()
            elif "100" in clean_category and ">" in clean_category:
                count = Sale.objects.filter(amount__gte=100).count()
            else:
                return JsonResponse({'error': f'Invalid category: {category}'}, status=400)

            return JsonResponse({'count': count})
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
            
    return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)