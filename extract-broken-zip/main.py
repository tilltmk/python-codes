import zipfile
import os
from tqdm import tqdm
import zlib

def extract_zip_excluding(input_zip, output_dir):
    try:
        with zipfile.ZipFile(input_zip, 'r') as zip_ref:
            members = zip_ref.namelist()
            total_members = len(members)
            
            # Initialize the progress bar
            with tqdm(total=total_members, unit='file') as progress_bar:
                for member in members:
                    if member:
                        try:
                            zip_ref.extract(member, output_dir)
                        except (zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error) as e:
                            print(f"Failed to extract {member}: {e}")
                    progress_bar.update(1)
        return True
    except FileNotFoundError:
        print(f"The file {input_zip} does not exist.")
        return False
    except zipfile.BadZipFile:
        print(f"The file {input_zip} is not a zip file.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    input_zip = input("Please enter path to zip-file")
    output_dir = input("Please enter output-path")

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    success = extract_zip_excluding(input_zip, output_dir)
    if success:
        print("Extraction completed successfully!")
    else:
        print("Extraction failed.")
