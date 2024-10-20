import os

# Define the directory path
directory = "real_time_models/cucumber_yolov11/datasets/cucumber_classes/valid/labels"
count=0
# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.startswith("Downy-Mildew") and filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        
        # Read the content of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Modify the content
        modified_lines = []
        for line in lines:
            parts = line.split()
            if parts:
                parts[0] = "3"
                modified_lines.append(" ".join(parts) + "\n")
        
        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)
        
        count+=1

print("number of modified files",count)
print("Conversion completed.")