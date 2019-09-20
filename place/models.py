from django.db import models

class Place(models.Model):
	name          = models.CharField(max_length = 100, null = False, unique = True)
	full_address  = models.CharField(max_length = 100, null = False)
	zipcode       = models.CharField(max_length = 10, null = False)
	street        = models.CharField(max_length = 100, null = False)
	county        = models.CharField(max_length = 20, null = False)
	city          = models.CharField(max_length = 10, null = False)
	province      = models.CharField(max_length = 20, null = False)
	country       = models.CharField(max_length = 20, null = False)
	longitude     = models.CharField(max_length = 100, null = False)
	latitude      = models.CharField(max_length = 100, null = False)
	website       = models.URLField(max_length = 2500, null = True)
	facebook      = models.URLField(max_length = 2500, null = True)
	instagram     = models.URLField(max_length = 2500, null = True)
	phone         = models.CharField(max_length = 100, null = True)
	price_min     = models.DecimalField(max_digits = 9, decimal_places = 1, null = False)
	price_max     = models.DecimalField(max_digits = 9, decimal_places = 1, null = False)
	persons_min   = models.PositiveSmallIntegerField(null = False)
	persons_max   = models.PositiveSmallIntegerField(null = False)
	is_vacancy    = models.BooleanField(default = True, null = True)
	room_capacity = models.PositiveSmallIntegerField(null = False)
	check_in      = models.CharField(max_length = 10, null = False)
	check_out     = models.CharField(max_length = 10, null = False)
	created_at    = models.DateTimeField(auto_now_add = True)
	updated_at    = models.DateTimeField(auto_now = True)
	styles        = models.ManyToManyField('Style', blank = True)
	targets       = models.ManyToManyField('Target', blank = True)
	amenities     = models.ManyToManyField('Amenity', blank = True)
	tourspots     = models.ManyToManyField('Tourspot', blank = True)
	features      = models.ManyToManyField('Feature', blank = True)

	class Meta:
		db_table = 'place'

class Style(models.Model):
	styles = models.CharField(max_length = 100, null = True, unique = True)

	class Meta:
		db_table = 'style'

class Target(models.Model):
	targets = models.CharField(max_length = 100, null = True, unique = True)
	
	class Meta:
		db_table = 'target'

class Amenity(models.Model):
	amenities = models.CharField(max_length = 100, null = True, unique = True)
	
	class Meta:
		db_table = 'amenity'

class Tourspot(models.Model):
	tourspots = models.CharField(max_length = 100, null = True, unique = True)
	
	class Meta:
		db_table = 'tourspot'

class Feature(models.Model):
	features = models.CharField(max_length = 100, null = True, unique = True)

	class Meta:
		db_table = 'feature'
