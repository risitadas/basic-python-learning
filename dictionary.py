#dictionary is nothing but key value pairs
d1 = {}
#print(type(d1))
d2 = {"Monalisa":"Painting",
      "Von":"Oil",
      "Neptune":"Muses"}
#print(d2)
#print(d2["Von"])
#creating a dictionary ,inside another dictionary
d3 = {"Monalisa":"Painting",
      "Von":"Oil",
      "Neptune":"Muses",
      "Academia":{"i":"Dark","ii":"Aesthethic","iii":"Love"}}
#print(d3["Academia"])
#print(d3["Academia"]["ii"])
#adding elements
d3["Holy"] = "Gran"
d3["The"] = "Weeknd"
d3["i78"] = "Cats"
#deleting one element
del d3["i78"]
#print(d3)
#Functions
#d4=d3.copy()
#del d4["The"]
#print(d3)
#print(d3.keys())
#d3.update({"Taylor":"Swift"})
#print(d3)
#print(d3.items())

