import os

def add_imports(file_path, imports):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Check if imports already exist
    for imp in imports:
        if imp in content:
            continue
        
        # Add import at the beginning of the file
        content = imp + '\n' + content
    
    with open(file_path, 'w') as file:
        file.write(content)

def update_files():
    base_dir = '.'  # Adjust this if your script is not in the project root
    
    # Define the imports to add
    exception_import = 'from .exceptions import AIConsensusError, ModelQueryError, VotingError, DatabaseError'
    logger_import = 'from .logger import logger'
    config_import = 'from .config import Config'
    
    # List of files to update
    files_to_update = [
        'models/base_model.py',
        'models/openai.py',
        'models/azure.py',
        'models/groq.py',
        'models/anthropic.py',
        'models/gemini.py',
        'db_manager.py',
        'main.py',
    ]
    
    for file in files_to_update:
        file_path = os.path.join(base_dir, file)
        if os.path.exists(file_path):
            print(f"Updating {file}")
            add_imports(file_path, [exception_import, logger_import, config_import])
        else:
            print(f"File not found: {file}")

if __name__ == "__main__":
    update_files()