import os
import sys
import csv
from datetime import datetime


def generate_csv(folder_path):
    
    if not os.path.exists(folder_path):
        print("Error: The specified folder does not exist.")
        return

    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_filename = os.path.join(folder_path, f"file_details_{timestamp}.csv")

    
    headers = [
        "Filename", "File Path", "File Size (MB)", "File Extension",
        "Date Created"
    ]

   
    try:
        with open(csv_filename, mode='w', newline='',
                  encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(headers)  # Write headers

           
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        # Gather file details
                        file_size = os.path.getsize(file_path) / (
                            1024 * 1024)  # Convert bytes to MB
                        file_extension = os.path.splitext(file)[1]
                        date_created = datetime.fromtimestamp(
                            os.path.getctime(file_path)).strftime(
                                '%Y-%m-%d %H:%M:%S')

                        # Write file details to the CSV
                        csv_writer.writerow([
                            file, file_path, f"{file_size:.2f}",
                            file_extension, date_created
                        ])
                    except Exception as e:
                        print(
                            f"Error processing file: {file_path}. Error: {e}")
        print(f"CSV file created: {csv_filename}")
    except Exception as e:
        print(f"Error creating CSV file: {e}")


if __name__ == "__main__":
   
    folder_path = "./"
    generate_csv(folder_path)