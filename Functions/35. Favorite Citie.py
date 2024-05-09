print("#####--------35. Favorite Cities--------#####")

class City:
    def __init__(self, name, country, population, landmarks, founded, nickname):
      self.name = name
      self.country = country
      self.population = population
      self.landmarks = landmarks
      self.founded = founded
      self.nickname = nickname

Bucaramanga = City('Bucaramanga', 'Colombia', 581130, 'Puente la Novena', 1622, 'Ciudad Bonita')
Brisbane = City('Brisbane', 'Australia', 2280000, 'History Bridge', 1824, 'Brisbanistan')

print(vars(Bucaramanga))
print(vars(Brisbane))
