class Queries:
    CREATE_REVIEW_TABLE = """
        CREATE TABLE IF NOT EXISTS review (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, 
            contact TEXT, 
            date_visit INTEGER, 
            food_quality TEXT, 
            clean_est TEXT, 
            add_comment TEXT
        )
    """