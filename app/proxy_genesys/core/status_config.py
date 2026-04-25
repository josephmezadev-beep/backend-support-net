STATUS_CONFIG = [
    {
        "status": "Meal",
        "status_name": "Comida",
        "source": "presence",
        "min_threshold": 3600,
        "max_threshold": 4200,
    },
    {
        "status": "Busy",
        "status_name": "Ocupado",
        "source": "presence",
        "min_threshold": 900,
        "max_threshold": 1500,
    },
    {
        "status": "Offline",
        "status_name": "Desconectado",
        "source": "presence",
        "min_threshold": 60,
        "max_threshold": 300,
        "visibility_only": True
    },
    {
        "status": "Training",
        "status_name": "Capacitación",
        "source": "presence",
        "min_threshold": 900,
        "max_threshold": 1500,
    },
    {
        "status": "Available",
        "status_name": "Disponible",
        "source": "presence",
        "min_threshold": 60,
        "max_threshold": 180,
    },
    {
        "status": "IDLE",
        "status_name": "Ocioso",
        "source": "routing",
        "min_threshold": 120,
        "max_threshold": 240,
    },
    {
        "status": "NOT_RESPONDING",
        "status_name": "No Responden",
        "source": "routing",
        "min_threshold": 60,
        "max_threshold": 300,
    }
]