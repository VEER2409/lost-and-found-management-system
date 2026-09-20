from database import get_connection

#generate case id logic -----------------------------------------------------------
def generate_case_id():

    connection=get_connection()
    cursor=connection.cursor()

    cursor.execute("select case_id from found_items order by case_id desc limit 1")

    result=cursor.fetchone()

    cursor.close()
    connection.close()

    if result is None:
        return "LF0001"

    last_case_id=result[0]
    last_number=int(last_case_id[2:])
    new_number=last_number+1

    return f"LF{new_number:04d}"

# <1> input case data into table ------------------------------------------------------------------
def create_found_item(item_data):
    case_id=generate_case_id()

    connection=get_connection()
    cursor=connection.cursor()

    query=""" insert into found_items (case_id,category,item_name,brand,model,description,found_location,found_date,finder_name,finder_employee_id,storage_location)
              values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    values=(
        case_id,
        item_data["category"],
        item_data["item_name"],
        item_data["brand"],
        item_data["model"],
        item_data["description"],
        item_data["found_location"],
        item_data["found_date"],
        item_data["finder_name"],
        item_data["finder_employee_id"],
        item_data["storage_location"],
    )

    cursor.execute(query,values)

    connection.commit()
    cursor.close()

    return case_id

    print(f"Item created successfully. Case ID: {case_id}")

# <3> search operation  ------------------------------------------------------------------------------

def search_by_case_id(case_id):
    connection=get_connection()
    cursor=connection.cursor(dictionary=True)

    query="select * from found_items where case_id=%s"

    cursor.execute(query,(case_id,))

    case=cursor.fetchone()

    cursor.close()
    connection.close()

    return case


# <4> update model -------------------------

#update crud operation---------------------------------------
def update_found_item(case_id,field,new_val):
    connection=get_connection()
    cursor=connection.cursor()

    query=f"update found_items set {field}=%s where case_id=%s "
    value=(new_val,case_id)

    cursor.execute(query,value)

    connection.commit()
    cursor.close()
    connection.close()

    print(f"{field.upper()} has been updated to {new_val.upper()}")

# <5> update model -------------------------


def delete_found_item(case_id):

    connection=get_connection()
    cursor=connection.cursor()

    query="delete from found_items where case_id=%s"

    cursor.execute(query,(case_id,))

    connection.commit()
    cursor.close()
    connection.close