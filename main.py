__winc_id__         = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__      = "Betsy Webshop"

from models import(
                    sqlite_db,
                    User,
                    Product,
                    Tag,
                    Product_Tag,
                    Product_User,
                    Transaction
                    )
import models
import peewee
from rich.console import Console
from rich.style import Style
console = Console()
from rich import print
from rich.panel import Panel

def ToConnectDatabase():
    models.sqlite_db.connect()
    print("\n====================================================================")
    print(Panel.fit('[blink bold white on green]DATABASE HAS BEEN CONNECTED[/]'))
    
ToConnectDatabase()

def create_tables():
    print('\nCreating tables....')
    with models.sqlite_db:
        models.sqlite_db.create_tables(
                                 [models.User, 
                                 models.Product,
                                 models.Tag,
                                 models.Product_Tag,
                                 models.Product_User,
                                 models.Transaction]
                                 )
    print('Tables have been created with desire information.')
create_tables()

def CreateUsersInfoWithTestData():
    """Now we have stored 10 users with respect to their name, user_address data, and billing information in the database. Let’s perform some data queries to obtain required results."""
    user_01 = models.User.create(
        name                    =      'Zafar', 
        user_address            = {
            'street'            :      'Example Street',
            'number'            :       23,
            'postal_code'       :       '3087XX',
            'city'              :       'Rotterdam'
                                },
        user_invoice            = {
            'card_holder'       :       'Zafar',
            'card_number'       :       '1234 5678 1234 5678',
            'exp_date'          :       '23-09-2039',
                                }
                                )
    
    user_02 = models.User.create(
        name                    =      'Peter', 
        user_address            = {
            'street'            :      'Example Street',
            'number'            :       23,
            'postal_code'       :       '3087XX',
            'city'              :       'Amsterdam'
                                },
        user_invoice            = {
            'card_holder'       :       'Peter',
            'card_number'       :       '5678 1234 9274 5608',
            'exp_date'          :       '23-09-2099',
                                }
                                )
    user_03 = models.User.create(
        name                    =      'Cathy', 
        user_address            = {
            'street'            :      'Example Street',
            'number'            :       87,
            'postal_code'       :       '3087XX',
            'city'              :       'Breda'
                                },
        user_invoice            = {
            'card_holder'       :       'Cathy',
            'card_number'       :       '8730 5678 3782 0698',
            'exp_date'          :       '23-09-2050',
                                }
                                )
    user_04 = models.User.create(
        name                    =      'John', 
        user_address            = {
            'street'            :      'Example Street',
            'number'            :       203,
            'postal_code'       :       '3087XX',
            'city'              :       'Utrecht'
                                },
        user_invoice            = {
            'card_holder'       :       'John',
            'card_number'       :       '9034 6743 0234 2',
            'exp_date'          :       '23-09-2070',
                                }
                                )

    user_05 = models.User.create(
        name                    =      'Trump', 
        user_address            = {
            'street'            :      'Example Street',
            'number'            :       67,
            'postal_code'       :       '3087XX',
            'city'              :       'Rotterdam'
                                },
        user_invoice            = {
            'card_holder'       :       'Trump',
            'card_number'       :       '0034 9878 0934 4023',
            'exp_date'          :       '23-09-2065',
                                }
                                )
    
    user_06 = models.User.create(
        name                    =      'Biden', 
        user_address            = {
            'street'            :      'Example Street',
            'number'            :       34,
            'postal_code'       :       '6743XX',
            'city'              :       'Rotterdam'
                                },
        user_invoice            = {
            'card_holder'       :       'Biden',
            'card_number'       :       '4534 9878 6732 4023',
            'exp_date'          :       '23-09-2069',
                                }
                                )
    
    user_07 = models.User.create(
        name                    =      'Nancy', 
        user_address            = {
            'street'            :      'Example Street',
            'number'            :       26,
            'postal_code'       :       '9065XX',
            'city'              :       'Amsterdam'
                                },
        user_invoice            = {
            'card_holder'       :       'Nancy',
            'card_number'       :       '0452 9878 6732 4023',
            'exp_date'          :       '23-09-2069',
                                }
                                )

    user_08 = models.User.create(
        name                    =      'Donald', 
        user_address            = {
            'street'            :      'Example Street',
            'number'            :       89,
            'postal_code'       :       '5412XX',
            'city'              :       'Breda'
                                },
        user_invoice            = {
            'card_holder'       :       'Donald',
            'card_number'       :       '8753 9878 6732 4023',
            'exp_date'          :       '23-09-2089',
                                }
                                )
    user_09 = models.User.create(
        name                    =      'Clinton', 
        user_address            = {
            'street'            :      'Example Street',
            'number'            :       67,
            'postal_code'       :       '6743XX',
            'city'              :       'Rotterdam'
                                },
        user_invoice            = {
            'card_holder'       :       'Clinton',
            'card_number'       :       '0978 9878 6732 4023',
            'exp_date'          :       '23-09-2040',
                                }
                                )
    

    user_10 = models.User.create(
        name                    =      'Bush', 
        user_address            = {
            'street'            :      'Example Street',
            'number'            :       56,
            'postal_code'       :       '9843XX',
            'city'              :       'Utrecht'
                                },
        user_invoice            = {
            'card_holder'       :       'Bush',
            'card_number'       :       '3214 9878 6732 4023',
            'exp_date'          :       '23-09-2078',
                                }
                                )
    
    coat                =   models.Product.create(
    name                =   'Coat',
    ItemDescription     =   'B-01-Wool Size M L XL',
    PricePerItem        =    179.50,
    StockQuantity       =    25
                        )
    
    pantalon            =   models.Product.create( 
    name                =   'Pantalon',
    ItemDescription     =   'B-02-corduroy in dark brown',
    PricePerItem        =   120.50,
    StockQuantity       =   50
                        )
    
    shoes               =   models.Product.create(
    name                =   'Shoes',
    ItemDescription     =   'B-03-casual Black',
    PricePerItem        =   39.95,
    StockQuantity       =   75
                        )

    jacket              =   models.Product.create(
    name                =   'Jacket',
    ItemDescription     =   'B-04-Dark Green Size S M L',
    PricePerItem        =   240.95,
    StockQuantity       =   100
                        )
    
    suit                =   models.Product.create(
    name                =   'Suit',
    ItemDescription     =   'B-05-Three piece suit in Navy Blue',
    PricePerItem        =   350.90,
    StockQuantity       =   125
                        )
    wallet              =   models.Product.create(
    name                =   'Wallet',
    ItemDescription     =   'B-06-Genuine leather',
    PricePerItem        =   50.90,
    StockQuantity       =   150
                        )
    
    shirt               =   models.Product.create(
    name                =   'Shirt',
    ItemDescription     =   'B-07-Cotton',
    PricePerItem        =   30.90,
    StockQuantity       =   175
                        )
    belt                =   models.Product.create(
    name                =   'Belt',
    ItemDescription     =   'B-08-Genuine leather in dark brown',
    PricePerItem        =   55.90,
    StockQuantity       =   200
                        )
    hat                 =   models.Product.create(
    name                =   'Hat',
    ItemDescription     =   'B-09-Black',
    PricePerItem        =   35.90,
    StockQuantity       =   225
                        )
    blazer              =   models.Product.create(
    name                =   'Blazer',
    ItemDescription     =   'B-10-Genuine leather & woolen made.',
    PricePerItem        =   350.90,
    StockQuantity       =   300
                        )
    
    dress               =   models.Tag.create(tag   = '\"Dress\"')
    others              =   models.Tag.create(tag   = '\"Others\"')
    
    product_user_01 = models.Product_User.create(user = user_01, product = coat)
    product_user_02 = models.Product_User.create(user = user_02, product = pantalon)
    product_user_03 = models.Product_User.create(user = user_05, product = shoes)
    product_user_04 = models.Product_User.create(user = user_03, product = jacket)
    product_user_05 = models.Product_User.create(user = user_03, product = suit)
    product_user_06 = models.Product_User.create(user = user_04, product = wallet)
    product_user_07 = models.Product_User.create(user = user_04, product = shirt)
    product_user_08 = models.Product_User.create(user = user_04, product = belt)
    product_user_09 = models.Product_User.create(user = user_03, product = hat)
    product_user_10 = models.Product_User.create(user = user_04, product = blazer)
    
    product_tag_01 = models.Product_Tag.create(product  = coat,      tag   = dress)
    product_tag_02 = models.Product_Tag.create(product  = pantalon,  tag   = dress)
    product_tag_03 = models.Product_Tag.create(product  = shoes,     tag   = others)
    product_tag_04 = models.Product_Tag.create(product  = jacket,    tag   = dress)
    product_tag_05 = models.Product_Tag.create(product  = suit,      tag   = dress)
    product_tag_06 = models.Product_Tag.create(product  = wallet,    tag   = others)
    product_tag_07 = models.Product_Tag.create(product  = shirt,     tag   = dress)
    product_tag_08 = models.Product_Tag.create(product  = belt,      tag   = others)
    product_tag_09 = models.Product_Tag.create(product  = hat,       tag   = others)
    product_tag_10 = models.Product_Tag.create(product  = blazer,    tag   = dress)
    

    print('Please, Print Test database with acquired products.')
