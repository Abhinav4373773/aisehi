import subprocess

# Define the path to your notebook
notebook_path = "starting_bert.ipynb"

# Execute the notebook
subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", notebook_path], check=True)
