filename = input("filename = ")
f_extns = filename.split(".")
print("extension = " + repr(f_extns[-1]))
if f_extns=="py":
    print("python")
elif f_extns==".js":
    print("javascript")
    
    
