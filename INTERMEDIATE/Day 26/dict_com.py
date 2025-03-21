
subject=["Physics","Math","Chemistry","English","Computer"]
import random
dict={sub:random.randint(1,100) for sub in subject}


passed={subject:score for (subject,score) in dict.items() if score>60}

for (key,value) in dict.items():
    print(key)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list=sentence.split()
result = {key:len(key) for key in word_list}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {key:round(value*1.4+32,2) for (key,value) in weather_c.items()}

print(weather_f)