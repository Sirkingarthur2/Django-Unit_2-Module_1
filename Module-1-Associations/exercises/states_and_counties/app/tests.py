from django.test import TestCase
from app.models import *

# Create your tests here.

class StateCountyTests(TestCase):
    def setUp(self):

        self.state = create_state("California", "CA", "California Poppy", "Sacramento")

        self.county1 = create_county("Los Angeles County", "Los Angeles", 10000000, self.state)
        self.county2 = create_county("San Diego County", "San Diego", 3000000, self.state)
        self.county3 = create_county("Sacramento County", "Sacramento", 1500000, self.state)

    def test_create_state(self):
        state = create_state("Texas", "TX", "Bluebonnet", "Austin")
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "Texas")
        self.assertEqual(state.abbreviation, "TX")
        self.assertEqual(state.state_flower, "Bluebonnet")
        self.assertEqual(state.capital_city, "Austin")

    def test_create_county(self):
        county = create_county("Orange County", "Santa Ana", 3000000, self.state)
        self.assertIsInstance(county, County)
        self.assertEqual(county.name, "Orange County")
        self.assertEqual(county.county_seat, "Santa Ana")
        self.assertEqual(county.population, 3000000)
        self.assertEqual(county.state, self.state)

    def test_find_counties_for_state(self):
        counties = find_counties_for_state("CA")
        self.assertIn(self.county1, counties)
        self.assertIn(self.county2, counties)
        self.assertIn(self.county3, counties)
        self.assertEqual(len(counties), 3)

    def test_state_population(self):
        total_population = state_population(self.state)
        self.assertEqual(total_population, 10000000 + 3000000 + 1500000) 

    def test_counties_containing_state_capital(self):
        counties_with_capital = counties_containing_state_capital()
        self.assertIn(self.county3, counties_with_capital)  
        self.assertNotIn(self.county1, counties_with_capital)  
