# Digital Notice Board - Django Admin Panel
# ડિજિટલ નોટિસ બોર્ડ - Django Admin Panel

## Overview / સંક્ષિપ્ત માહિતી

આ એક complete Django application છે જેમાં admin panel દ્વારા notices manage થાય છે.

## Key Features / મુખ્ય સુવિધાઓ

### Admin Features (Admin માટે):
- ✅ Notice add કરો (text, photo, PDF)
- ✅ Notice update કરો
- ✅ Notice delete કરો
- ✅ Photo અને PDF upload કરો
- ✅ Expiry date set કરો
- ✅ Notice નો રંગ અને pin color પસંદ કરો
- ✅ Notices ને active/inactive કરો

### User Features (User માટે):
- ✅ બધા active notices જુઓ
- ✅ Photo અને PDF download કરો
- ✅ Expired notices automatically છુપાય છે

## Quick Start / ઝડપથી શરૂઆત

1. **Install Dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Setup Database:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create Admin User:**
   ```bash
   python manage.py createsuperuser
   ```

   Example credentials:
   - Username: `admin`
   - Email: `admin@example.com`
   - Password: `admin123` (તમારું પોતાનું password રાખો)

4. **Start Server:**
   ```bash
   python manage.py runserver
   ```

5. **Access:**
   - User View: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Admin Panel Usage / Admin Panel નો ઉપયોગ

### Login:
1. http://127.0.0.1:8000/admin/ પર જાઓ
2. Username અને Password નાખો
3. Login કરો

### Add New Notice:
1. "Notices" પર ક્લિક કરો
2. "Add Notice" બટન દબાવો
3. Form ભરો:
   - Title: Notice નું શીર્ષક
   - Description: Notice ની વિગત
   - Notice Type: Text/Image/PDF
   - File: Photo અથવા PDF (optional)
   - Color: Notice નો background color
   - Pin Color: Pin નો color
   - Expiry Date: Notice ક્યારે expire થશે
   - Is Active: Notice display થાય કે નહીં
4. "Save" દબાવો

### Update Notice:
1. Notice list માંથી notice પર ક્લિક કરો
2. Changes કરો
3. "Save" દબાવો

### Delete Notice:
1. Notice select કરો
2. Action dropdown માંથી "Delete" પસંદ કરો
3. "Go" દબાવો અને confirm કરો

## Technical Details / ટેકનિકલ વિગતો

- **Framework**: Django 4.2
- **Database**: SQLite (default)
- **File Storage**: Local media folder
- **Admin Interface**: Django Admin (Gujarati + English)
- **Frontend**: HTML, CSS, JavaScript with Django templates

## File Upload Support / ફાઈલ અપલોડ સપોર્ટ

- **Images**: JPG, JPEG, PNG, GIF, WEBP
- **Documents**: PDF
- **Storage**: `/backend/media/uploads/`

## Security Features / સુરક્ષા સુવિધાઓ

- Admin panel માત્ર authorized users માટે
- Password protection
- File upload validation
- Automatic expired notice filtering

## Default Admin Credentials / Default Admin Login

⚠️ **Important**: તમારે પહેલી વાર admin user બનાવવાનું રહેશે.

Run this command:
```bash
python manage.py createsuperuser
```

Then create your credentials:
- Username: તમારું નામ (example: `admin`)
- Email: તમારું email
- Password: મજબૂત password રાખો

## Full Documentation

વધુ વિગતવાર માહિતી માટે `SETUP_INSTRUCTIONS.md` જુઓ.

---

**Created with Django** | **Made in Gujarat, India**
