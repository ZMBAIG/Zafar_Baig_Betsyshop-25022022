# Models go here    
from peewee import (Model,
                    TextField,
                    CharField,
                    DecimalField,
                    IntegerField,
                    ForeignKeyField,
                    FloatField,)

from playhouse.sqlite_ext import(JSONField,)
import peewee

sqlite_db = peewee.SqliteDatabase("BetsyshopDatabase.db")
  
class BaseModel(Model):
    """A base model that will use our Sqlite database"""    
    class Meta:
        database            =      sqlite_db

class User(BaseModel):
    name                    =      TextField()
    user_address            =      JSONField()
    user_invoice            =      JSONField()

class Product(BaseModel):
    name                    =      CharField()
    ItemDescription         =      TextField()
    PricePerItem            =      DecimalField(auto_round = True)
    StockQuantity           =      IntegerField()

class Tag(BaseModel):
    tag                     =      CharField(unique = True) 

class Product_Tag(BaseModel):
    product                 =      ForeignKeyField(Product)
    tag                     =      ForeignKeyField(Tag)

class Product_User(BaseModel):
    user                    =      ForeignKeyField(User)
    product                 =      ForeignKeyField(Product)
    
class Transaction(BaseModel):
    user                    =      ForeignKeyField(User)
    product                 =      ForeignKeyField(Product)
    TotalProductPurchased   =      IntegerField() 
    total                   =      FloatField()       