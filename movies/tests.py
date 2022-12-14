# from django.test import TestCase
# from rest_framework.test import APITestCase
# from rest_framework import status
# # Create your tests here.
# from django.contrib.auth import get_user_model
# from .models import Movie

# from django.urls import reverse

# class MovieTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         testuser1 = get_user_model().objects.create_user(
#             username="testuser1", password="pass"
#         )
#         testuser1.save()

#         testuser2 = get_user_model().objects.create_user(
#             username="testuser2", password="pass"
#         )
#         testuser2.save()

#         test_Movie = Movie.objects.create(
#             name="rake",
#             user=testuser1,
#             description="Better for collecting leaves than a shovel.",
#         )
#         test_Movie.save()


#     def setUp(self):
#         self.client.login(username='testuser1', password="pass")




#     def test_Movies_model(self):
#         Movie = Movie.objects.get(id=1)
#         actual_user = str(Movie.user)
#         actual_name = str(Movie.name)
#         actual_description = str(Movie.description)
#         self.assertEqual(actual_user, "testuser1")
#         self.assertEqual(actual_name, "rake")
#         self.assertEqual(
#             actual_description, "Better for collecting leaves than a shovel."
#         )

    # def test_get_Movie_list(self):
    #     url = reverse("Movie_list")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     Movies = response.data
    #     self.assertEqual(len(Movies), 1)
        

    # def test_auth_required(self):
    #     self.client.logout()
    #     url = reverse("Movie_list")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_only_owner_can_delete(self):
    #     self.client.logout()
    #     self.client.login(username='testuser2', password="pass")
    #     url = reverse("Movie_detail", args=[1])
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)