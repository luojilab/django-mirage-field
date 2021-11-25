# base64.urlsafe_encode('django-mirage-field have fun')
SECRET_KEY = "ZGphbmdvLW1pcmFnZS1maWVsZCBoYXZlIGZ1bg=="

DEBUG = True
STATIC_URL = "/static/"
ROOT_URLCONF = "urls"

MIRAGE_SECRET_KEY = "MIRAGE_SECRET_KEYMIRAGE_SECRET_KEY"
MIRAGE_CIPHER_MODE = "CBC"
MIRAGE_CIPHER_IV = "1234567890abcdef"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps',
    'mirage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
