class DatabaseConnection:
    def __enter__(self):
        print("Database Connected")
    def __exit__(self,exec_type,exec_value,traceback):
        print("Database closed")
with DatabaseConnection():
    print("Performing query")
        