CreateUsersInfoWithTestData()
       
# Search for products based on a term. e.g. 'Shoes'.
def search(term = str):
    print('\nLooking for your requested items.')
    query = (models.Product.select().where(models.Product.name ** f"%{term}%"))

    if query:
        for x_product in query:
            console.print(f"[bold green]This is your searched product: [underline]{x_product.name}[/]")
    else:
        console.print('[blink bold red]Sorry! No products matched with your search term[/]') 
    print("\n====================================================================")
search('Suit')
# search('sweater')

               
# View the products of a given user.
def list_user_products(user_id):
    query_to_get_user = models.User.get(models.User.id == user_id)
    
    console.print(f"\nDetail of the products that [blue]{query_to_get_user.name}[/] found.")
    query = (models.Product.select().join(models.Product_User).join(models.User).where(models.User.id == user_id))
    
    if query:
        console.print(f"These are the products of [blue]{query_to_get_user.name}:[/]\n ")
        for x_product in query:
            print(x_product.name)
    else:
        print(f"Sorry! No product is found. Either this user {query_to_get_user.name} has not selected any product or he has not given a valid product.")
list_user_products(3)# user_03 is Cathy        

# View all products for a given tag.
def list_products_per_tag(tag_id):
    query_to_get_tag = models.Tag.get(models.Tag.id == tag_id)
    query = (models.Product.select().join(models.Product_Tag).join(models.Tag).where(models.Tag.id == tag_id))
    print("\n====================================================================")
    
    if query:
        console.print(f"\n[bold white on blue]PRODUCTS CLASSIFIED WITH TAG {query_to_get_tag.tag}[/]\n")
        for product in query:
            print(product.name)
    else:
        console.print('[bold yellow]No product found. Either there is not any relevant product  or this tag doesn\'t exist.[/]')
    print("====================================================================")
