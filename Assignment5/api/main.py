from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import orders, sandwiches, resources, recipes, order_details
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)



@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db=db, sandwich=sandwich)

@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwiches"])
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)

@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich_obj = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich_obj is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwich_obj

@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def update_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    if sandwiches.read_one(db, sandwich_id=sandwich_id) is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwiches.update(db=db, sandwich_id=sandwich_id, sandwich=sandwich)

@app.delete("/sandwiches/{sandwich_id}", tags=["Sandwiches"])
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    if sandwiches.read_one(db, sandwich_id=sandwich_id) is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwiches.delete(db=db, sandwich_id=sandwich_id)


@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, resource=resource)

@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)

@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource_obj = resources.read_one(db, resource_id=resource_id)
    if resource_obj is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource_obj

@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def update_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    if resources.read_one(db, resource_id=resource_id) is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources.update(db=db, resource_id=resource_id, resource=resource)

@app.delete("/resources/{resource_id}", tags=["Resources"])
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    if resources.read_one(db, resource_id=resource_id) is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources.delete(db=db, resource_id=resource_id)


@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, recipe=recipe)

@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)

@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe_obj = recipes.read_one(db, recipe_id=recipe_id)
    if recipe_obj is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe_obj

@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def update_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    if recipes.read_one(db, recipe_id=recipe_id) is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipes.update(db=db, recipe_id=recipe_id, recipe=recipe)

@app.delete("/recipes/{recipe_id}", tags=["Recipes"])
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    if recipes.read_one(db, recipe_id=recipe_id) is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipes.delete(db=db, recipe_id=recipe_id)


@app.post("/order_details/", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def create_order_detail(order_detail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create(db=db, order_detail=order_detail)

@app.get("/order_details/", response_model=list[schemas.OrderDetail], tags=["OrderDetails"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.read_all(db)

@app.get("/order_details/{order_detail_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def read_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail_obj = order_details.read_one(db, order_detail_id=order_detail_id)
    if order_detail_obj is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return order_detail_obj

@app.put("/order_details/{order_detail_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def update_order_detail(order_detail_id: int, order_detail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    if order_details.read_one(db, order_detail_id=order_detail_id) is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return order_details.update(db=db, order_detail_id=order_detail_id, order_detail=order_detail)

@app.delete("/order_details/{order_detail_id}", tags=["OrderDetails"])
def delete_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    if order_details.read_one(db, order_detail_id=order_detail_id) is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return order_details.delete(db=db, order_detail_id=order_detail_id)