from ui import show_category

#category selection------------------------------------------

def get_category():
    categories={
        "1": "Electronics",
        "2": "ID / Documents",
        "3": "Jewelry",
        "4": "Bags & Accessories",
        "5": "Clothing",
        "6": "Books & Stationery",
        "7": "Keys",
        "8": "Office Equipment",
        "9": "Personal Items",
        "10": "Other"
    }

    while True:
        show_category()
        choice=input("Enter your choice - ")

        if choice in categories:
            return categories[choice]
        print("Invalid choice. Please select a category from the menu. ")