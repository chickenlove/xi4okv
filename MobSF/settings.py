"""
Django settings for MobSF project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os,platform
import java, vbox
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

#Based on https://gist.github.com/ndarville/3452907#file-secret-key-gen-py
#SECRET_KEY = '#r$=rg*lit&!4nukg++@%k+n9#6fhkv_*a6)2t$n1b=*wpvptl'

try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(BASE_DIR, "MobSF/secret")
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            import random
            SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters \
            to generate your secret key!' % SECRET_FILE)

# SECURITY WARNING: don't run with debug turned on in production!
# ^ This is fine Do not turn it off untill MobSF framework moves from Beta to Stable
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'StaticAnalyzer',
    'DynamicAnalyzer',
    'MobSF',
    'APITester',
    'MalwareAnalyzer',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'MobSF.urls'

WSGI_APPLICATION = 'MobSF.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/uploads/'
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates'),
    )
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static/'),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_URL = '/static/'
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
MOBSF_VER = "v0.9.2 Beta"

if platform.system()=="Windows":
    print '\n\nMobile Security Framework '+ MOBSF_VER
else:
    print '\n\n\033[1m\033[34mMobile Security Framework '+ MOBSF_VER +'\033[0m'

# DO NOT EDIT ANYTHING ABOVE THIS
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#Logs Directory
LOG_DIR=os.path.join(BASE_DIR,'logs/')
#Static Directory
STATIC_DIR=os.path.join(BASE_DIR,'static/')
#Download Directory
DWD_DIR=os.path.join(STATIC_DIR, 'downloads/')
#Upload Directory
UPLD_DIR=os.path.join(BASE_DIR,'uploads/')
#Database Directory
DB_DIR = os.path.join(BASE_DIR, 'db.sqlite3')

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DB_DIR,
    }
}

#==========DECOMPILER SETTINGS================
DECOMPILER = "jd-core"

#Two Decompilers are available 
#1. jd-core
#2. cfr
#==============================================

#==========Dex to Jar Converter================
JAR_CONVERTER = "d2j"
#Two dex to jar converters are available 
#1. d2j
#2. enjarify
'''
enjarify requires python3. Install Python 3 and add the path to environment variable 
PATH or provide the Python 3 path to PYTHON3_PATH variable in settings.py
ex: PYTHON3_PATH = "C:/Users/<user>/AppData/Local/Programs/Python/Python35-32/"
'''
PYTHON3_PATH = ""
#==============================================

#============JAVA SETTINGS=====================
JAVA_PATH=java.FindJava()

#Sample Java Path
#Windows - JAVA_PATH='C:/Program Files/Java/jdk1.7.0_17/bin/'  
#OSX and Linux - JAVA_PATH='/usr/bin/'
#===============================================

#==========SKIP CLASSES==========================
SKIP_CLASSES = ['android/support/','com/google/','android/content/','com/android/',
'com/facebook/','com/twitter/','twitter4j/','org/apache/','com/squareup/okhttp/',
'oauth/signpost/','org/chromium/']
#================================================

#===============DEVICE Settings=================
REAL_DEVICE = False
DEVICE_IP = '192.168.56.101'
DEVICE_ADB_PORT = 5555
DEVICE_TIMEOUT = 300
#===============================================

#================VirtualBox Settings============
if REAL_DEVICE == False:
    if platform.system()=="Windows":
        VBOX='C:\Program Files\Oracle\VirtualBox\VBoxManage.exe'
        #Path to VBoxManage.exe
    else:
        VBOX=vbox.FindVbox()
        #Path to VBoxManage in Linux/OSX
#===============================================

#================VM SETTINGS ==================
#VM UUID
UUID='1a83a753-d448-4dfe-8bce-7fd194e4d634'
#Snapshot UUID
SUUID='3bff4dee-655a-4f3d-aade-b90b478c9e6d'
#IP of the MobSF VM
VM_IP='192.168.56.101'
VM_ADB_PORT = 5555
VM_TIMEOUT = 100
#=============================================

#================HOST/PROXY SETTINGS ===========
PROXY_IP='192.168.56.1' #Host/Server/Proxy IP
PORT=1337 #Proxy Port
ROOT_CA='0025aabb.0'

SCREEN_IP = PROXY_IP #ScreenCast IP
SCREEN_PORT = 9339 #ScreenCast Port
#===============================================

#===============UPSTREAM PROXY==================
#If you are behind a Proxy
UPSTREAM_PROXY_IP = None
UPSTREAM_PROXY_PORT = None
UPSTREAM_PROXY_USERNAME = None
UPSTREAM_PROXY_PASSWORD = None
#===============================================

#=========Path Traversal - API Testing==========
CHECK_FILE = "/etc/passwd"
RESPONSE_REGEX = "root:|nobody:"
#===============================================

#=========Rate Limit Check - API Testing========
RATE_REGISTER = 20
RATE_LOGIN = 20
#===============================================

#===============MobSF Cloud Settings============
CLOUD_SERVER = 'http://opensecurity.in:8080'
'''
This server validates SSRF and XXE during Web API Testing
See the source code of the cloud server from APITester/cloud/cloud_server.py
You can also host the cloud server. Host it on a public IP and point CLOUD_SERVER to that IP.
'''
#===============================================



