from pydantic.fields import Field
from pydantic import BaseModel


class ProductItem(BaseModel):
    product_name: str = Field(None, alias='productName')
    short_name: str = Field(None, alias='shortName')
    status: str = Field(None)
    migration_date: int = Field(None, alias='migrationDate')
    validation_date: int = Field(None, alias='validationDate')
    reset_date: int = Field(None, alias='resetDate')
    currency: str = Field(None)

    class Config:
        allow_population_by_field_name = True
