# -*- coding: utf-8 -*-

import os.path, sys, os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

APPEND_SLASH = False
ALLOWED_HOSTS = ["*"]

ADMINS = (
    ("Admin", "example@example.com"),
)

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "tina",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake"
    }
}

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
]

# Default configuration for reverse proxy
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

# Errors report configuration
SEND_BROKEN_LINK_EMAILS = True
IGNORABLE_404_ENDS = (".php", ".cgi")
IGNORABLE_404_STARTS = ("/phpmyadmin/",)

ATOMIC_REQUESTS = True
TIME_ZONE = "UTC"
LOGIN_URL="/auth/login/"
USE_TZ = True

USE_I18N = True
USE_L10N = True
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'vi'

# Languages we provide translations for, out of the box.
LANGUAGES = [
    #("af", "Afrikaans"),  # Afrikaans
    #("ar", "العربية‏"),  # Arabic
    #("ast", "Asturiano"),  # Asturian
    #("az", "Azərbaycan dili"),  # Azerbaijani
    #("bg", "Български"),  # Bulgarian
    #("be", "Беларуская"),  # Belarusian
    #("bn", "বাংলা"),  # Bengali
    #("br", "Bretón"),  # Breton
    #("bs", "Bosanski"),  # Bosnian
    # ("ca", "Català"),  # Catalan
    #("cs", "Čeština"),  # Czech
    #("cy", "Cymraeg"),  # Welsh
    #("da", "Dansk"),  # Danish
    # ("de", "Deutsch"),  # German
    #("el", "Ελληνικά"),  # Greek
    ("en", "English (US)"),  # English
    #("en-au", "English (Australia)"),  # Australian English
    #("en-gb", "English (UK)"),  # British English
    #("eo", "esperanta"),  # Esperanto
    # ("es", "Español"),  # Spanish
    #("es-ar", "Español (Argentina)"),  # Argentinian Spanish
    #("es-mx", "Español (México)"),  # Mexican Spanish
    #("es-ni", "Español (Nicaragua)"),  # Nicaraguan Spanish
    #("es-ve", "Español (Venezuela)"),  # Venezuelan Spanish
    #("et", "Eesti"),  # Estonian
    # ("eu", "Euskara"),  # Basque
    # ("fa", "فارسی‏"),  # Persian
    # ("fi", "Suomi"),  # Finnish
    # ("fr", "Français"),  # French
    #("fy", "Frysk"),  # Frisian
    #("ga", "Irish"),  # Irish
    #("gl", "Galego"),  # Galician
    # ("he", "עברית‏"),  # Hebrew
    #("hi", "हिन्दी"),  # Hindi
    #("hr", "Hrvatski"),  # Croatian
    #("hu", "Magyar"),  # Hungarian
    #("ia", "Interlingua"),  # Interlingua
    #("id", "Bahasa Indonesia"),  # Indonesian
    #("io", "IDO"),  # Ido
    #("is", "Íslenska"),  # Icelandic
    # ("it", "Italiano"),  # Italian
    # ("ja", "日本語"),  # Japanese
    #("ka", "ქართული"),  # Georgian
    #("kk", "Қазақша"),  # Kazakh
    #("km", "ភាសាខ្មែរ"),  # Khmer
    #("kn", "ಕನ್ನಡ"),  # Kannada
    # ("ko", "한국어"),  # Korean
    #("lb", "Lëtzebuergesch"),  # Luxembourgish
    #("lt", "Lietuvių"),  # Lithuanian
    #("lv", "Latviešu"),  # Latvian
    #("mk", "Македонски"),  # Macedonian
    #("ml", "മലയാളം"),  # Malayalam
    #("mn", "Монгол"),  # Mongolian
    #("mr", "मराठी"),  # Marathi
    #("my", "မြန်မာ"),  # Burmese
    # ("nb", "Norsk (bokmål)"),  # Norwegian Bokmal
    #("ne", "नेपाली"),  # Nepali
    # ("nl", "Nederlands"),  # Dutch
    #("nn", "Norsk (nynorsk)"),  # Norwegian Nynorsk
    #("os", "Ирон æвзаг"),  # Ossetic
    #("pa", "ਪੰਜਾਬੀ"),  # Punjabi
    # ("pl", "Polski"),  # Polish
    #("pt", "Português (Portugal)"),  # Portuguese
    # ("pt-br", "Português (Brasil)"),  # Brazilian Portuguese
    #("ro", "Română"),  # Romanian
    # ("ru", "Русский"),  # Russian
    #("sk", "Slovenčina"),  # Slovak
    #("sl", "Slovenščina"),  # Slovenian
    #("sq", "Shqip"),  # Albanian
    #("sr", "Српски"),  # Serbian
    #("sr-latn", "srpski"),  # Serbian Latin
    # ("sv", "Svenska"),  # Swedish
    #("sw", "Kiswahili"),  # Swahili
    #("ta", "தமிழ்"),  # Tamil
    #("te", "తెలుగు"),  # Telugu
    #("th", "ภาษาไทย"),  # Thai
    # ("tr", "Türkçe"),  # Turkish
    #("tt", "татар теле"),  # Tatar
    #("udm", "удмурт кыл"),  # Udmurt
    # ("uk", "Українська"),  # Ukrainian
    #("ur", "اردو‏"),  # Urdu
    ("vi", "Tiếng Việt"),  # Vietnamese
    # ("zh-hans", "中文(简体)"),  # Simplified Chinese
    # ("zh-hant", "中文(香港)"),  # Traditional Chinese
]

