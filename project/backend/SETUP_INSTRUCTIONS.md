# Django Notice Board - Setup Instructions
# ડિજિટલ નોટિસ બોર્ડ - સેટઅપ સૂચનાઓ

## Requirements / જરૂરીયાતો

- Python 3.8 or higher
- Django 4.2
- Pillow (for image handling)

## Installation Steps / ઇન્સ્ટોલેશન સ્ટેપ્સ

### 1. Install Python Dependencies / Python Dependencies ઇન્સ્ટોલ કરો

```bash
cd backend
pip install -r requirements.txt
```

Or if using pip3:
```bash
pip3 install -r requirements.txt
```

### 2. Run Database Migrations / Database Migrations ચલાવો

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Admin User / Admin User બનાવો

```bash
python manage.py createsuperuser
```

તમને પૂછવામાં આવશે:
- Username: તમારું નામ લખો (example: admin)
- Email: તમારું email લખો (example: admin@example.com)
- Password: પાસવર્ડ બે વાર લખો

**Important:** Password આપતી વખતે screen પર કંઈ દેખાશે નહીં, પણ તે લખાઈ રહ્યું છે.

### 4. Start Development Server / Server શરૂ કરો

```bash
python manage.py runserver
```

Server આ address પર ચાલશે: http://127.0.0.1:8000/

## Usage / ઉપયોગ

### Admin Panel માં Login કરવું

1. Browser માં આ URL ખોલો: http://127.0.0.1:8000/admin/
2. તમારું username અને password નાખો
3. Login કરો

### Notice Add કરવું

1. Admin panel માં login કર્યા પછી "Notices" પર ક્લિક કરો
2. "Add Notice" બટન પર ક્લિક કરો
3. આ માહિતી ભરો:
   - **Title (શીર્ષક)**: Notice નું શીર્ષક
   - **Description (વર્ણન)**: Notice ની વિગતવાર માહિતી
   - **Notice Type**: Text, Image, અથવા PDF
   - **File**: Photo અથવા PDF upload કરો (optional)
   - **Color**: Notice નો રંગ પસંદ કરો
   - **Pin Color**: Pin નો રંગ પસંદ કરો
   - **Expiry Date**: કયા દિવસે notice expire થવું જોઈએ
   - **Is Active**: Notice દેખાડવું છે કે નહીં
4. "Save" બટન દબાવો

### Notice Update કરવું

1. Admin panel માં "Notices" પર ક્લિક કરો
2. જે notice update કરવું હોય તેના પર ક્લિક કરો
3. માહિતી બદલો
4. "Save" બટન દબાવો

### Notice Delete કરવું

1. Admin panel માં "Notices" પર ક્લિક કરો
2. જે notice delete કરવું હોય તેની બાજુમાં checkbox સિલેક્ટ કરો
3. ઉપર "Action" dropdown માંથી "Delete selected notices" પસંદ કરો
4. "Go" બટન દબાવો
5. Confirm કરો

### User View

User આ URL પર જઈને બધા active notices જોઈ શકે છે:
http://127.0.0.1:8000/

- User માત્ર જોઈ શકે છે
- Photo અને PDF download કરી શકે છે
- કોઈ changes કરી શકતા નથી

## Admin Login Credentials (Example)

After running `createsuperuser`, you might create:

- **Username**: admin
- **Password**: admin123 (તમે તમારું પોતાનું password રાખો)

## Features / સુવિધાઓ

1. ✅ Admin panel દ્વારા notices add/update/delete
2. ✅ Photo અને PDF upload
3. ✅ Expiry date સાથે automatic filtering
4. ✅ User માટે download option
5. ✅ Beautiful notice board design
6. ✅ Gujarati + English support

## File Structure / ફાઈલ સ્ટ્રક્ચર

```
backend/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3               # Database (created after migration)
├── my_django_project/       # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── notices/                 # Notices app
│   ├── models.py           # Notice database model
│   ├── admin.py            # Admin panel configuration
│   ├── views.py            # User views
│   └── urls.py
├── templates/              # HTML templates
│   └── index.html
├── static/                 # CSS, JS, Images
│   └── css/
│       └── custom.css
└── media/                  # Uploaded files
    └── uploads/           # Photos and PDFs
```

## Troubleshooting / સમસ્યા નિવારણ

### "Module not found" error મળે તો:
```bash
pip install -r requirements.txt
```

### Database error આવે તો:
```bash
python manage.py migrate --run-syncdb
```

### Admin login નથી થઈ રહ્યું તો:
નવું superuser બનાવો:
```bash
python manage.py createsuperuser
```

## Support

કોઈ પણ સમસ્યા માટે SETUP_INSTRUCTIONS.md file ફરીથી વાંચો.
