from main.models import ItemModel
from main.models import SellerModel
from main.models import CategoryModel
from main.models import CurrencyModel

seller = SellerModel.objects.filter(username='new_user')
currency = CurrencyModel.objects.filter(short_name='грн.')
category = CategoryModel.objects.filter(name='Спортивные носки, гетры')
item = ItemModel.objects.create(short_name='Test item 1', seller=seller[0], category=category[0], currency=currency[0])
item.price = 23.56
item.save()

# --------------------------------------------------------------------------------------------------------------------

cat = CategoryModel.objects.get(name='Спортивные носки, гетры')
items = ItemModel.objects.all().filter(category=cat, price__lte=25)

# --------------------------------------------------------------------------------------------------------------------

'''
>>> from main.models import ItemModel
>>> from main.models import SellerModel
>>> from main.models import CurrencyModel
>>> from main.models import CategoryModel
>>>
>>> seller = SellerModel.objects.get(username='new_user')
>>> seller
<SellerModel: new_user>
>>> currency = CurrencyModel.objects.get(short_name='грн.')
>>> currency
<CurrencyModel: грн.>
>>> category = CategoryModel.objects.get(name='Спортивные носки, гетры')
>>> category
<CategoryModel: Спортивные носки, гетры>
>>> item = ItemModel.objects.create(short_name='Some good', category=category, seller=seller, currency=currency, price=150)
>>> item
<ItemModel: Some good>
>>> item.save()
>>> item.pk
10
>>> item = ItemModel(short_name='One more item', category=category, seller=seller, currency=currency, price=151)
>>> item
<ItemModel: One more item>
>>> item.pk
>>> item.save()
>>> item.pk
11
>>> 
>>> 
>>> i = ItemModel.objects.all().filter(price__gte=149, price__lte=152)
>>> i
<QuerySet [<ItemModel: Some good>, <ItemModel: One more item>]>
>>> i.query.__str__()
'SELECT "main_itemmodel"."id", "main_itemmodel"."short_name", "main_itemmodel"."description", "main_itemmodel"."image", 
"main_itemmodel"."seller_id", "main_itemmodel"."category_id", "main_itemmodel"."price", "main_itemmodel"."currency_id", 
"main_itemmodel"."published", "main_itemmodel"."item_create", "main_itemmodel"."item_update" FROM "main_itemmodel" 
WHERE ("main_itemmodel"."price" >= 149.0 AND "main_itemmodel"."price" <= 152.0)'
'''