# Languages using BiDi (right-to-left) layout
LANGUAGES_BIDI = ["he", "ar", "fa", "ur"]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
    os.path.join(BASE_DIR, "tina", "locale"),
)

SITES = {
    "api": {"domain": "localhost:8000", "scheme": "http", "name": "api"},
    "front": {"domain": "localhost:9001", "scheme": "http", "name": "front"},
}

SITE_ID = "api"

# Session configuration (only used for admin)
SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_AGE = 1209600 # (2 weeks)

# MAIL OPTIONS
DEFAULT_FROM_EMAIL = "john@doe.com"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DJMAIL_REAL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DJMAIL_SEND_ASYNC = True
DJMAIL_MAX_RETRY_NUMBER = 3
DJMAIL_TEMPLATE_EXTENSION = "jinja"

# Events backend
EVENTS_PUSH_BACKEND = "tina.events.backends.postgresql.EventsPushBackend"
# EVENTS_PUSH_BACKEND = "tina.events.backends.rabbitmq.EventsPushBackend"
# EVENTS_PUSH_BACKEND_OPTIONS = {"url": "//guest:guest@127.0.0.1/"}

# Message System
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

# The absolute url is mandatory because attachments
# urls depends on it. On production should be set
# something like https://media.tina.io/
MEDIA_URL = "http://localhost:8000/media/"
STATIC_URL = "http://localhost:8000/static/"

# Static configuration.
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Don't forget to use absolute paths, not relative paths.
)

# Default storage
DEFAULT_FILE_STORAGE = "tina.base.storage.FileSystemStorage"

FILE_UPLOAD_PERMISSIONS = 0o644

SECRET_KEY = "aw3+t2r(8(0kkrhg8)gx6i96v5^kv%6cfep9wxfom0%7dy0m9e"

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
            "match_extension": ".jinja",
        }
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        }
    },
]


MIDDLEWARE_CLASSES = [
    "tina.base.middleware.cors.CoorsMiddleware",
    "tina.events.middleware.SessionIDMiddleware",

    # Common middlewares
    "django.middleware.common.CommonMiddleware",
    "django.middleware.locale.LocaleMiddleware",

    # Only needed by django admin
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]


ROOT_URLCONF = "tina.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.admin",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.postgres",

    "tina.base",
    "tina.base.api",
    "tina.locale",
    "tina.events",
    "tina.front",
    "tina.users",
    "tina.userstorage",
    "tina.external_apps",
    "tina.projects",
    "tina.projects.references",
    "tina.projects.custom_attributes",
    "tina.projects.history",
    "tina.projects.notifications",
    "tina.projects.attachments",
    "tina.projects.likes",
    "tina.projects.votes",
    "tina.projects.milestones",
    "tina.projects.epics",
    "tina.projects.userstories",
    "tina.projects.funds",
    "tina.projects.tasks",
    "tina.projects.issues",
    "tina.projects.wiki",
    "tina.projects.contact",
    "tina.projects.settings",
    "tina.searches",
    "tina.timeline",
    "tina.mdrender",
    "tina.export_import",
    "tina.feedback",
    "tina.stats",
    "tina.hooks.github",
    "tina.hooks.gitlab",
    "tina.hooks.bitbucket",
    "tina.hooks.gogs",
    "tina.webhooks",
    "tina.importers",

    "djmail",
    "django_jinja",
    "django_jinja.contrib._humanize",
    "sr",
    "easy_thumbnails",
    "raven.contrib.django.raven_compat",
]

