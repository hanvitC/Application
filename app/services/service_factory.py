from framework.services.service_factory import BaseServiceFactory
from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService


class ServiceFactory(BaseServiceFactory):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_service(cls, service_name):
        """
        Returns the appropriate service based on the `service_name`.
        """

        # MySQL connection
        context = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "dbuserdbuser"
        }

        if service_name == 'UserResource':
            from app.resources.user_resource import UserResource
            data_service = cls.get_service('UserDataService')
            result = UserResource(config=None, data_service=data_service)
        elif service_name == 'NotesResource':
            from app.resources.notes_resource import NotesResource
            data_service = cls.get_service('NotesDataService')
            result = NotesResource(config=None, data_service=data_service)
        elif service_name == 'StudySessionsResource':
            from app.resources.study_sessions_resource import StudySessionsResource
            data_service = cls.get_service('StudySessionsDataService')
            result = StudySessionsResource(config=None, data_service=data_service)
        elif service_name in ['UserDataService', 'NotesDataService', 'StudySessionsDataService']:
            result = MySQLRDBDataService(context=context)
        else:
            result = None

        return result
