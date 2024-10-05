from sqlalchemy.orm import Session
from framework.resources.base_resource import BaseResource
from app.models.user import User


class UserResource(BaseResource):

    def __init__(self, config, data_service):
        super().__init__(config)
        self.data_service = data_service
        self.database = "study_tracker"
        self.collection = "User"
        self.key_field = "id"

    def get_by_key(self, key: int) -> User:
        """
        Fetch a user by the user ID.
        """
        result = self.data_service.get_data_object(
            self.database, self.collection, key_field=self.key_field, key_value=key
        )
        return User(**result)

    def create_user(self, user_data: dict):
        """
        Create a new user.
        """
        result = self.data_service.create_data_object(
            self.database, self.collection, user_data
        )
        return result

    def delete_user(self, key: int):
        """
        Delete a user by the user ID.
        """
        self.data_service.delete_data_object(
            self.database, self.collection, key_field=self.key_field, key_value=key
        )
