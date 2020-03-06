from django.test import TestCase

# Create your tests here.
class TaskListPageTest(TestCase):

	def test_uses_list_template(self):
		response = self.client.get('/heroes')
		self.assertTemplateUsed(response, 'heroes.html')

		response = self.client.get('/hero/cloud')
		self.assertTemplateUsed(response, 'detail_cloud.html')

		response = self.client.get('/hero/sunflowey')
		self.assertTemplateUsed(response, 'detail_sunflowey.html')

		response = self.client.get('/hero/jester')
		self.assertTemplateUsed(response, 'detail_jester.html')