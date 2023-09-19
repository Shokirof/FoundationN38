#1
import random

student_ids = ['S001', 'S002', 'SOO3', 'S004']
student_names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
student_scores = [85, 98, 89, 92]

student_data = {}

for i in range(len(student_ids)):
    student_data[student_ids[i]] = (student_names[i], student_scores[i])

print(student_data)
#2
string = "w3resource"

dc = {}

for character in string:
    if character not in dc:
        dc[character] = 1
    else:
        dc[character] += 1

print(dc)
#4
string = "Salom Yoz.Olam juda ham go'zal.Imtihon bo'lyapti"

words = []
sentences = []

for sentence in string.split(". "):
    sentences.append(sentence)

for sentence in sentences:
    for word in sentence.split():
        words.append(word)

print("words:", words)
print("sentences:", sentences)
#5
numbers = [1, 2, 3]

largest_number = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] > largest_number:
        largest_number = numbers[i]

print(largest_number)

numbers = [61, 228, 9]

largest_number = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] > largest_number:
        largest_number = numbers[i]

print(largest_number)

#6
data = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

dc = {}

for row in data:
    key = row[0]
    value = [row[1], row[2]]
    dc[key] = value

print(dc)
#1
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic_all = {}

dic_all.update(dic1)
dic_all.update(dic2)
dic_all.update(dic3)

print(dic_all)

#2
N = int(input("N ni kiriting: "))

dictionary = {}

for i in range(1, N + 1):
  key = i
  value = i * i
  dictionary[key] = value

print(dictionary)
#5
list1 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

sum_list = []

for tup in list1:
    sum = 0
    for num in tup:
        sum += num
    sum_list.append(sum)

print(sum_list)

#6
input_list = [(1, 2), (2, 3), (3, 4)]

output_list = []

for tuple in input_list:
    output_list.append(list(tuple))

print(output_list)
