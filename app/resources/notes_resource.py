from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService

class NotesResource:
    def __init__(self, config=None):
        # Define the connection context with the database name
        context = {
            'user': 'root',
            'password': 'dbuserdbuser',
            'host': 'localhost',
            'port': 3306,
            'database': 'study_tracker'  # Specify the database name here
        }
        self.data_service = MySQLRDBDataService(context=context) if config is None else MySQLRDBDataService(context=config)

    def get_by_user(self, user_id: int):
        query = f"SELECT * FROM Notes WHERE user_id = {user_id}"
        result = self.data_service.execute(query)
        return result

    def create_note(self, note_data):
        query = f"INSERT INTO Notes (user_id, title, created_date) VALUES ({note_data['user_id']}, '{note_data['title']}', NOW())"
        self.data_service.execute(query)

    def delete_note(self, note_id: int):
        query = f"DELETE FROM Notes WHERE id = {note_id}"
        self.data_service.execute(query)
