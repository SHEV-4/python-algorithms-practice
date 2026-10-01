from datetime import datetime
def get_days_from_today(date:str):
    try:
        now_date = datetime.now()
        current_date = datetime.strptime(date,"%Y-%m-%d")
        diff = now_date - current_date
        return diff.days
    except ValueError:
        return f'Дата має неправильний формат. Правильний формат "РРРР-ММ-ДД"'
    
