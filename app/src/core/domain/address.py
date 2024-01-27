from dataclasses import dataclass
from src.core.domain.enum.country import Country

@dataclass
class Address:
    zipCode: str
    country: Country
    state: str
    city: str    
    address: str
    