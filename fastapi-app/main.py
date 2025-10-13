from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Image(BaseModel):
    url: str = Field(..., example = "http://example.com/image.jpg")
    name: str = Field(..., example = "Product Image")

# class Item(BaseModel):
#     name: str = Field(..., example = "게이밍 마우스")
#     description: str | None = Field(default=None, example="버티컬 마우스.")
#     price: float = Field(..., example = 59.99)
#     tax: float = Field(default = None, ge=0, example=0.1)
#
#     tags: list[str] = Field(default=[], example = ["전자제품", "게이밍 마우스", "PC 주변기기"])
#
#     image: Image | None = Field(default=None)

class Item(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    description: str | None = Field(default=None, max_length=500)
    price: float = Field(..., gt=0)
    tax: float | None = Field(default=None, ge=0)
    tags: list[str] = Field(default = [])
    image: Image | None = Field(default=None)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "버티컬 마우스",
                "description": "손목이 편안한 마우스",
                "price": 59.99,
                "tax": 0.1,
                "tags": ["버티컬", "PC 부품", "마우스"],
                "image": {
                    "url": "http://example.com/image.jpg",
                    "name": "Product Image",
                }
            }
        }

@app.post("/items/")
def create_item(item: Item):
    return item

@app.post("/items/bulk/")
def create_bulk_item(items: list[Item]):
    return {"message": f"{len(items)} items created.", "data": items}

