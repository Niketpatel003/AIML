import random
import matplotlib.pyplot as plt

Students = ["Amit", "Niket", "Jigar", "Het", "Smit", "Dhruv"]
Maths = [random.randint(0,100) for _ in range(6)]
Science = [random.randint(0,100) for _ in range(6)]
Physics = [random.randint(0,100) for _ in range(6)]
English = [random.randint(0,100) for _ in range(6)]
max_maths = max(Maths)
max_science = max(Science)
max_pysics = max(Physics)
max_english = max(English)
plt.plot(Students,Maths,label="Maths")
plt.plot(Students,Science, label="Science")
plt.plot(Students, Physics, label="Physics")
plt.plot(Students, English, label="English")
plt.scatter(Students[Maths.index(max_maths)], max_maths, color='blue', s=100, label="Highest in Maths")
plt.scatter(Students[Science.index(max_science)], max_science, color='orange', s=100, label="Highest in Science")
plt.scatter(Students[Physics.index(max_pysics)], max_pysics, color='green', s=100, label="Highest in Physics")
plt.scatter(Students[English.index(max_english)], max_english, color='red', s=100, label="Highest in English")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks of Students")
plt.legend()
plt.grid(True)
plt.show()