WSGI_APPLICATION = "tina.wsgi.application"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "formatters": {
        "complete": {
            "format": "%(levelname)s:%(asctime)s:%(module)s %(message)s"
        },
        "simple": {
            "format": "%(levelname)s:%(asctime)s: %(message)s"
        },
        "null": {
            "format": "%(message)s",
        },
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[%(server_time)s] %(message)s",
        },
    },
    "handlers": {
        "null": {
            "level":"DEBUG",
            "class":"logging.NullHandler",
        },
        "console":{
            "level":"DEBUG",
            "class":"logging.StreamHandler",
            "formatter": "simple",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
    },
    "loggers": {
        "django": {
            "handlers":["null"],
            "propagate": True,
            "level":"INFO",
        },
        "django.request": {
            "handlers": ["mail_admins", "console"],
            "level": "ERROR",
            "propagate": False,
        },
        "tina.export_import": {
            "handlers": ["mail_admins", "console"],
            "level": "ERROR",
            "propagate": False,
        },
        "tina": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        }
    }
}


AUTH_USER_MODEL = "users.User"
FORMAT_MODULE_PATH = "tina.base.formats"

DATE_INPUT_FORMATS = (
    "%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%b %d %Y",
    "%b %d, %Y", "%d %b %Y", "%d %b, %Y", "%B %d %Y",
    "%B %d, %Y", "%d %B %Y", "%d %B, %Y"
)

# Authentication settings (only for django admin)
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend", # default
)

MAX_AGE_AUTH_TOKEN = None
MAX_AGE_CANCEL_ACCOUNT = 30 * 24 * 60 * 60 # 30 days in seconds

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # Mainly used by tina-front
        "tina.auth.backends.Token",

        # Mainly used for api debug.
        "tina.auth.backends.Session",

        # Application tokens auth
        "tina.external_apps.auth_backends.Token",
    ),
    "DEFAULT_THROTTLE_CLASSES": (
        "tina.base.throttling.CommonThrottle",
    ),
    "DEFAULT_THROTTLE_RATES": {
        "anon-write": None,
        "user-write": None,
        "anon-read": None,
        "user-read": None,
        "import-mode": None,
        "import-dump-mode": "1/minute",
        "create-memberships": None,
        "login-fail": None,
        "register-success": None,
        "user-detail": None,
        "user-update": None,
    },
    "DEFAULT_THROTTLE_WHITELIST": [],
    "FILTER_BACKEND": "tina.base.filters.FilterBackend",
    "EXCEPTION_HANDLER": "tina.base.exceptions.exception_handler",
    "PAGINATE_BY": 30,
    "PAGINATE_BY_PARAM": "page_size",
    "MAX_PAGINATE_BY": 1000,
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z"
}

# Extra expose header related to Tina APP (see tina.base.middleware.cors=)
APP_EXTRA_EXPOSE_HEADERS = [
    "tina-info-total-opened-milestones",
    "tina-info-total-closed-milestones",
    "tina-info-project-memberships",
    "tina-info-project-is-private",
    "tina-info-order-updated"
]

DEFAULT_PROJECT_TEMPLATE = "scrum"
# Setting DEFAULT_PROJECT_SLUG_PREFIX to false removes the username from project slug
DEFAULT_PROJECT_SLUG_PREFIX = True
PUBLIC_REGISTER_ENABLED = False
# None or [] values in USER_EMAIL_ALLOWED_DOMAINS means allow any domain
USER_EMAIL_ALLOWED_DOMAINS = None

SEARCHES_MAX_RESULTS = 150

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}


THN_AVATAR_SIZE = 80                # 80x80 pixels
THN_AVATAR_BIG_SIZE = 300           # 300x300 pixels
THN_LOGO_SMALL_SIZE = 80            # 80x80 pixels
THN_LOGO_BIG_SIZE = 300             # 300x300 pixels
THN_TIMELINE_IMAGE_SIZE = 640       # 640x??? pixels
THN_CARD_IMAGE_WIDTH = 300          # 300 pixels
THN_CARD_IMAGE_HEIGHT = 200         # 200 pixels
THN_PREVIEW_IMAGE_WIDTH = 800       # 800 pixels

THN_AVATAR_SMALL = "avatar"
THN_AVATAR_BIG = "big-avatar"
THN_LOGO_SMALL = "logo-small"
THN_LOGO_BIG = "logo-big"
THN_ATTACHMENT_TIMELINE = "timeline-image"
THN_ATTACHMENT_CARD = "card-image"
THN_ATTACHMENT_PREVIEW = "preview-image"

