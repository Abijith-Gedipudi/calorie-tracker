from django.shortcuts import render, redirect
from .models import FoodTable, Calories
# Create your views here.


def index(request):
    foods = FoodTable.objects.all()  # Always load foods first

    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')  # Use .get() to avoid crashing if missing

        if food_consumed:  # Proceed only if something was selected
            try:
                food = FoodTable.objects.get(name=food_consumed)
                user = request.user
                consume = Calories(user=user, food_consumed=food)
                consume.save()
            except FoodTable.DoesNotExist:
                pass  # You can handle or log this if needed

    consumed_food = Calories.objects.filter(user=request.user)

    return render(request, 'myapp/index(Main).html', {
        'foods': foods,
        'consumed_food': consumed_food
    })



def delete_consume(request, id):
    consumed_food = Calories.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'myapp/remove.html')