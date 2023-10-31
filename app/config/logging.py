import logging

import config
from config import LOG_DIR, LOG_LEVEL, LOG_PROPAGATE


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {'format': '[%(asctime)s.%(msecs)03d] %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'},
        'console': {'format': '[%(asctime)s.%(msecs)03d] %(name)s:%(levelname)s %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'},
    },
    'filters': {
        'request_id_filter': {
            '()': 'internal.core.logs.filters.RequestIdFilter',
        },
        'access_filter': {
            '()': 'internal.core.logs.filters.AccessFilter',
        },
    },
    'handlers': {
        'console': {
            'level': LOG_LEVEL,
            'formatter': 'console',
            'class': 'logging.StreamHandler',
        },
        'access_file_handler': {
            'formatter': 'standard',
            'level': logging.INFO,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{LOG_DIR}/access.log',
            'when': 'midnight',
            'backupCount': 0,
        },
        'error_file_handler': {
            'formatter': 'standard',
            'level': logging.ERROR,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{LOG_DIR}/error.log',
            'when': 'midnight',
            'backupCount': 0,
        },
        'smsinfo_file_handler': {
            'formatter': 'standard',
            'level': LOG_LEVEL,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{LOG_DIR}/smsinfo.log',
            'when': 'midnight',
            'backupCount': 0,
        },
        'requests_file_handler': {
            'formatter': 'standard',
            'level': logging.INFO,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{LOG_DIR}/requests.log',
            'when': 'midnight',
            'backupCount': 0,
        },
    },
    'loggers': {
        'root': {'level': LOG_LEVEL, 'handlers': ['console'], 'propagate': False},
        'smsinfo': {
            'handlers': ['smsinfo_file_handler'],
            'filters': ['request_id_filter'],
            'propagate': LOG_PROPAGATE,
        },
        'requests': {
            'handlers': ['requests_file_handler'],
            'filters': ['request_id_filter'],
            'propagate': LOG_PROPAGATE,
        },
        'error': {
            'handlers': ['error_file_handler'],
            'filters': ['request_id_filter'],
            'level': logging.ERROR,
            'propagate': LOG_PROPAGATE,
        },
        'sanic.access': {'handlers': ['access_file_handler'], 'filters': ['access_filter', 'request_id_filter'], 'level': logging.INFO, 'propagate': True},
        'sanic.root': {'level': config.LOG_LEVEL, 'propagate': True},
    },
}
