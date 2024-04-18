from pathlib import Path

def with_base_path(relative_path = '', alternate_base = ''):
    if(alternate_base):
        return f"{alternate_base}/{relative_path}";
    else:
        return f"{str(Path(__file__).parents()[1])}/{relative_path}";