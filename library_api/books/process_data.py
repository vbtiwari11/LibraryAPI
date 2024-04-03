import pandas as pd
from datetime import datetime,timedelta


library_data = {
    'Title': ['Book 1', 'Book 2', 'Book 3'],
    'Available Copies': [5, 3, 7]
}
library_df = pd.DataFrame(library_data)

# Create users DataFrame
users_data = {
    'User ID': ['S001', 'S002', 'L001'],
    'Type': ['Student', 'Student', 'Librarian']
}
users_df = pd.DataFrame(users_data)

# Create borrowing history DataFrame
borrowing_data = {
    'User ID': [],
    'Title': [],
    'Borrowed Date': [],
    'Return Date': [],
    'Renewals': []
}
borrowing_df = pd.DataFrame(borrowing_data)

def get_data_from_df(type,userrprofile):
    print(type,userrprofile)
    df=pd.read_csv(r'C:\Users\VAITIWAR\PycharmProjects\LibraryApi\library_api\data.csv')
    profile=str(userrprofile)
    res_df=df[(df['userid']==int(type)) & (df['userprofile']==profile)]
    return res_df


def borrow_book(user_id, title):
    if user_id.startswith('S'):  # Student
        if user_id not in borrowing_df['User ID'].values and len(
                borrowing_df[borrowing_df['User ID'] == user_id]) == 2:
            return "You have already borrowed maximum number of books."

    if title not in library_df['Title'].values or library_df.loc[library_df['Title'] == title, 'Available Copies'].iloc[
        0] == 0:
        return "The book is not available at the moment."

    library_df.loc[library_df['Title'] == title, 'Available Copies'] -= 1
    borrowing_df.loc[len(borrowing_df)] = [user_id, title, datetime.now(), datetime.now() + timedelta(days=30), 0]
    return "Book borrowed successfully."


# Function to return a book
def return_book(user_id, title):
    if title not in borrowing_df[borrowing_df['User ID'] == user_id]['Title'].values:
        return "You have not borrowed this book."

    library_df.loc[library_df['Title'] == title, 'Available Copies'] += 1
    borrowing_df.drop(borrowing_df[(borrowing_df['User ID'] == user_id) & (borrowing_df['Title'] == title)].index,
                      inplace=True)
    return "Book returned successfully."


def renew_book(user_id, title):
    if title not in borrowing_df[borrowing_df['User ID'] == user_id]['Title'].values:
        return "You have not borrowed this book."

    if borrowing_df[(borrowing_df['User ID'] == user_id) & (borrowing_df['Title'] == title)]['Renewals'].iloc[0] >= 1:
        return "You have already renewed this book once."

    borrowing_df.loc[
        (borrowing_df['User ID'] == user_id) & (borrowing_df['Title'] == title), 'Return Date'] += timedelta(days=30)
    borrowing_df.loc[(borrowing_df['User ID'] == user_id) & (borrowing_df['Title'] == title), 'Renewals'] += 1
    return "Book renewed successfully."

def check_library():
    return library_df.to_dict(orient='records')

def check_borrowed_books(user_id):
    return borrowing_df[borrowing_df['User ID'] == user_id]

# Function to check user's borrowing history
def check_borrowing_history(user_id):
    return borrowing_df[borrowing_df['User ID'] == user_id]


def check_book_availability(title):
    if title not in library_df['Title'].values:
        return "The book is not available in the library."
    else:
        available_copies = library_df.loc[library_df['Title'] == title, 'Available Copies'].iloc[0]
        if available_copies > 0:
            return f"The book is available. {available_copies} copies are available for borrowing."
        else:
            latest_return_date = max(borrowing_df[borrowing_df['Title'] == title]['Return Date'])
            return f"The book is not available at the moment. The latest return date for this book is {latest_return_date}."
