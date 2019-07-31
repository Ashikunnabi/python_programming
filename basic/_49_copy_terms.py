__pname__    = 'Normal copy VS Shallow copy VS Deep copy'
__author__   = 'Md. Ashikun Nabi'
__email__    = 'ashikunnabituhin@gmail.com'

import copy

# Normal copy
# -Use same memory location
# -Assignment operatior is used for that
nc_old = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nc_new = nc_old

print("Memory location of nc_old", id(nc_old))
print("Memory location of nc_new", id(nc_new))

# ==================================================
print()
# ==================================================

# shallow copy --
# -fully new object
# -just a reference of parent variable
sc_old = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sc_new = copy.copy(sc_old)

sc_old.append([4, 4, 4])

print("Old list:", sc_old)
print("New list:", sc_new)
print("Memory location of sc_new", id(sc_old))
print("Memory location of sc_new", id(sc_new))

print()

# -However, when you change any nested objects in sc_old, 
# the changes appear in sc_new
sc_old[1][1] = "Changed"

print("Old list:", sc_old)
print("New list:", sc_new)
print("Memory location of sc_new", id(sc_old))
print("Memory location of sc_new", id(sc_new))

# ==================================================
print()
# ==================================================

# Deep copy --
# -fully new object
dc_old = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
dc_new = copy.deepcopy(dc_old)

dc_old.append([4, 4, 4])

print("Old list:", dc_old)
print("New list:", dc_new)
print("Memory location of dc_old", id(dc_old))
print("Memory location of dc_new", id(dc_new))

print()

# -However, when you change any nested objects in sc_old, the changes appear in sc_new
dc_old[1][1] = "Changed"

print("Old list:", dc_old)
print("New list:", dc_new)
print("Memory location of dc_old", id(dc_old))
print("Memory location of dc_new", id(dc_new))