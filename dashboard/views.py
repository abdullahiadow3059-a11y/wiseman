import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid JSON"})

        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            return JsonResponse({
                "id": user.id,
                "username": user.username
            })

        return JsonResponse({"error": "Invalid credentials"})
    
    return JsonResponse({"error": "POST only"})
    

# SIMPLE MEMORY DB
expenses_db = {}

@csrf_exempt
def add_expense(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = str(data.get("user_id"))

        if user_id not in expenses_db:
            expenses_db[user_id] = []

        expenses_db[user_id].append({
            "amount": data.get("amount"),
            "category": data.get("category"),
            "description": data.get("description")
        })

        return JsonResponse({"status": "success"})

    return JsonResponse({"error": "POST only"})


def get_expenses(request, user_id):
    return JsonResponse(expenses_db.get(str(user_id), []), safe=False)


@csrf_exempt
def reset(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = str(data.get("user_id"))
        expenses_db[user_id] = []
        return JsonResponse({"status": "reset"})

    return JsonResponse({"error": "POST only"})
