EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "jhonazsh.17@gmail.com"
EMAIL_HOST_PASSWORD = "octubre6"
EMAIL_PORT = 587

from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = '4b&f#3f0le-+u(c8u6+n!pe@6vp)&nbh!pj+8#_e8b=vs$gb-u'

DJANGO_APPS = (
            'django_admin_bootstrapped.bootstrap3',
            'django_admin_bootstrapped',
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        )

THIRD_PARTY_APPS = (

        )

LOCAL_APPS = (
            'apps.home',
            'apps.projects',
            'apps.services',
            'apps.sectors',
            'apps.team',
            'apps.licenses',
            'apps.awards',
        )

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'srs.urls'

WSGI_APPLICATION = 'srs.wsgi.application'