from os import environ

SESSION_CONFIGS = [
    dict(name='test_app', app_sequence=['test_app'], num_demo_participants=4),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
AUTH_LEVEL = 'DEMO'
DEMO_PAGE_INTRO_HTML = """ """

# Ejecutar otree prodserver 80
contraseña = 'test'
environ['DATABASE_URL'] = "postgres://postgres:{}@localhost/django_db".format(contraseña)
SECRET_KEY = '5988987251664'

