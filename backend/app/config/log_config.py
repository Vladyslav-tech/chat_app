LOG_LEVEL: str = "INFO"
FORMAT: str = "%(levelname)s:\t  %(asctime)s - %(name)s - %(message)s"

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "basic": {
            "format": FORMAT,
        }
    },
    "handlers": {
        "console": {
            "formatter": "basic",
            "class": "logging.StreamHandler",
            "level": LOG_LEVEL,
        },
    },
    "loggers": {
        "app": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": True,
        }
    },
}
