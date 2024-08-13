from dataclasses import dataclass
from datetime import datetime


@dataclass
class SellerApplication:
    id: int  # noqa
    presentation_text: str
    email: str
    approved: bool
    created_at: datetime
    updated_at: datetime
