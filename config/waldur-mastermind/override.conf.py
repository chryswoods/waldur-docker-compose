import os

WALDUR_CORE['AUTHENTICATION_METHODS'] = ["LOCAL_SIGNIN", "SOCIAL_SIGNUP"]

WALDUR_CORE['CREATE_DEFAULT_PROJECT_ON_ORGANIZATION_CREATION'] = True

WALDUR_CORE['HOMEPORT_SENTRY_ENVIRONMENT'] = env.get('SENTRY_ENVIRONMENT', 'waldur-production')

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_USER = os.environ.get('RABBITMQ_USERNAME')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD')
RABBITMQ_PORT = "5672"
POSTGRESQL_HOST = os.environ.get('POSTGRESQL_HOST')
POSTGRESQL_PORT = "5432"
POSTGRESQL_PASSWORD = os.environ.get('POSTGRESQL_PASSWORD')
POSTGRESQL_NAME = 'celery_results'

CELERY_BROKER_URL = f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}'
CELERY_RESULT_BACKEND = f'db+postgresql://waldur:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_NAME}'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'waldur_cache',
    }
}

RABBITMQ_MQTT = {
    "HOST": "waldur-queue",
    "PORT": 1883,
    "USER": RABBITMQ_USER,
    "PASSWORD": RABBITMQ_PASSWORD,
    "MANAGEMENT_PORT": 15672,
}
