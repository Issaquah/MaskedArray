
import numpy as np
import numpy.ma as ma                                   # using numpy.ma module used to mask elements of an array

array1 = np.array([1, 2, 3, 4])                        
array2 = ma.array([1, 2, 3, 4], mask=[0, 0, 0, 1])      # masking the last element of array as invalid using mask attribute

print(array1)
print("")
print(array2)


# In[ ]:


# CREATING MASKED ARRAYS
# masked array can be careted by taking a view of the already created array and setting mask of view as nomask(false)

import numpy as np
import numpy.ma as ma                                   # using numpy.ma module used to mask elements of an array

x = np.array([1, 2, 3, 4])
print(x.view(ma.MaskedArray))       # prints masked array with view of array, mask(here no entry masked so nomask i.e, false)
x = np.array([(1,1), (2,2), (3,3), (4,4)], dtype = [('a',int), ('b', float)]     # create a masked-array with mask= nomask and data-type of values in array 
x.view(ma.MaskedArray)     


# In[ ]:


# ACCESING ONLY VALID ENTRIES OF A MASKED ARRAY
# 1 indicates a invalid entry as a boolean true returns 
# 0 indicates a valid entry opposite to what a bolean true does 
import numpy as np
import numpy.ma as ma                                   # using numpy.ma module used to mask elements of an array

x = ma.array([[1, 2], [3, 4]], mask=[[0, 1], [1, 0]])   # using mask attribute to mask the values 
x[~x.mask]                                              # valid entries can be accessed using the ~ operator 


# In[ ]:


# ACCESING ONLY VALID ENTRIES OF A MASKED ARRAY
import numpy as np
import numpy.ma as ma                                   # using numpy.ma module used to mask elements of an array

x = ma.array([[1, 2], [3, 4]], mask=[[0, 1], [1, 0]])
x.compressed()                                          # compressed() method returns a 1 dimensional ndarray object of valid entries


# In[ ]:


# MASKING AN ENTRY/ ENTRIES

# value(s) in an array can be masked by assigning a special value 'masked' to them
# use ma.masked by specifying the entries to mask

import numpy as np
import numpy.ma as ma  

# 1)MASKING A SINGLE ENTRY
x = ma.array([1, 2, 3,4])         # creating an array
x[1] = ma.masked                  # masking the 2nd entry from the array using ma.masked
x

# 2)MASKING MULTIPLE ENTRIES
y = ma.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])      # creating an ndarray
y[(0, 1, 2), (1, 2, 0)] = ma.masked                  # specifying the entries that are to be masked and then using the masked value on them invoking the ma
y

# 3)MASKED ENTRY IS INDICATED AS TRUE
# WE CAN MASK ENTRIES OF AN ARRAY/ WHOLE ARRAY BY ASSIGNING 'TRUE' TO MASK
z = ma.array([1, 2, 3,4])         # creating an array
z.mask = True                     # assigning 'True' to the mask. This way all the entries will be masked in the array
z


# In[ ]:


# UNMASKING AN ENTRY/ ENTRIES
# we can unmask an entry by specifying a valid values to them

x = ma.array([1, 2, 3], mask=[0, 0, 1])     # unmask 1st two values and only mask he last value 
x

x[-1] = 5                                   # last value was  invalid/ masked so now add a valid value to array
x