THUMBNAIL_ALIASES = {
    "": {
        THN_AVATAR_SMALL: {"size": (THN_AVATAR_SIZE, THN_AVATAR_SIZE), "crop": True},
        THN_AVATAR_BIG: {"size": (THN_AVATAR_BIG_SIZE, THN_AVATAR_BIG_SIZE), "crop": True},
        THN_LOGO_SMALL: {"size": (THN_LOGO_SMALL_SIZE, THN_LOGO_SMALL_SIZE), "crop": True},
        THN_LOGO_BIG: {"size": (THN_LOGO_BIG_SIZE, THN_LOGO_BIG_SIZE), "crop": True},
        THN_ATTACHMENT_TIMELINE: {"size": (THN_TIMELINE_IMAGE_SIZE, 0), "crop": True},
        THN_ATTACHMENT_CARD: {"size": (THN_CARD_IMAGE_WIDTH, THN_CARD_IMAGE_HEIGHT), "crop": True},
        THN_ATTACHMENT_PREVIEW: {"size": (THN_PREVIEW_IMAGE_WIDTH, 0), "crop": False},
    },
}

TAGS_PREDEFINED_COLORS = ["#fce94f", "#edd400", "#c4a000", "#8ae234",
                          "#73d216", "#4e9a06", "#d3d7cf", "#fcaf3e",
                          "#f57900", "#ce5c00", "#729fcf", "#3465a4",
                          "#204a87", "#888a85", "#ad7fa8", "#75507b",
                          "#5c3566", "#ef2929", "#cc0000", "#a40000",
                          "#2e3436",]

# Feedback module settings
FEEDBACK_ENABLED = True
FEEDBACK_EMAIL = "support@tina.io"

# Stats module settings
STATS_ENABLED = False
STATS_CACHE_TIMEOUT = 60*60  # In second

# 0 notifications will work in a synchronous way
# >0 an external process will check the pending notifications and will send them
# collapsed during that interval
CHANGE_NOTIFICATIONS_MIN_INTERVAL = 0 #seconds


# List of functions called for filling correctly the ProjectModulesConfig associated to a project
# This functions should receive a Project parameter and return a dict with the desired configuration
PROJECT_MODULES_CONFIGURATORS = {
    "github": "tina.hooks.github.services.get_or_generate_config",
    "gitlab": "tina.hooks.gitlab.services.get_or_generate_config",
    "bitbucket": "tina.hooks.bitbucket.services.get_or_generate_config",
    "gogs": "tina.hooks.gogs.services.get_or_generate_config",
}

BITBUCKET_VALID_ORIGIN_IPS = ["131.103.20.165", "131.103.20.166", "104.192.143.192/28", "104.192.143.208/28"]

GITLAB_VALID_ORIGIN_IPS = []

EXPORTS_TTL = 60 * 60 * 24  # 24 hours

CELERY_ENABLED = False
WEBHOOKS_ENABLED = False
WEBHOOKS_BLOCK_PRIVATE_ADDRESS = False


# If is True /front/sitemap.xml show a valid sitemap of tina-front client
FRONT_SITEMAP_ENABLED = False
FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second

EXTRA_BLOCKING_CODES = []

MAX_PRIVATE_PROJECTS_PER_USER = None # None == no limit
MAX_PUBLIC_PROJECTS_PER_USER = None # None == no limit
MAX_MEMBERSHIPS_PRIVATE_PROJECTS = None # None == no limit
MAX_MEMBERSHIPS_PUBLIC_PROJECTS = None # None == no limit

MAX_PENDING_MEMBERSHIPS = 30 # Max number of unconfirmed memberships in a project

from .sr import *

IMPORTERS = {
    "github": {
        "active": False,
        "client_id": "",
        "client_secret": "",
    },
    "trello": {
        "active": False,
        "api_key": "",
        "secret_key": "",
    },
    "jira": {
        "active": False,
        "consumer_key": "",
        "cert": "",
        "pub_cert": "",
    },
    "asana": {
        "active": False,
        "callback_url": "",
        "app_id": "",
        "app_secret": "",
    }
}

# NOTE: DON'T INSERT MORE SETTINGS AFTER THIS LINE
TEST_RUNNER="django.test.runner.DiscoverRunner"

if "test" in sys.argv:
    print ("\033[1;91mNo django tests.\033[0m")
    print ("Try: \033[1;33mpy.test\033[0m")
    sys.exit(0)
