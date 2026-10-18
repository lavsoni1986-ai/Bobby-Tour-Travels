from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

IS_ACTIVE = (
		('yes', 'Yes'), #Left for Value Right for Display
		('no', 'No')
	)


DIFFICULTY = (
		('easy', 'Easy'),
		('medium', 'Medium'),
		('hard', 'Hard')
	)


class Activity(models.Model):
	activity_title = models.CharField(max_length=200, verbose_name="Activity Title")
	activity_slug = models.SlugField(max_length=200, verbose_name="Activity Slug")
	activity_description = RichTextField(blank=True, null=True, verbose_name="Activity Description")
	activity_image = models.ImageField(upload_to='activities/', blank=True, null=True, verbose_name="Activity Image")
	activity_icon = models.CharField(max_length=200, blank=True, null=True, verbose_name="Activity Icon")
	activity_is_active = models.CharField(
			choices = IS_ACTIVE,
			default = 'Yes',
			max_length = 10,
			verbose_name = 'Is Active?'
		)
	activity_is_featured = models.CharField(
			choices = IS_ACTIVE,
			default = 'Yes',
			max_length = 10,
			verbose_name = 'Is Featured?'
		)
	activity_created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
	activity_updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
	activity_added_by = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True, verbose_name="Added By")

	#META for SEO
	seo_activity_title = models.CharField(max_length=100, blank=True, null=True, verbose_name="SEO Activity Title (60 Characters Long)")
	seo_activity_keywords = models.TextField(blank=True, null=True, verbose_name="SEO Activity Keywords (Separated by Commas)")
	seo_activity_description = models.TextField(blank=True, null=True, verbose_name="SEO Activity Description (160 Characters Long)")

	class Meta:
		verbose_name = "Activity"
		verbose_name_plural = "Activities"
		ordering = ['-activity_created_at']

	def __str__(self):
		return self.activity_title



class Region(models.Model):
	region_title = models.CharField(max_length=200, verbose_name="Region Title")
	region_slug = models.CharField(max_length=200, verbose_name="Region Slug")
	region_description = RichTextField(blank=True, null=True, verbose_name="Region Description")
	region_image = models.ImageField(upload_to='regions/', blank=True, null=True, verbose_name="Region Image")
	region_is_active = models.CharField(
			choices = IS_ACTIVE,
			default = 'Yes',
			max_length = 10,
			verbose_name = 'Is Active?'
		)
	region_is_featured = models.CharField(
			choices = IS_ACTIVE,
			default = 'Yes',
			max_length = 10,
			verbose_name = 'Is Featured?'
		)
	region_created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
	region_updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
	region_added_by = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True, verbose_name="Added By")

	# Meta for SEO
	seo_region_title = models.CharField(max_length=200, blank=True, null=True, verbose_name="SEO Region Title (60 Characters Long)")
	seo_region_keywords = models.TextField(blank=True, null=True, verbose_name="SEO Region Keywords (Separated by Commas)")
	seo_region_description = models.TextField(blank=True, null=True, verbose_name="SEO Region Description (160 Characters Long)")

	def __str__(self):
		return self.region_title


	class Meta:
		verbose_name = "Region"
		verbose_name_plural = "Regions"
		ordering = ['-region_created_at']



