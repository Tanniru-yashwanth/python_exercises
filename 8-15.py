'''Put the functions for the example printing_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of printing_models.py, and modify the file to use the imported functions'''


import printing_functions
unprinted_design = ['phone case', 'robot pendant', 'dodecahedron']
completed_model = []
printing_functions.print_models(unprinted_design, completed_model)
printing_functions.show_completed_models(completed_model)
print(unprinted_design)
print(completed_model)
