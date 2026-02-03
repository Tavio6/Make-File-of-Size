import os

def create_file(filename: str, size_in_bytes: int):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    
    with open(file_path, 'wb') as f:
        f.write(b' ' * size_in_bytes)
    
    print(f"File created: {file_path} ({size_in_bytes} bytes)")

if __name__ == "__main__":
    output_name = "output.txt"
    size_bytes = 64327680 #64 mega bytes btw

    create_file(output_name, size_bytes)
