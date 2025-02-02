# python_practice

## Weather app

Few requirement based code  to practice python
## Password validator 
Requirements:
- Check if a password meets the following criteria:
    - At least 8 characters long.
    - Contains at least one uppercase letter.
    - Contains at least one lowercase letter.
    - Contains at least one digit.
- Display whether the password is valid or not and explain why if invalid.



## Contact List

# 📱 Contact List App Requirements

## 1️⃣ Functional Requirements
- ✅ **Add a Contact** → Store name, phone number, email, and address  
- ✅ **View Contacts** → Display a list of saved contacts  
- ✅ **Search Contacts** → Search by name or phone number  
- ✅ **Update a Contact** → Modify existing contact details  
- ✅ **Delete a Contact** → Remove a contact from the list  
- ✅ **Save Data** → Store contacts in a file (`CSV`, `JSON`, or database)  

---

## 2️⃣ Technical Requirements
### 📌 Required Python Modules
- `csv` or `json` → To store contacts in a file  
- `sqlite3` → If using a database instead of files  
- `os` → For file handling and data persistence  
- `prettytable` (optional) → For displaying contacts in a neat table  

### 📌 Programming Concepts Needed
- Functions (for modular code)  
- Lists & dictionaries (to store contacts)  
- File handling (read/write contacts)  
- User input validation (check valid phone/email)  

---

## 3️⃣ Data Structure
Each contact can be stored as:
```python
{
    "name": "John Doe",
    "phone": "123-456-7890",
    "email": "john@example.com",
    "address": "123 Main St, NY"
}
```
If using **CSV**, it looks like:
```csv
name,phone,email,address
John Doe,123-456-7890,john@example.com,123 Main St, NY
```

---

## 4️⃣ Optional Advanced Features
🚀 **GUI Version** → Use **Tkinter** or **PyQt** for a graphical interface  
🚀 **Database Storage** → Use **SQLite** for efficient data handling  
🚀 **Export/Import Contacts** → Allow users to save contacts in CSV/JSON  
🚀 **Error Handling** → Prevent duplicate contacts, handle invalid input  
🚀 **Sorting & Filtering** → Sort contacts alphabetically, filter by category  

---

## 5️⃣ Next Steps
✅ Decide between **CLI or GUI** version  
✅ Choose **file-based or database** storage  
✅ Start with **basic features**, then expand  
