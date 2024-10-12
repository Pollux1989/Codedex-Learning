# 1 - Call countryinfo import CountryInfo

from countryinfo import CountryInfo 
import matplotlib.pyplot as plt
import pandas as pd

# 2 - Create an Input for the country name
country_1 = CountryInfo(input('Enter 1 country: '))
country_2 = CountryInfo(input('Enter 2 country: '))
country_3 = CountryInfo(input('Enter 3 country: '))
country_4 = CountryInfo(input('Enter 4 country: '))
country_5 = CountryInfo(input('Enter 5 country: '))

# 3 listas que iran en la tabla
c_name = [ country_1.name(), country_2.name(), country_3.name(), country_4.name(), country_5.name()]
c_capital = [country_1.capital(), country_2.capital(), country_3.capital(), country_4.capital(), country_5.capital()]
c_area = [ country_1.area(), country_2.area(), country_3.area(), country_4.area(), country_5.area()]
c_population = [ country_1.population(), country_2.population(), country_3.population(), country_4.population(), country_5.population()]

# 4 creando tabla y Dataframe
country_info = { 'Country':c_name, 'Capital': c_capital, 'Area': c_area, "Population": c_population}
data_countries = pd.DataFrame(country_info)

# 5 Imprimiendo en la consola
print(data_countries)

#6 Guardando el archivo en CSV
data_countries.to_csv('countries.csv', index = False)

#7 Generacion de graficos
colors_list = ['cyan', 'yellowgreen', 'orange', 'lightblue', 'Grey']
explode_values = (0.1, 0.1, 0.1, 0.1, 0.1)

fg, ax = plt.subplots()

ax.pie (country_info["Population"], labels= c_population, 
         autopct = '%1.1f%%', colors = colors_list, 
         explode= explode_values, shadow = False,
         startangle = 90, counterclock = False, 
         wedgeprops = {'linewidth' : 1, 'edgecolor' :'black'})

plt.title ('Country Population Comparator', color = "blue",
            fontsize = "25", fontweight = "bold", )

plt.legend(c_name, loc = 'lower right' )

ax.axis('equal')
plt.show()







