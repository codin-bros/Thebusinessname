# config.py
business = {
    "name": "Fresh Fade Barbers",
    "tagline": "Sharp Cuts. Clean Style.",
    "description": "Family-owned barber shop offering classic and modern cuts and shaves.",
    "domain": "www.freshfadebarbers.com",
    "email": "bookings@freshfadebarbers.com",
    "phone": "(555) 123-4567",
    "address": "123 Main Street, Springfield, IL 62701",
    "hours": [
        {"days": "Mon–Fri", "hours": "9:00 AM – 7:00 PM"},
        {"days": "Sat", "hours": "9:00 AM – 5:00 PM"},
        {"days": "Sun", "hours": "Closed"},
    ],

    # Theme
    "primary_color": "#111111",
    "secondary_color": "#C59D5F",
    "accent_color": "#FFFFFF",
    "gradient_start": "#111111",
    "gradient_end": "#333333",

    # Services
    "services": [
        {"name": "Haircut", "price": "$25", "desc": "Classic & modern cuts."},
        {"name": "Beard Trim", "price": "$15", "desc": "Clean lines & shape."},
        {"name": "Kids Cut", "price": "$20", "desc": "Under 12 years old."},
        {"name": "Hot Towel Shave", "price": "$30", "desc": "Traditional relaxing shave."},
        {"name": "Hot Towel Shave", "price": "$300", "desc": "Traditional relaxing shave."},
    ],

    # Appointments
    "appointment_link": "",
    "use_internal_booking_form": True,

    # Map & social
    "google_maps_embed": "",
    "social": {
        "instagram": "",
        "facebook": "",
        "tiktok": ""
    },

    # SEO
    "seo_title": "Fresh Fade Barbers | Classic & Modern Haircuts",
    "seo_description": "Sharp cuts, clean style. Walk-ins welcome. Book your appointment online.",
    "analytics_id": ""
}
