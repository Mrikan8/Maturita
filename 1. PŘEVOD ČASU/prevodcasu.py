cas = int(input('Zadej čas v sekundách: '))

dny = cas // 86400
zbyvajici_sekundy = cas % 86400

hodiny = zbyvajici_sekundy // 3600
zbyvajici_sekundy %= 3600

minuty = zbyvajici_sekundy // 60
sekundy = zbyvajici_sekundy % 60

print(f'{cas} sekund je {dny} dní, {hodiny} hodin, {minuty} minut a {sekundy} sekund.')