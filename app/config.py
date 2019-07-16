# Python
import os
# lib
# app

RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'guest')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD', 'guest')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'rabbitmq')
RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT', 5672))
RABBITMQ_VHOST = os.getenv('RABBITMQ_VHOST', '/')
RABBITMQ_URI = os.getenv(
    'RABBITMQ_URI', 'amqp://{}:{}@{}:{}{}'.format(
        RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_VHOST
    )
)

DB_HOST = os.getenv('DB_HOST', 'postgres')
DB_USER = os.getenv('DB_USER', 'guest')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'guest')
DB_DB = os.getenv('DB_DB', 'celery_playground')
DB_PORT = os.getenv('DB_PORT', 5432)
DB_CONNECTION_LIMIT = int(os.getenv('DB_CONNECTION_LIMIT', 30))
DB_SCHEME = os.getenv('DB_SCHEME', 'postgresql')

DB_URI = os.getenv(
    'DB_URI',
    '{}://{}:{}@{}:{}/{}'.format(DB_SCHEME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DB)
)

BROKER_CONNECTION_RETRY = True
BROKER_CONNECTION_TIMEOUT = 30

# db+dialect://
CELERY_RESULT_BACKEND = 'db+{}'.format(DB_URI)
BROKER_URL = RABBITMQ_URI
