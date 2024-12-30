from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=2, unique=True)
    state_flower = models.CharField(max_length=100)
    capital_city = models.CharField(max_length=100)

class County(models.Model):
    name = models.CharField(max_length=100)
    county_seat = models.CharField(max_length=100)
    population = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='counties')

def create_state(name, abbreviation, state_flower, capital_city):
    state = State.objects.create(name=name, abbreviation=abbreviation, state_flower=state_flower, capital_city=capital_city)
    return state

def create_county(name, county_seat, population, state):
    county = County.objects.create(name=name, county_seat=county_seat, population=population, state=state)
    return county

def find_counties_for_state(abbreviation):
    return County.objects.filter(state__abbreviation=abbreviation)

def state_population(state):
    total_population = 0
    counties = state.counties.all() 
    for county in counties:
        total_population += county.population 
    return total_population

def counties_containing_state_capital():
    counties_with_capital = []
    counties = County.objects.all()
    for county in counties:
        if county.county_seat == county.state.capital_city:  
            counties_with_capital.append(county)
    return counties_with_capital