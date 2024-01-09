from fastapi import FastAPI

app=FastAPI()

# @app.get('/hello/{name}')#This is a decorator after this a function or a class is expected .Hello here is the name of an endpoint
# async def hello(name):
#     return f"Welcome to FastAPI tutorial {name}"


#Right now we are not having a database but we will try to observe its behaviour via a dictionary
food={
    "Indian":['Samosa','Biryani'],
    "Chinese":['Noodles','Soup'],
    "Italian":['Pizza','Pasta']
}

valid_cuisine=food.keys()

@app.get('/get_items/{cuisine}')
def get_items(cuisine:str):
    if cuisine not in valid_cuisine:
        return f'valid cuisine are {valid_cuisine}'#This is how we do the validation in code but fastapi has a powerful feature wherein
        #it itself does all the things
    return food.get(cuisine)

coupon_code={
    1:'10%',
    2:'20%',
    3:'30%'
}

@app.get('/get_coupon/{code}')
def get_coupon(code:int):
    return f'Discount is : {coupon_code.get(code)}'