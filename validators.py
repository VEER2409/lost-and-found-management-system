from datetime import datetime

#validator for other fields------------------------------

def validate_required(value,field_name):
    if not value.strip():
        return False,f"{field_name} cannot be empty "
    return True,""

def get_required_input(field_name):
    while True:
        value=input(f"{field_name}: ")

        valid,message=validate_required(value,field_name)

        if valid:
            return value
        print(message)


#validator for date---------------------------------------


def validate_date(date_text):
    try:
        datetime.strptime(date_text,"%Y-%m-%d")
        return True,""
    except ValueError:
       return False , "data must be in YYYY-MM-DD format."


def check_date_format():
    while True:
            found_date = input("Found Date (YYYY-MM-DD): ")

            valid, message = validate_date(found_date)

            if valid:
                return found_date

            print(message)