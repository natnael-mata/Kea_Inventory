# Deployment Guide: PythonAnywhere

This guide provides step-by-step instructions for deploying the **Kea Inventory** project to PythonAnywhere.

## 1. Prepare Your Repository
Ensure all latest changes are pushed to your GitHub repository:
```bash
git add .
git commit -m "chore: prepare for deployment"
git push origin master
```

## 2. PythonAnywhere Terminal Setup

### Clone the Repository
Open a **Bash Console** on PythonAnywhere and run:
```bash
git clone https://github.com/natnael-mata/Kea_Inventory.git
cd Kea_Inventory
```

### Create a Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.10 kea-venv
pip install -r requirements.txt
```

## 3. Database Setup (MySQL)
1. Go to the **Databases** tab on PythonAnywhere.
2. Initialize MySQL if you haven't (set a password).
3. Create a new database named `KEA_INV_DB`.
4. Note your **Host address** (e.g., `yourusername.mysql.pythonanywhere-services.com`).

## 4. Web App Configuration
Go to the **Web** tab and click **Add a new web app**.
1. Choose **Manual configuration** (not Django) and select **Python 3.10**.
2. **Virtualenv**: Enter the path to your created environment (e.g., `/home/yourusername/.virtualenvs/kea-venv`).
3. **Static Files**: Add an entry:
   - URL: `/static/`
   - Path: `/home/yourusername/Kea_Inventory/staticfiles/`

### Edit WSGI Configuration
In the **Web** tab, click the link to your WSGI configuration file and replace its content with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/Kea_Inventory'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Kea_Inventory.settings'

# Set environment variables for DB and Secret Key
os.environ['SECRET_KEY'] = 'your-secret-key'
os.environ['DB_NAME'] = 'yourusername$KEA_INV_DB'
os.environ['DB_USER'] = 'yourusername'
os.environ['DB_PASSWORD'] = 'your-db-password'
os.environ['DB_HOST'] = 'yourusername.mysql.pythonanywhere-services.com'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## 5. Finalize Deployment
In your PythonAnywhere Bash console:
```bash
python manage.py collectstatic
python manage.py migrate
```

Go back to the **Web** tab and click **Reload**. Your site should now be live!
