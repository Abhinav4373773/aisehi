import subprocess

# Define the path to your notebook
notebook_path = "path/to/your_notebook.ipynb"

# Execute the notebook
subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", notebook_path], check=True)