list_products_per_tag(1)# i.e. 1 = Dress, 2 = Others

# Add a product to a catalog.
def add_product_to_catalog(user_id, product):
    console.print('\n[black on yellow]ADDITION OF PRODUCTS TO USER[/]')
    query_to_get_user    = models.User.get(models.User.id == user_id)
    query_to_get_product = models.Product.get(models.Product.name == product)
    models.Product_User.get_or_create(user=query_to_get_user, product=query_to_get_product)
    
    print(f"\nAdded a {query_to_get_product.name} to {query_to_get_user.name}")
add_product_to_catalog(3, 'Suit')

# Update the stock quantity of a product.    
def update_stock(product_id, new_quantity):
    query_to_get_product = models.Product.get(models.Product.id == product_id)
    query = models.Product.update(StockQuantity = new_quantity).where(models.Product.id == product_id).execute()
    
    print(f"\nUpdating Database with new addition of {query_to_get_product.name}.")
    
    console.print(f"After adding [bold green]\"{query_to_get_product.name}\"[/] in the database, status of stock quantity:  {new_quantity}")
    
    print("\n====================================================================")
# update_stock(2, 5)
update_stock(5, 10)

# Handle a purchase between a buyer and a seller for a given product
def purchase_product(product_id, buyer_id, quantity):
    console.print('\n[bold white on green]PURCHASING OF PRODUCTS[/]')
    buyer           =   models.User.get(models.User.id == buyer_id)
    product         =   models.Product.get(models.Product.id == product_id)
    PricePerProduct =   product.PricePerItem
    TotalPrice      =   int(quantity) * PricePerProduct

    models.Transaction.create(
        user                    =   buyer_id,
        product                 =   product_id,
        TotalProductPurchased   =   quantity,
        total                   =   TotalPrice
                            )

    ProductStockStatus = product.StockQuantity - quantity

    update_stock(product_id, ProductStockStatus)
purchase_product(4, 2, 5)

# Removing a product from a user with product_id.    
def remove_product(product_id):
    query_to_get_product = models.Product.get(models.Product.id == product_id)
    query = models.Product.delete().where(models.Product.id == product_id).execute()
    console.print('\n[red on white]REMOVAL OF PRODUCTS[/]')
    console.print(f"\n[red]The product named [red on white]{query_to_get_product.name} [/]has been removed from the database.[/]\n")
    print("====================================================================")
remove_product(3)

    
   

