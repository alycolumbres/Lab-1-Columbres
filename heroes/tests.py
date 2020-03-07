from django.test import TestCase

# Create your tests here.
class TestForHeroes(TestCase):

	def test_heroes_if_correct_response_(self):
		response = self.client.get('/heroes')
		self.assertTemplateUsed(response, 'heroes.html')

class TestForHeroCloud(TestCase):

	def test_hero_cloud_if_correct_response_(self):
		response = self.client.get('/hero/cloud')
		self.assertTemplateUsed(response, 'detail_cloud.html')

class TestForHeroSunflowey(TestCase):

	def test_hero_sunflowey_if_correct_response_(self):
		response = self.client.get('/hero/sunflowey')
		self.assertTemplateUsed(response, 'detail_sunflowey.html')

class TestForHeroJester(TestCase):

	def test_hero_jester_if_correct_response_(self):
		response = self.client.get('/hero/jester')
		self.assertTemplateUsed(response, 'detail_jester.html')