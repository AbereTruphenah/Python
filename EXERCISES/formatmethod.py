min_age="18"
#use of variable assignment
print("The minimum age required for one to apply for a national identity card is {} years.".format(min_age))
#use of indexes
print("Anyone above age {1} is considered as an adult and anyone from age {2} to age {0} is still a child.".format("17",min_age,"0"))
#use keyword arguments
print("{student} was punished by {teacher} for failing exams and she is just under {age}. She went and complained to her mother {mother} who reported {teacher} to the {principle}".format(student="Mary",teacher="Mr. Bundi",mother="Agnes",principle="school principle", age=min_age))



name="Ganymede"
planet="Mars"
gravity="1.43"
template="""
Gravity Facts about {name}
--------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""
print(template.format(name=name,gravity=gravity,planet=planet))