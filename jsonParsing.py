import json

courses='{"name": "Ganesh", "Languages":["Java", "Python"]}' #Json stored as string in variable named courses

#Method named 'loads' parses the json string and returns Dictionary object

dict_courses = json.loads(courses)
print(type(dict_courses)) #to verify if the type of dict_courses is of dictionary or not
print(dict_courses)
print(dict_courses['name']) # to print value of key named "name"
print(dict_courses['Languages'])

#to print value "Java"
print(dict_courses['Languages'][0])

#to write the above entire process in single step to print "Java"
print((json.loads('{"name": "Ganesh", "Languages":["Java", "Python"]}'))['Languages'][0])

#********* Parse content present in json file
with open('C:\\Users\\LENOVO\\Documents\\Json files\\course.json') as f:
    file_data=json.load(f)
    print("type of 'file_data' is ",type(file_data))
    print("Printing second title from the file is ", file_data['courses'][1]['title'])