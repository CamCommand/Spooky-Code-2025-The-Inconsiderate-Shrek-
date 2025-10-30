import random
import string
import csv
import webbrowser
import time

with open('Facts.csv', 'r') as read_obj:
    # Create a CSV reader object
    csv_reader = csv.reader(read_obj)
    
    # Convert the CSV reader object to a list
    facts_list_of_rows = list(csv_reader)

while True:
	string.ascii_lowercase
	alpha = list(string.ascii_lowercase)

	print("Enter your name:")
	name = input()
	
	if name == "":
		name = "Chris Wells"		
	
	for char in name:
			Name_chance = random.randrange(1, 100)
			if Name_chance >= 70:
				name = name.replace(char, random.choice(alpha))
	
	print(f"Hi {name}, dumb name.")
	f = ' '.join(random.choice(facts_list_of_rows))
	print("Anyway, did you know,")
	print(f"{f}\n")
	print("See for yourself!")
	time.sleep(5)
	webbrowser.open('https://drive.google.com/file/d/1NezVaMIuVH1Gt0cHCQMT3JeJu7JuxlIG/view?usp=drive_link')
