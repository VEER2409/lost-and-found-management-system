# Lost & Found Management System

A Python and MySQL based **Lost & Found Management System** designed to help reception staff register found items, manage cases, and handle employee claims.

## 📌 Project Overview

This project provides a simple command-line system for managing lost and found items.

Reception staff can:

* Register found items
* View all found-item cases
* Search for a case using Case ID
* Update case information
* Delete cases
* Create claims for found items
* Export found-item data to Excel

The system uses **MySQL** for data storage and Python for application logic.

## ✨ Features

### Case Management

* Register a found item
* Automatically generate Case IDs
* View all found cases
* Search cases by Case ID
* Update case information
* Delete cases
* Categorize found items

### Claim Management

* Create a claim for a found item
* Automatically generate Claim IDs
* Store claimant information
* Store claim date and description
* Link claims to found-item cases using `case_id`
* Maintain claim status using MySQL

### Excel Export

* Export found-item records from MySQL to Excel
* Generate `Lost_And_Found_Items.xlsx`

## 🛠️ Technologies Used

* **Python**
* **MySQL**
* **MySQL Connector/Python**
* **Pandas**
* **OpenPyXL**
* **Rich**

## 📂 Project Structure

```text
lost_and_found/
│
├── main.py
├── database.py
├── ui.py
├── validators.py
├── models.py
├── case_crud.py
├── claim_crud.py
├── export_excel.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 🗄️ Database

The project uses MySQL to store the application data.

Main tables:

### `found_items`

Stores information about found items and their cases.

### `claims`

Stores claims made against found items.

The `claims` table uses `case_id` as a foreign key referencing the `found_items` table.

This creates a relationship between a found item and its claim.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project

```bash
cd lost_and_found
```

### 3. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure MySQL

Make sure your MySQL server is running and create the required database.

Update the database connection settings in `database.py`.

### 6. Run the application

```bash
python main.py
```

## 📋 Main Menu

```text
1. Case Management
2. Claim Management
3. Export Data To Excel
4. Exit
```

## 🎯 Project Purpose

This project was created to practice:

* Python programming
* Functions and modules
* CRUD operations
* MySQL database integration
* SQL queries
* Foreign key relationships
* Input validation
* Data export using Pandas
* Building a modular command-line application

## 🔮 Future Improvements

Possible future improvements include:

* More advanced claim verification
* Automatic status updates after claim approval
* Improved Excel formatting
* Better error handling
* Authentication and employee login
* More detailed reports
* Improved user interface

## 👨‍💻 Author

Viresh Shankad

Built as a Python + MySQL learning project.
