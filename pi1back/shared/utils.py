from datetime import datetime

def get_current_quarter():
    now = datetime.now()
    return (now.month - 1) // 3 + 1
