my_list = ["blue","orange","pink","blue","beige","red","pink"]

# set takes {} syntax, list takes [] syntax 
my_colors = {color for color in my_list}

print(my_colors)

univ_students = {"Joy":["Mechanical", "Computer Science"],"Raj":["Mining","Metallurgy","Physics"],"Sita":["Computer Science","Electronics"],"Ram":["Physics","Electronics"]}
# print(univ_students.values())
unique_branches = {branch for students in univ_students.values() for branch in students}

print(unique_branches)

# python comprehension can take multuple for loops also if condition is not important to put