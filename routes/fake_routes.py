"""
Make some fake routes for testing purposes
"""

from flask_restful import Resource
from tests.create_users import set_up_test_database


class TestData(Resource):
    """
    Class to be used for generating fake data
    """

    def post(self):
        """
        Create the default fake data
        """
        message = set_up_test_database()
        return {"status": "success", "messages": [message]}
