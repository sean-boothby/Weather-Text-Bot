## Make a new method for each person
## Later on, this is a classic OOP type of problem

EMAIL_ADDRESS = ""
PASSWORD = ""
API_KEY = "367045e5786e71ee343275158bdc6d8b"

def name(name,email):
    FNAME = name.split()[0]
    LNAME = name.split()[1]
    return FNAME, LNAME, email


