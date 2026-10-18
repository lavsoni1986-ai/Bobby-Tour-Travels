from django.contrib import admin
from .models import Activity, Region, Tour, BookingEnquiry, SeasonalBanner



class ActivityAdmin(admin.ModelAdmin):
	list_display = ('activity_title', 'activity_slug', 'activity_is_active', 'activity_is_featured', 'activity_added_by')
	list_editable = ('activity_slug', 'activity_is_active', 'activity_is_featured')
	list_filter = ('activity_created_at', 'activity_is_active')
	list_per_page = 10
	search_fields = ('activity_title', 'activity_description')
	prepopulated_fields = {"activity_slug": ("activity_title", )}


class RegionAdmin(admin.ModelAdmin):
	list_display = ('region_title', 'region_slug', 'region_is_active', 'region_is_featured', 'region_added_by')
	list_editable = ('region_slug', 'region_is_active', 'region_is_featured')
	list_filter = ('region_created_at', 'region_is_active')
	list_per_page = 10
	search_fields = ('region_title', 'region_description')
	prepopulated_fields = {"region_slug": ("region_title", )}


class TourAdmin(admin.ModelAdmin):
	list_display = ('tour_title', 'starting_price', 'tour_slug', 'tour_is_active', 'tour_is_featured', 'tour_added_by')
	list_editable = ('starting_price', 'tour_slug', 'tour_is_active', 'tour_is_featured')
	list_per_page = 10
	list_filter = ('tour_created_at', 'tour_is_active')
	search_fields = ('tour_title', 'starting_price', 'tour_description')
	prepopulated_fields = {"tour_slug": ("tour_title", )}


@admin.register(BookingEnquiry)
class BookingEnquiryAdmin(admin.ModelAdmin):
	list_display  = ('full_name', 'phone_number', 'pickup_location', 'destination', 'car_requirement', 'created_at', 'is_resolved')
	list_filter   = ('is_resolved', 'created_at', 'car_requirement')
	list_editable = ('is_resolved',)
	search_fields = ('full_name', 'phone_number', 'pickup_location', 'destination', 'message')
	date_hierarchy = 'created_at'
	list_per_page = 25
	readonly_fields = ('created_at',)
	fieldsets = (
		('Customer Details', {
			'fields': ('full_name', 'phone_number')
		}),
		('Trip Details', {
			'fields': ('pickup_location', 'destination', 'car_requirement', 'message')
		}),
		('Status', {
			'fields': ('is_resolved', 'created_at')
		}),
	)


# Register your models here.
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Tour, TourAdmin)


@admin.register(SeasonalBanner)
class SeasonalBannerAdmin(admin.ModelAdmin):
	list_display = ('title', 'badge_text', 'is_active', 'created_at')
	list_editable = ('is_active',)
	list_filter = ('is_active', 'created_at')
	search_fields = ('title', 'subtitle', 'badge_text')
	list_per_page = 15
