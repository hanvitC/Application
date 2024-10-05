from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService

class StudySessionsResource:
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
        query = f"SELECT * FROM Study_Sessions WHERE user_id = {user_id}"
        result = self.data_service.execute(query)
        return result

    def create_session(self, session_data):
        query = f"INSERT INTO Study_Sessions (user_id, start_time, end_time) VALUES ({session_data['user_id']}, '{session_data['start_time']}', '{session_data['end_time']}')"
        self.data_service.execute(query)

    def delete_session(self, session_id: int):
        query = f"DELETE FROM Study_Sessions WHERE id = {session_id}"
        self.data_service.execute(query)
