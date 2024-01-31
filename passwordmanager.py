import getpass
import os
import mysql.connector

# Function to store a new password
def store_password():
    site = input("Enter the site name: ")
    username = input("Enter the username: ")
    password = getpass.getpass("Enter the password: ")

    # Connect to the database
    cnx = mysql.connector.connect(user=os.getenv('DB_USER'), 
                                  password=os.getenv('DB_PASS'),
                                  host=os.getenv('DB_HOST'),
                                  database=os.getenv('DB_NAME'))
    cursor = cnx.cursor()

    # Insert the data into the database
    add_password = ("INSERT INTO passwords "
                   "(site, username, password) "
                   "VALUES (%s, %s, %s)")
    data_password = (site, username, password)
    cursor.execute(add_password, data_password)

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()

    print("Password saved successfully.")

# Function to retrieve a stored password
def get_password():
    site = input("Enter the site name: ")
    username = input("Enter the username: ")

    # Connect to the database
    cnx = mysql.connector.connect(user=os.getenv('DB_USER'), 
                                  password=os.getenv('DB_PASS'),
                                  host=os.getenv('DB_HOST'),
                                  database=os.getenv('DB_NAME'))
    cursor = cnx.cursor()

    # Query to get the password
    query = ("SELECT password FROM passwords WHERE site = %s AND username = %s")
    cursor.execute(query, (site, username))

    # Fetch the password
    result = cursor.fetchone()
    if result is None:
        print("No password found for this site and username.")
        return

    password = result[0]

    print("The password is: ", password)

    cursor.close()
    cnx.close()

# Function to update a stored password
def update_password():
    site = input("Enter the site name: ")
    username = input("Enter the username: ")
    new_password = getpass.getpass("Enter the new password: ")

    # Connect to the database
    cnx = mysql.connector.connect(user=os.getenv('DB_USER'), 
                                  password=os.getenv('DB_PASS'),
                                  host=os.getenv('DB_HOST'),
                                  database=os.getenv('DB_NAME'))
    cursor = cnx.cursor()

    # Update the password in the database
    update_password = ("UPDATE passwords SET password = %s WHERE site = %s AND username = %s")
    data_password = (new_password, site, username)
    cursor.execute(update_password, data_password)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()

    print("Password updated successfully.")

# Function to delete a stored password
def delete_password():
    site = input("Enter the site name: ")
    username = input("Enter the username: ")

    # Connect to the database
    cnx = mysql.connector.connect(user=os.getenv('DB_USER'), 
                                  password=os.getenv('DB_PASS'),
                                  host=os.getenv('DB_HOST'),
                                  database=os.getenv('DB_NAME'))
    cursor = cnx.cursor()

    # Delete the password from the database
    delete_password = ("DELETE FROM passwords WHERE site = %s AND username = %s")
    cursor.execute(delete_password, (site, username))

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()

    print("Password deleted successfully.")    

# Main function to run the password manager
def main():
    while True:
        print("1. Store password")
        print("2. Retrieve password")
        print("3. Update password")
        print("4. Delete password")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            store_password()
        elif choice == '2':
            get_password()
        elif choice == '3':
            update_password()
        elif choice == '4':
            delete_password()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()