#-*- coding:utf8 -*-
"""
Django settings for djStat project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$r4)f_8p^$@voa81ebp1km^$1t6v0$up^xqg!3&@x0q(@a1)f0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#templates directory
TEMPLATE_DIRS = (
		os.path.join(os.path.dirname(__file__),'templates').replace('\\','/'),
)
# Application definition

INSTALLED_APPS = (
	'grappelli',
	'filebrowser',#文件浏览器
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'djStat.dbmgr',
	'djStat.g168',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',#让admin显示为中文界面
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djStat.urls'

WSGI_APPLICATION = 'djStat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		'ENGINE':'django.db.backends.mysql',
		'NAME':'pydb',
		'USER':'root',
		'PASSWORD':'123456',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#用户上传的文件保存目录
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/').replace('\\','/')
MEDIA_URL = "/media/"
#css,js,Images保存目录
STATIC_ROOT = os.path.join(BASE_DIR,'static/').replace('\\','/')
STATIC_URL = "/static/"
#把每个APP下的static目录添加到下面元组
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'djStat/dbmgr/static/').replace('\\','/'),)
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'djStat/g168/static/').replace('\\','/'),)


