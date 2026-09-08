import pandas as pd
from database import get_connection

def export_to_excel():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query="select * from found_items order by case_id"

    cursor.execute(query)

    cases=cursor.fetchall()

    cursor.close()
    connection.close()

    df=pd.DataFrame(cases)

    df.to_excel("Lost_And_Found_Items.xlsx",index=False)

    print("\nCases Successfully Exported ")
    print("File:Lost_And_Found_Items.xlsx ")