class Tour(models.Model):
	tour_title = models.CharField(max_length=200, verbose_name="Tour Title")
	tour_slug = models.CharField(max_length=200, verbose_name="Tour Slug")
	tour_duration = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Tour Duration")
	tour_altitude = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Tour Max Altitude")
	tour_difficulty = models.CharField(
			choices = DIFFICULTY,
			default = 'Medium',
			max_length = 10,
			verbose_name = 'Tour Difficulty'
		)
	starting_price = models.CharField(
		max_length=100,
		blank=True,
		default="Starting ₹2,499",
		verbose_name="Starting Price / Tariff",
		help_text="e.g. 'Starting ₹2,499' or '₹12/km (Outstation)'"
	)
	tour_description = RichTextField(blank=True, null=True, verbose_name="Tour Description")
	tour_image = models.ImageField(upload_to='tours/', blank=True, null=True, verbose_name="Tour Image")
	tour_map = models.ImageField(upload_to='maps/', blank=True, null=True, verbose_name="Tour Map")
	tour_activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, default = None, null=True, verbose_name='Tour Activity')
	tour_region = models.ManyToManyField(Region, verbose_name='Tour Region')
	tour_is_active = models.CharField(
			choices = IS_ACTIVE,
			default = 'Yes',
			max_length = 10,
			verbose_name = 'Is Active?'
		)
	tour_is_featured = models.CharField(
			choices = IS_ACTIVE,
			default = 'Yes',
			max_length = 10,
			verbose_name = 'Is Featured?'
		)
	tour_created_at = models.DateTimeField(auto_now_add=True, verbose_name="Added Date")
	tour_updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
	tour_added_by = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True, verbose_name='Added By')

	# Meta for SEO

	seo_tour_title = models.CharField(max_length=200, blank=True, null=True, verbose_name="SEO Tour Title (60 Characters Long)")
	seo_tour_keywords = models.TextField(blank=True, null=True, verbose_name="SEO Tour Keywords Separated by Commas")
	seo_tour_description = models.TextField(blank=True, null=True, verbose_name="SEO Tour Description (160 Characters Long)")

	class Meta:
		verbose_name = "Tour Package"
		verbose_name_plural = "Tour Packages"
		ordering = ['-tour_created_at']

	def __str__(self):
		return self.tour_title


class BookingEnquiry(models.Model):
	"""Stores cab/tour booking enquiries submitted via the Contact page."""

	CAR_CHOICES = (
		('', 'Any / Not Sure'),
		('Maruti Dzire', 'Maruti Dzire (Sedan)'),
		('Maruti Ertiga', 'Maruti Ertiga (MUV)'),
		('Mahindra Scorpio', 'Mahindra Scorpio (SUV)'),
		('Toyota Innova Crysta', 'Toyota Innova Crysta (Premium)'),
	)

	full_name       = models.CharField(max_length=100, verbose_name="Full Name")
	phone_number    = models.CharField(max_length=15, verbose_name="Phone Number")
	pickup_location = models.CharField(max_length=150, verbose_name="Pickup Location")
	destination     = models.CharField(max_length=150, verbose_name="Destination / Route")
	car_requirement = models.CharField(
		max_length=100,
		choices=CAR_CHOICES,
		blank=True,
		default='',
		verbose_name="Car Preference"
	)
	message     = models.TextField(blank=True, verbose_name="Additional Message")
	created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Received At")
	is_resolved = models.BooleanField(
		default=False,
		verbose_name="Resolved?",
		help_text="Mark as resolved once the customer has been contacted."
	)

	class Meta:
		ordering = ['-created_at']
		verbose_name = "Booking Enquiry"
		verbose_name_plural = "Booking Enquiries"

	def __str__(self):
		return f"{self.full_name} - {self.destination} ({self.phone_number})"


class SeasonalBanner(models.Model):
	"""Admin-controlled promotional/seasonal announcement banners."""

	title       = models.CharField(max_length=150, verbose_name="Offer Title")
	subtitle    = models.CharField(max_length=250, verbose_name="Subtitle / Offer Details")
	badge_text  = models.CharField(max_length=50, default="Limited Time Offer", verbose_name="Badge Text")
	button_text = models.CharField(max_length=50, default="Book on WhatsApp", verbose_name="Button Text")
	button_url  = models.CharField(
		max_length=500,
		default="https://wa.me/919424489377?text=Hello%20Bobby%20Tour%20and%20Travels,%20I%20am%20interested%20in%20your%20seasonal%20offer!",
		verbose_name="Button Action URL / WhatsApp Link"
	)
	is_active   = models.BooleanField(default=True, verbose_name="Is Active?")
	created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

	class Meta:
		ordering = ['-created_at']
		verbose_name = "Seasonal Banner"
		verbose_name_plural = "Seasonal Banners"

	def __str__(self):
		return self.title

