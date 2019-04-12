import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

varieties = []
norway = []
globe = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			varieties.append(row)
			line_count += 1
		elif row[4] == "NOR":
			norway.append([int(row[0]), row[5], row[6], row[7]])
		else:
			globe.append([int(row[0]), row[5], row[6], row[7]]) 
		line_count += 1

print('total medal for Norway:', len(norway))
print('********************************************************')
print('total medals for everyone else:', len(globe))
print('********************************************************')
print('processed', line_count, 'rows of data')
print('********************************************************')

gold_1924 = []
gold_1948 = []
gold_1972 = []
gold_2002 = []
gold_2014 = []

for medal in norway: 
	if medal[0] == 1924 and medal[3] == "Gold":
		gold_1924.append(medal)

	if medal[0] == 1948 and medal[3] == "Gold":
		gold_1948.append(medal)

	if medal[0] == 1972 and medal[3] == "Gold":
		gold_1972.append(medal)

	if medal[0] == 2002 and medal[3] == "Gold":
		gold_2002.append(medal)

	if medal[0] == 2014 and medal[3] == "Gold":
		gold_2014.append(medal)

print('Norway won', len(gold_1924), 'gold medals in 1924')
print('********************************************************')
print('Norway won', len(gold_1972), 'gold medals in 1972')
print('********************************************************')
print('Norway won', len(gold_2014), 'gold medals in 2014')
print('********************************************************')

Years = ('1924', '1948', '1972', '2002', '2014')
medal_norway = [len(gold_1924), len(gold_1948), len(gold_1972), len(gold_2002), len(gold_2014)]

plt.plot(Years, medal_norway, color='skyblue')
plt.xlabel('Years')
plt.ylabel('Gold-medals')
plt.title('NORWAY WINS GOLD MEDALS')

plt.show()
