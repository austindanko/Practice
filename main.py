import pynmrstar
entry15000 = pynmrstar.Entry.from_database(15000)
#Overall entry structure, remove # below
#entry15000.print_tree()

#Creating inital saveframe.
Save_Person = pynmrstar.Saveframe.from_scratch("Name", "Name") #Name being the tag within my initial saveframe, but why does it need to be quoted twice?
print(Save_Person)
#Now to add a loop for work
Work = pynmrstar.Loop.from_scratch()
print(Work)