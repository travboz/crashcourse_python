# import printing_models_export as pm # importing and aliasing

# # Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# pm.print_models(unprinted_designs, completed_models)
# pm.show_completed_models(completed_models)

# could also do this:
from printing_models_export import print_models as pm
from printing_models_export import show_completed_models as showcm
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
pm(unprinted_designs, completed_models)
showcm(completed_models)