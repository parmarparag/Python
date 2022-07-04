mydict={
    "Parag" : "Founder",
    "Mayur":"Python Developer",
    "Dhairya" : "Talk Master",
    "Nisarg" : "Bussiness Man",
    "marks" : [12,25]
}

print(mydict.keys())
print(mydict.values())
updatedict={
"kajal" : "House Wife",
"Sanaya" : "cute girl"
}
mydict.update(updatedict)
print(mydict)
print(mydict.get("Parag"))