import pynmrstar

#Creating inital saveframe.
#Saveframe (Name, Value)
save_person = pynmrstar.Saveframe.from_scratch("Person", "Name")
##print(Save_Person)
#Now to add a loop for work
work = pynmrstar.Loop.from_scratch()

#add tags into the loop
work.add_tag(['Work_history.Job_title', 'Work_history.Start', 'Work_history.End', 'Work_history.Responsiblity'])
##print(Work)
#add loop into saveframe
save_person.add_loop(work)
#print(Save_Person)
#Now that the loop is within the saveframe, add_tag() & add_data() to the saveframe & loop for Email assignment similarity
save_person.add_tag("First_Name", "ZZZ")
save_person.add_tag("Last_Name", "YYY")
work.add_data(['ZZZ', '01-01-1979', '01-01-1979', 'Programmed Systems'])
work.add_data(['YYY', '01-01-2000', '01-01-2000', 'Hacked the planet'])
print(save_person)

save_person.write_to_file("file_name.str")

#pynmrstar.utils.iter_entries()

