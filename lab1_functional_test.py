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
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention 
		# 'The Will of the Wisps Wiki'
		self.assertIn('The Will of the Wisps Wiki', self.browser.title)
		
		# She sees a list containing three heroes with their corresponding 
		# names, health points, and damage 
		seld.assertIn(self.browser.current_url,
			'http://localhost:8000/heroes')
		
		# When she selects one of the heroes, she is sent to another page
		# containing more information about the hero (additional stats, lore, image).
		self.browser.get('http://localhost:8000/hero/cloud')

		self.assertIn('Health Points', self.browser.find_element_by_id('hero_health').text)

		self.assertIn('Base Attack Damage', self.browser.find_element_by_id('hero_attack').text)

		self.assertIn('Skills', self.browser.find_element_by_id('hero_skills').text)

		self.assertIn('Lore', self.browser.find_element_by_id('hero_lore').text)

		self.assertIn('.png', self.browser.find_element_by_id('hero_image').get_attribute('src'))
		# She spots the page title and header mentions the name of the hero she selected.
		self.assertIn('Detail - ', self.browser.title)
		
		# While she is in a specific hero's page, she sees a button labeled "Back to Heroes List".
		# She clicks this and she is redirected back to the wiki's homepage.
		
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings = 'ignore')