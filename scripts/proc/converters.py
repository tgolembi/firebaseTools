from datetime import datetime

def convert_datetime(obj):
    if isinstance(obj, datetime):  # Se for datetime padrão do Python
        return obj.isoformat()
    return str(obj)

def convert_date_time_to_string(dt: datetime | None = None):
    if dt is None:
        dt = datetime.now()
    elif not isinstance(dt, datetime):
        raise TypeError("O parâmetro deve ser um objeto datetime ou None.")
    return dt.strftime("%Y%m%d_%H%M%S")

