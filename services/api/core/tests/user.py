from rest_framework.test import APITestCase, APIRequestFactory
# from django.contrib.auth import get_user_model


# User = get_user_model()


class UserTests(APITestCase):
    def test_unauthorized_cannot_get(self):
        assert False

    def test_unatuhorized_cannot_list(self):
        assert False
    
    def test_unauthorized_cannot_post(self):
        assert False
    
    def test_unauthorized_cannot_put(self):
        assert False
    
    def test_unauthorized_cannot_patch(self):
        assert False
