import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_project.settings')
django.setup()

from django.contrib.auth.models import User
from tour.models import Tour, Region, Activity
from blog.models import Blog, Category
from page.models import Page
from thisapp.models import AppDetail

def run():
    print("Starting database update for Bobby Tour & Travels, Shahdol...")
    admin_user = User.objects.first()

    # 1. Clear old Nepal tours, regions, activities, blogs, and categories
    print("Clearing old Nepal tours, regions, activities, blogs, and categories...")
    Tour.objects.all().delete()
    Region.objects.all().delete()
    Activity.objects.all().delete()
    Blog.objects.all().delete()
    Category.objects.all().delete()

    # Remove old Nepal specific pages
    Page.objects.filter(page_slug__in=[
        'map-reading-course', 'team-building-course', 'kayaking-course-nepal'
    ]).delete()

    # 2. Insert new Activities
    print("Creating new Activities...")
    act_rental = Activity.objects.create(
        activity_title="Car Rental",
        activity_slug="car-rental",
        activity_description="Rent brand new luxury cars in Shahdol including Innova Crysta, Scorpio, Ertiga, and Swift Dzire for local and outstation trips.",
        activity_icon="icon-car",
        activity_image="activities/luxury_cabs.jpg",
        activity_is_active="yes",
        activity_is_featured="yes",
        activity_added_by=admin_user,
        seo_activity_title="Luxury Car Rental Services in Shahdol - Innova & Dzire",
        seo_activity_keywords="car rental shahdol, innova crysta rental shahdol, luxury car hire shahdol, dzire rental",
        seo_activity_description="Best car rental service in Shahdol. Brand new Innova Crysta, Scorpio, Ertiga, and Dzire with verified drivers."
    )

    act_outstation = Activity.objects.create(
        activity_title="Outstation Cabs",
        activity_slug="outstation-cabs",
        activity_description="Reliable 24x7 one-way and roundtrip cab service from Shahdol to Jabalpur, Bhopal, Indore, Rewa, Bilaspur, and Raipur.",
        activity_icon="icon-compass",
        activity_image="activities/luxury_cabs.jpg",
        activity_is_active="yes",
        activity_is_featured="yes",
        activity_added_by=admin_user,
        seo_activity_title="Outstation Cab Service in Shahdol - One-Way & Round Trip",
        seo_activity_keywords="outstation cab shahdol, shahdol to jabalpur taxi, shahdol to bhopal cab, taxi service shahdol",
        seo_activity_description="24x7 outstation cabs from Shahdol to Jabalpur, Bhopal, Indore. On-time pickup, sanitized cars, transparent per km rates."
    )

    act_jungle = Activity.objects.create(
        activity_title="Jungle Safari",
        activity_slug="jungle-safari",
        activity_description="Complete Bandhavgarh National Park tiger safari packages with gypsy booking, expert naturalist, resort stay, and cab transfers.",
        activity_icon="icon-eye",
        activity_image="activities/bandhavgarh.jpg",
        activity_is_active="yes",
        activity_is_featured="yes",
        activity_added_by=admin_user,
        seo_activity_title="Bandhavgarh Jungle Safari Packages & Cab Booking",
        seo_activity_keywords="bandhavgarh safari, jungle safari shahdol, tiger safari bandhavgarh, bandhavgarh taxi",
        seo_activity_description="Book Bandhavgarh tiger safari with luxury cab pickup and drop from Shahdol and Umaria."
    )

    act_pilgrimage = Activity.objects.create(
        activity_title="Pilgrimage Tours",
        activity_slug="pilgrimage-tours",
        activity_description="Spiritual pilgrimage tours to sacred Narmada Udgam in Amarkantak, Mai ki Bagiya, Kapildhara, and Maa Sharda Temple Maihar.",
        activity_icon="icon-heart",
        activity_image="activities/amarkantak.jpg",
        activity_is_active="yes",
        activity_is_featured="yes",
        activity_added_by=admin_user,
        seo_activity_title="Amarkantak & Maihar Pilgrimage Tour Packages from Shahdol",
        seo_activity_keywords="amarkantak tour, narmada udgam tour, maihar sharda mandir cab, pilgrimage taxi shahdol",
        seo_activity_description="Comfortable spiritual tours to holy Amarkantak Narmada Udgam and Maihar Sharda Mandir from Shahdol."
    )

    # 3. Insert new Regions
    print("Creating new Regions...")
    reg_shahdol = Region.objects.create(
        region_title="Shahdol & Nearby",
        region_slug="shahdol-nearby",
        region_description="Shahdol division hub connecting Umaria, Anuppur, Bandhavgarh, and Amarkantak with premier outstation cab services and luxury rentals.",
        region_image="regions/luxury_cabs.jpg",
        region_is_active="yes",
        region_is_featured="yes",
        region_added_by=admin_user,
        seo_region_title="Shahdol & Nearby Travel and Taxi Services",
        seo_region_keywords="shahdol travel, taxi in shahdol, cab hire shahdol, anuppur cab",
        seo_region_description="Premier cab and tour services across Shahdol, Anuppur, Umaria, and surrounding destinations."
    )

    reg_amarkantak = Region.objects.create(
        region_title="Amarkantak",
        region_slug="amarkantak",
        region_description="The revered pilgrim center in Anuppur district where Holy River Narmada, Son, and Johila originate amidst lush Maikal hills.",
        region_image="regions/amarkantak.jpg",
        region_is_active="yes",
        region_is_featured="yes",
        region_added_by=admin_user,
        seo_region_title="Amarkantak Tourism & Cab Services from Shahdol",
        seo_region_keywords="amarkantak tourism, narmada udgam, kapildhara, amarkantak taxi",
        seo_region_description="Visit sacred Amarkantak with comfortable AC cabs from Shahdol and Anuppur."
    )

    reg_bandhavgarh = Region.objects.create(
        region_title="Bandhavgarh",
        region_slug="bandhavgarh",
        region_description="World-renowned tiger reserve in Umaria district near Shahdol, boasting the highest tiger density in India.",
        region_image="regions/bandhavgarh.jpg",
        region_is_active="yes",
        region_is_featured="yes",
        region_added_by=admin_user,
        seo_region_title="Bandhavgarh National Park Tours from Shahdol",
        seo_region_keywords="bandhavgarh national park, tala zone, magadhi zone, bandhavgarh safari taxi",
        seo_region_description="Explore Bandhavgarh Tiger Reserve with prompt cab services and safari packages from Shahdol."
    )

    reg_jabalpur = Region.objects.create(
        region_title="Jabalpur",
        region_slug="jabalpur",
        region_description="Cultural capital of MP famous for Bhedaghat Marble Rocks, Dhuandhar Falls, airport connectivity, and historic ghats.",
        region_image="regions/bhedaghat.jpg",
        region_is_active="yes",
        region_is_featured="yes",
        region_added_by=admin_user,
        seo_region_title="Jabalpur & Bhedaghat Outstation Cabs from Shahdol",
        seo_region_keywords="shahdol to jabalpur cab, bhedaghat marble rocks, dhuandhar falls, jabalpur airport taxi",
        seo_region_description="One-way and roundtrip cabs between Shahdol and Jabalpur. Marble Rocks & Dhuandhar tour packages."
    )

    reg_bhopal_indore = Region.objects.create(
        region_title="Bhopal / Indore",
        region_slug="bhopal-indore",
        region_description="Major metropolitan routes from Shahdol with premium highway cab connectivity, punctual pickups, and night drops.",
        region_image="regions/luxury_cabs.jpg",
        region_is_active="yes",
        region_is_featured="yes",
        region_added_by=admin_user,
        seo_region_title="Shahdol to Bhopal & Indore Outstation Cab Services",
        seo_region_keywords="shahdol to bhopal cab, shahdol to indore taxi, outstation luxury taxi mp",
        seo_region_description="Safe and comfortable long-distance outstation cabs from Shahdol to Bhopal and Indore."
    )

    # 4. Insert new Tours
    print("Creating new Tours...")
    t1 = Tour.objects.create(
        tour_title="Bandhavgarh Jungle Tiger Safari",
        tour_slug="bandhavgarh-jungle-tiger-safari",
        tour_duration=2,
        tour_altitude=800,
        tour_difficulty="easy",
        tour_description="""<h3>Starting Price: ₹4,500</h3>
<p>Complete jungle gypsy safari and luxury cab roundtrip from Shahdol. Experience the thrill of spotting Royal Bengal Tigers in the renowned Bandhavgarh National Park (Tala, Magadhi, and Khitauli zones).</p>
<p><strong>Package Inclusions:</strong></p>
<ul>
    <li>Sanitized AC cab roundtrip from Shahdol / Umaria in Innova Crysta / Ertiga / Dzire</li>
    <li>Jungle Gypsy Safari permit assistance and zone guide coordination</li>
    <li>Resort booking assistance in Tala / Magadhi</li>
    <li>24x7 helpline & verified driver</li>
</ul>
<p><strong>Hotline:</strong> <a href="tel:+919424489377">+91 9424489377</a></p>""",
        tour_image="tours/bandhavgarh.jpg",
        tour_activity=act_jungle,
        tour_is_active="yes",
        tour_is_featured="yes",
        tour_added_by=admin_user,
        seo_tour_title="Bandhavgarh Jungle Tiger Safari from Shahdol - ₹4,500",
        seo_tour_keywords="bandhavgarh safari, tiger safari tour, shahdol to bandhavgarh taxi, safari package",
        seo_tour_description="Book Bandhavgarh tiger safari and luxury cab roundtrip from Shahdol starting at ₹4,500."
    )
    t1.tour_region.add(reg_bandhavgarh, reg_shahdol)

    t2 = Tour.objects.create(
        tour_title="Amarkantak Teerth & Narmada Udgam Tour",
        tour_slug="amarkantak-teerth-narmada-udgam-tour",
        tour_duration=1,
        tour_altitude=1048,
        tour_difficulty="easy",
        tour_description="""<h3>Starting Price: ₹3,200</h3>
<p>Holy darshan of Narmada Udgam, Mai ki Bagiya, Kapildhara, and Dudh Dhara with AC Innova Crysta / Dzire. The sacred origin of Holy River Narmada nestled in the peaceful Maikal Hills.</p>
<p><strong>Package Inclusions:</strong></p>
<ul>
    <li>Doorstep pickup and drop from Shahdol & Anuppur</li>
    <li>Narmada Kund & Mandir complex holy darshan</li>
    <li>Kapildhara & Dudh Dhara scenic waterfalls</li>
    <li>Mai ki Bagiya & Ancient Kalachuri Temples visit</li>
    <li>Clean, comfortable AC cab with experienced courteous driver</li>
</ul>
<p><strong>Hotline:</strong> <a href="tel:+919424489377">+91 9424489377</a></p>""",
        tour_image="tours/amarkantak.jpg",
        tour_activity=act_pilgrimage,
        tour_is_active="yes",
        tour_is_featured="yes",
        tour_added_by=admin_user,
        seo_tour_title="Amarkantak Narmada Udgam Tour from Shahdol - ₹3,200",
        seo_tour_keywords="amarkantak tour, narmada udgam darshan, shahdol to amarkantak cab, kapildhara waterfall",
        seo_tour_description="Holy Amarkantak teerth tour package with AC cab pickup from Shahdol starting at ₹3,200."
    )
    t2.tour_region.add(reg_amarkantak, reg_shahdol)

    t3 = Tour.objects.create(
        tour_title="Bhedaghat Marble Rocks & Dhuandhar Tour",
        tour_slug="bhedaghat-marble-rocks-dhuandhar-tour",
        tour_duration=1,
        tour_altitude=411,
        tour_difficulty="easy",
        tour_description="""<h3>Starting Price: ₹4,000</h3>
<p>Boating in soaring marble rocks along the Narmada River, majestic Dhuandhar waterfall view, Chausath Yogini Temple, and comfortable outstation pickup/drop from Shahdol.</p>
<p><strong>Package Inclusions:</strong></p>
<ul>
    <li>Outstation pickup and drop anywhere in Shahdol / Umaria</li>
    <li>Boating amidst world-famous Marble Rocks at Bhedaghat</li>
    <li>Spectacular Dhuandhar Waterfall roar and photography stops</li>
    <li>Optional Rani Durgavati Fort / Jabalpur sightseeing</li>
    <li>Experienced highway driver for a smooth family trip</li>
</ul>
<p><strong>Hotline:</strong> <a href="tel:+919424489377">+91 9424489377</a></p>""",
        tour_image="tours/bhedaghat.jpg",
        tour_activity=act_outstation,
        tour_is_active="yes",
        tour_is_featured="yes",
        tour_added_by=admin_user,
        seo_tour_title="Bhedaghat Marble Rocks & Dhuandhar Tour from Shahdol - ₹4,000",
        seo_tour_keywords="bhedaghat tour, dhuandhar falls, shahdol to jabalpur cab, marble rocks boating",
        seo_tour_description="Book Bhedaghat marble rocks and Dhuandhar waterfall tour from Shahdol starting at ₹4,000."
    )
    t3.tour_region.add(reg_jabalpur, reg_shahdol)

    t4 = Tour.objects.create(
        tour_title="Shahdol to Indore / Bhopal / Jabalpur One-Way & Round Cabs",
        tour_slug="shahdol-indore-bhopal-jabalpur-cabs",
        tour_duration=1,
        tour_altitude=500,
        tour_difficulty="easy",
        tour_description="""<h3>Starting Price: ₹12/km</h3>
<p>24x7 Verified drivers, brand new luxury cars (Innova Crysta, Scorpio, Dzire, Ertiga). Prompt on-time pickup from anywhere in Shahdol, Anuppur, Umaria to Jabalpur Airport/Railway Station, Bhopal, and Indore.</p>
<p><strong>Service Highlights:</strong></p>
<ul>
    <li>Fleet: Innova Crysta, Scorpio-N, Ertiga, Swift Dzire</li>
    <li>24x7 service for emergency, medical, wedding, and business travel</li>
    <li>Transparent per-km billing starting at ₹12/km</li>
    <li>Well-maintained, sanitized, GPS-tracked vehicles with AC</li>
</ul>
<p><strong>Hotline:</strong> <a href="tel:+919424489377">+91 9424489377</a></p>""",
        tour_image="tours/luxury_cabs.jpg",
        tour_activity=act_rental,
        tour_is_active="yes",
        tour_is_featured="yes",
        tour_added_by=admin_user,
        seo_tour_title="Shahdol to Indore / Bhopal / Jabalpur Outstation Cabs - ₹12/km",
        seo_tour_keywords="shahdol to bhopal taxi, shahdol to indore cab, innova crysta rental shahdol, outstation cab rate",
        seo_tour_description="24x7 outstation cabs from Shahdol to Jabalpur, Bhopal, and Indore starting at ₹12/km."
    )
    t4.tour_region.add(reg_bhopal_indore, reg_jabalpur, reg_shahdol)

    # 5. Insert Categories and Blogs
    print("Creating new Blogs & Categories...")
    cat_travel = Category.objects.create(
        category_title="Travel & Cabs",
        category_slug="travel-and-cabs",
        category_description="Travel tips, route guides, and cab rental updates from Bobby Tour & Travels.",
        category_is_active="yes",
        category_added_by=admin_user
    )

    b1 = Blog.objects.create(
        blog_title="Top Places to Visit Near Shahdol: Bandhavgarh, Amarkantak & Beyond",
        blog_slug="top-places-near-shahdol",
        blog_description="<p>Shahdol is blessed with proximity to some of Central India's finest destinations. From the thrilling Royal Bengal Tiger sightings in Bandhavgarh National Park to the serene, spiritual beauty of Narmada Udgam in Amarkantak, explore the best weekend road trips with Bobby Tour & Travels.</p>",
        blog_image="blogs/bandhavgarh.jpg",
        blog_is_active="yes",
        blog_is_featured="yes",
        blog_added_by=admin_user,
        seo_blog_title="Top Places to Visit Near Shahdol - Travel Guide",
        seo_blog_description="Explore top weekend destinations near Shahdol including Bandhavgarh and Amarkantak with luxury cab rentals."
    )
    b1.blog_category.add(cat_travel)

    b2 = Blog.objects.create(
        blog_title="Why Choose Innova Crysta for Your Outstation Trip from Shahdol?",
        blog_slug="why-choose-innova-crysta-shahdol",
        blog_description="<p>When planning a long-distance road trip from Shahdol to Bhopal, Indore, or Jabalpur, comfort, safety, and reliability are non-negotiable. Learn why the Toyota Innova Crysta remains the undisputed king of MP highways for family and corporate travel.</p>",
        blog_image="blogs/luxury_cabs.jpg",
        blog_is_active="yes",
        blog_is_featured="yes",
        blog_added_by=admin_user,
        seo_blog_title="Why Choose Innova Crysta for Outstation Trips from Shahdol",
        seo_blog_description="Discover why Innova Crysta is the best choice for outstation road trips from Shahdol."
    )
    b2.blog_category.add(cat_travel)

    b3 = Blog.objects.create(
        blog_title="Complete Guide to Bandhavgarh Tiger Safari from Shahdol",
        blog_slug="complete-guide-bandhavgarh-safari-shahdol",
        blog_description="<p>Bandhavgarh National Park is just a scenic 2-hour drive from Shahdol. Read our comprehensive guide on safari timings, Tala and Magadhi zone bookings, gypsy permits, and best luxury cab options for a seamless wildlife adventure.</p>",
        blog_image="blogs/bandhavgarh.jpg",
        blog_is_active="yes",
        blog_is_featured="yes",
        blog_added_by=admin_user,
        seo_blog_title="Complete Guide to Bandhavgarh Safari from Shahdol",
        seo_blog_description="Everything you need to know about planning a Bandhavgarh tiger safari from Shahdol."
    )
    b3.blog_category.add(cat_travel)

    # 6. Update AppDetail & About Us Page
    print("Updating AppDetail & About Us Page...")
    app = AppDetail.objects.first()
    if not app:
        app = AppDetail()
    app.app_name = "Bobby Tour & Travels"
    app.app_title = "Shahdol Outstation Cabs & Luxury Car Rental"
    app.app_description = "About Bobby Tour & Travels: Trusted car rental and outstation cab provider in Shahdol and Anuppur since decades. Providing brand new luxury cars (Innova Crysta, Scorpio, Swift, Ertiga) for outstation trips, local sightseeing, weddings, and Bandhavgarh jungle safaris."
    app.app_keywords = "Bobby Tour and Travels, Shahdol cab service, car rental Shahdol, outstation taxi Shahdol, Bandhavgarh cab, Amarkantak taxi, Innova Crysta rental Shahdol"
    app.app_email = "bobbytourstravels@gmail.com"
    app.app_contact = "+919424489377"
    app.app_address = "Shahdol, Madhya Pradesh"
    app.app_postal = "484001"
    app.whatsapp_booking = "yes"
    app.developed_by = "Bobby Tour & Travels"
    app.app_logo = "bobby-logo.png"
    app.app_icon = "bobby-favicon.png"
    app.save()

    about_page = Page.objects.filter(page_slug="about-us").first()
    if about_page:
        about_page.page_title = "About Bobby Tour & Travels"
        about_page.page_description = """<h2>Welcome to Bobby Tour & Travels, Shahdol</h2>
<p>Bobby Tour & Travels is Shahdol's premier car rental and outstation cab provider, serving travelers, corporate clients, families, and pilgrims across Madhya Pradesh for decades.</p>
<p>We take immense pride in our brand new luxury fleet comprising Toyota Innova Crysta, Mahindra Scorpio-N, Maruti Ertiga, and Swift Dzire. All our vehicles are equipped with top-tier comfort features, GPS safety tracking, chilled AC, and are operated by courteous, verified professional chauffeurs.</p>
<h3>Our Specializations:</h3>
<ul>
    <li><strong>24x7 Outstation Cabs:</strong> Punctual one-way and roundtrip cabs from Shahdol to Jabalpur, Bhopal, Indore, Bilaspur, Rewa, and Raipur.</li>
    <li><strong>Wildlife Safaris:</strong> Customized Bandhavgarh National Park tiger safari packages with luxury cab transfers and gypsy coordination.</li>
    <li><strong>Spiritual Teerth Yatras:</strong> Holy pilgrimage tours to Amarkantak (Narmada Udgam), Maihar Sharda Mandir, and Bhedaghat Marble Rocks.</li>
    <li><strong>Wedding & VIP Car Rentals:</strong> Premium decorated luxury cars for wedding processions and VIP corporate guests.</li>
</ul>
<p><strong>Contact Us:</strong> Call <a href="tel:+919424489377">+91 9424489377</a> or WhatsApp us 24x7 for instant booking and transparent rates.</p>"""
        about_page.save()

    print("Database update completed successfully!")

if __name__ == '__main__':
    run()
