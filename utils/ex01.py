from main_app.models import Product, Category
from django.db.models import Count, Max, Min, Avg, Sum

result = Product.objects.values(
    'category__name').annotate(qty_products=Avg('id')).order_by('category__id')
