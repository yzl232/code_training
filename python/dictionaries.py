# encoding=utf-8
'''
list =>dict。 一般用zip

'''

w={"house":"Haus","cat":"Katze","red":"rot"}
print w.items()
print w.values()
print w.keys()


dishes = ["pizza", "sauerkraut", "paella", "Hamburger"]
countries = ["Italy", "Germany", "Spanien", "USA"]

country_specialities = zip(countries, dishes)
print country_specialities
country_specialities_dict = dict(country_specialities)
print country_specialities_dict
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print c

a = b = c = range(20)
print zip(a, b, c)
#zip作用就是产生针对n个list,  产生一个n元tuple的list
'''
>>> sorted(d)
[-5, 1, 7]
>>> d
{1: 5, -5: 2, 7: 9}
'''