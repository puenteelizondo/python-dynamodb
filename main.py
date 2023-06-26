from uuid import uuid4

import boto3
from boto3.dynamodb.conditions import Key

#para hacer la conexiony retornar la tabla
def get_db_table():
    #conexion
    dynamodb_resource = boto3.resource("dynamodb")
    #acceder a la tabla que queremos
    return dynamodb_resource.Table("JESUS_EDUARDO")


def register_account(user_email: str, user_name: str) -> dict:
    ddb_table = get_db_table()

    response = ddb_table.put_item(
        Item={
            "PK": user_email,
            "SK": "PROFILE#",
            "name": user_name,
        }
    )

    return response


def invite_account(user_email: str, invited_user_email: str, invited_user_name: str):
    ddb_table = get_db_table()

    response = ddb_table.put_item(
        Item={
            "PK": user_email,
            "SK": f"USER#{invited_user_email}",
            "name": invited_user_name,
        }
    )

    return response

#creamos inventario
def register_inventory(user_email: str, inventory_name: str, inventory_price: int):
    ddb_table = get_db_table()

    response = ddb_table.put_item(
        Item={
            #al pk se le manda el usuario para saber a cual se van a conectar
            "PK": user_email,
            #generar id dentro del codigo para que no se repita que es uuid4
            #lo hacemos string para poder manipularlo
            "SK": f"INVENTORY#{str(uuid4())}",
            "name": inventory_name,
            "price": inventory_price,
        }
    )

    return response


def get_inventory(user_email: str):
    ddb_table = get_db_table()

    response = ddb_table.query(
        KeyConditionExpression=Key("PK").eq(user_email)
        & Key("SK").begins_with("INVENTORY#")
    )

    return response["Items"]


def get_invited_users(user_email: str):
    ddb_table = get_db_table()

    response = ddb_table.query(
        KeyConditionExpression=Key("PK").eq(user_email) & Key("SK").begins_with("USER#")
    )

    return response["Items"]


def delete_inventory(user_email: str, inventory_id: str):
    ddb_table = get_db_table()

    response = ddb_table.delete_item(
        Key={
            "PK": user_email,
            "SK": f"INVENTORY#{inventory_id}",
        }
    )

    return response


def update_inventory(
    user_email: str,
    inventory_id: str,
    new_inventory_name: str,
    new_inventory_price: int,
):
    ddb_table = get_db_table()

    response = ddb_table.put_item(
        Item={
            "PK": user_email,
            "SK": f"INVENTORY#{inventory_id}",
            "name": new_inventory_name,
            "price": new_inventory_price,
        }
    )

    return response



# for item in get_invited_users(user_email="emiliomoreno@dominio.com"):
#     print(item)

# for item in get_inventory(user_email="luisduran@dominio.com"):
#     print(item)

 #print(register_account(
  #   user_email="luisduran@dominio.com",
   #  user_name="Luis Duran"
 #))

#print(register_inventory(
#    user_email="luisduran@dominio.com",
#     inventory_name="Cuadernos",
#    inventory_price=80,
# ))

# print(invite_account(
#     user_email="emiliomoreno@dominio.com",
#     invited_user_email="emiliomoreno3@dominio.com",
#     invited_user_name="Emilio Moreno 3",
# ))

# print(
#     delete_inventory(
#         user_email="luisduran@dominio.com",
#         inventory_id="3ecc4594-3cd2-44e2-819c-00c1d2abcd3b",
#     )
# )

# print(update_inventory(
#     user_email="emiliomoreno@dominio.com",
#     inventory_id="9ed5cbcb-c67c-4655-ba0d-cf82342303e5",
#     new_inventory_name="Servilletas",
#     new_inventory_price=60,
# ))

print(register_inventory(

    
    
    user_email="luisduran@dominio.com",
    inventory_name="tenedores",
    inventory_price=30,
    
))