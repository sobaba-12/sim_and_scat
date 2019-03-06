---
interact_link: content/practicalities/visualise.ipynb
title: 'Visualise the simulation'
prev_page:
  url: /practicalities/intro
  title: 'Practicalities'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

## Visualise the structure

First of all it would be nice to see the structure of the molecule that we have simulated. 
Using the Python code below, it is possible to load and present the simulation trajectory. 
This can also be achieved offline by using software such as [VMD](https://www.ks.uiuc.edu/Research/vmd/).



{:.input_area}
```python
import MDAnalysis as mda
import nglview as nv
```




{:.input_area}
```python
u = mda.Universe('../assets/lysozyme.pdb')
```




{:.input_area}
```python
view = nv.show_mdanalysis(u)
view
```


From this it is clear that there are no water molecules in the visualisation. 
While there were some in the simulation we have removed them for ease of visualisation, and in our rough comparison with experimental data we will assume complete background substraction.
