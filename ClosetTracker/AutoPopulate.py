import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ClosetTracker.settings")

import django
django.setup()

from tracker.models import ClothingType, Season, Color, Size






context_dict ={}
def get_clothes():
	clothes = ["sweater","shirt","pants","dress","skirt",
	"shoes","underwear","size","color","price","picture"]

	seasons = ["Winter","Summer","Fall","Spring"]

	sizes = ["3XL","2XL","XL","L","M","S","XS"]

	colors = ["red","blue","green","yellow","orange","camo","black","white","purple"]


	for item in clothes:
		c, created = ClothingType.objects.get_or_create(name=item)
		c.save()
		 
	for season in seasons:
		s, created = Season.objects.get_or_create(name=season)
		s.save()
	for size in sizes:

		s2, created = Size.objects.get_or_create(name=size)
		s2.save()
	for color in colors:

		c2, created = Color.objects.get_or_create(name=color)
		c2.save()
	return c, s, s2, c2		 
		 


get_clothes()