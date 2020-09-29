import pynmrstar
entry15000 = pynmrstar.Entry.from_database(15000)
#Overall entry structure, remove # below
#entry15000.print_tree()

#Creating inital saveframe.
Save_Person = pynmrstar.Saveframe.from_scratch("Name", "Name") #Name being the tag within my initial saveframe, but why does it need to be quoted twice?
##print(Save_Person)
#Now to add a loop for work
Work = pynmrstar.Loop.from_scratch()

#add tags into the loop
Work.add_tag(['Work_history.Job_title', 'Work_history.Start', 'Work_history.End', 'Work_history.Responsiblity'])
##print(Work)
#add loop into saveframe
Save_Person.add_loop(Work)
#print(Save_Person)
#Now that the loop is within the saveframe, add_tag() & add_data() to the saveframe & loop for Email assignment similarity
Save_Person.add_tag("ZZZ", "YYY")
Work.add_data(['n/a', '01-01-1979', '01-01-1979', "Programmed Systems"])
print(Save_Person)