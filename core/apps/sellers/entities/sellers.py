from dataclasses import dataclass


@dataclass
class Seller:
    id: int  # noqa
    company_name: str
    description: str
    website_url: str
    contact_phone: str
