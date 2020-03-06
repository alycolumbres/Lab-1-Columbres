from selenium import webdriver
from django.test import TestCase
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def tearDown(self):
		self.browser.quit()

	def test_can_display_a_heroes_list_and_more_information_per_hero(self):
		# Widget has heard about a new wiki app for the game called The Will of the Wisps. 
		# She goes to check out its homepage
		browser.get('http://localhost:8000')

		# She notices the page title and header mention 
		# 'The Will of the Wisps Wiki'
		self.assertIn('The Will of the Wisps Wiki', self.browser.title)
		
	def test_uses_list_template(self):
		# She sees a list containing three heroes with their corresponding 
		# names, health points, and damage 
		response = self.client.get('/heroes')
		self.assertTemplateUsed(response, 'heroes.html')
		
		# When she selects one of the heroes, she is sent to another page
		# containing more information about the hero (additional stats, lore, image).
		response = self.client.get('/hero/cloud')
		self.assertTemplateUsed(response, 'detail_cloud.html')
		# She spots the page title and header mentions the name of the hero she selected.
		self.assertIn('Cloud', self.browser.title)

		response = self.client.get('/hero/sunflowey')
		self.assertTemplateUsed(response, 'detail_sunflowey.html')
		self.assertIn('Sunflowey', self.browser.title)

		response = self.client.get('/hero/jester')
		self.assertTemplateUsed(response, 'detail_jester.html')
		self.assertIn('Jester', self.browser.title)
		
		# While she is in a specific hero's page, she sees a button labeled "Back to Heroes List".
		# She clicks this and she is redirected back to the wiki's homepage.
		self.assertIn('Back to Heroes List', html)
		self.assertTemplateUsed(response, 'heroes.html')
		
		self.fail('Finish the test!')