import os

def create_readme():
    """Creates a README.md file with project name and description."""
    filename = "README.md"
    content = "# basket\nbasket game python"

    try:
        with open(filename, "w") as f:
            f.write(content)
        # print(f"Successfully created {filename}") # Removed print as per instructions
    except IOError as e:
        # print(f"Error creating {filename}: {e}") # Removed print as per instructions
        pass # Handle error silently as per instructions (no output)

if __name__ == "__main__":
    create_readme()