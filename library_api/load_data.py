import pandas as pd

library_data = {
    'Title': ['Book 1', 'Book 2', 'Book 3'],
    'Available Copies': [5, 3, 7]
}
library_df = pd.DataFrame(library_data)

# Create users DataFrame
users_data = {
    'User ID': ['U001', 'U002', 'U003'],
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
