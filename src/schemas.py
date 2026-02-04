from pydantic import BaseModel

class Cliente(BaseModel):
    months_active: int
    monthly_price: int
    users_count: int
    tickets_per_month: int
    logins_per_month: int
    mobile_usage_ratio: float
    api_usage: int
    support_tickets_last_3m: int