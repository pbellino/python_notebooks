# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] run_control={"frozen": false, "read_only": false}
# [![Notebook Tutorial](__code/__all/notebook_tutorial.png)](https://neutronimaging.pages.ornl.gov/tutorial/notebooks/rename_files/)

# + [markdown] run_control={"frozen": false, "read_only": false}
# <img src='__docs/__all/notebook_rules.png' />

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Select Your IPTS 

# + run_control={"frozen": false, "read_only": false}
from __code.rename_files import NamingSchemaDefinition, FormatFileNameIndex
from __code import system
system.System.select_working_dir()
from __code.__all import custom_style
custom_style.style()

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Select Input Folder

# + [markdown] run_control={"frozen": false, "read_only": false}
# Select input folder that contains all the images you need to rename.

# + run_control={"frozen": false, "read_only": false}
o_format = FormatFileNameIndex(working_dir=system.System.get_working_dir())
o_format.select_input_folder()

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Define New Naming Schema

# + run_control={"frozen": false, "read_only": false}
# keep most dominant files extension
o_format.calculate_most_dominant_files()
o_format.get_most_dominant_files()

o_schema = NamingSchemaDefinition(o_format=o_format)
o_schema.show()

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Select Output Folder

# + run_control={"frozen": false, "read_only": false}
o_schema.select_export_folder()

# +














