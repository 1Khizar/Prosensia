import json
import os
def read_requirements(client_requirement_file):
    with open(client_requirement_file, 'r') as file:
        lines = file.readlines()
    
    data = {
    'Project': '',
    'Features': [],
    'Timeline': '',
    'Priority': ''
    }

    
    for line in lines:
        line = line.strip()
        
        if line.startswith('Project'):
            data['Project'] = line.replace('Project:', '').strip()
            
        elif line.startswith('Features'):
            continue
            
        elif line.startswith('-'):
            data['Features'].append(line.replace('-', '').strip())
            
        elif line.startswith('Timeline'):
            data['Timeline'] = line.replace('Timeline:', '').strip()
            
        elif line.startswith('Priority'):
            data['Priority'] = line.replace('Priority:', '').strip()
        
    return data

def summary(data):
    print("📘 Project Summary Report")
    print("-------------------------")
    print(f"Project : {data['Project']}")
    print(f"Timeline : {data['Timeline']}")
    print(f"Priority : {data['Priority']}")
    print(f"Features to Implement: ")
    
    for feature in data['Features']:
        print(f'- {feature}')

def save_to_txt(data):
    with open(r'Day_12_Task\project_summary.txt', 'w', encoding='utf-8') as file:
        file.write("📘 Project Summary Report\n")
        file.write("-------------------------\n")
        file.write(f"Project : {data['Project']}\n")
        file.write(f"Timeline : {data['Timeline']}\n")
        file.write(f"Priority : {data['Priority']}\n")
        file.write(f"Features to Implement: \n")
        
        for feature in data['Features']:
            file.write(f'- {feature}\n')
        print("\n Summary saved to \'project_summary.txt\' ")
            
def save_to_json(data):
    data_with_status = data.copy()
    data_with_status['Features'] = {feature: "Pending" for feature in data['Features']}
    
    with open(r"Day_12_Task\project_summary.json", 'w') as json_file:
        json.dump(data_with_status, json_file, indent=4)
        print("\n Summary saved to \'project_summary.json\' ")

        
def main():
    default_path = r"C:\Users\DELL\OneDrive\Desktop\Prosensia\Day_12_Task\client_requirements.txt"
    client_requirements = input(f"Enter the file of client requirements [{default_path}]: ").strip()
    if not client_requirements:
        client_requirements = default_path

    if not os.path.isfile(client_requirements):
        print(f"File not found: {client_requirements}")
        return
    data = read_requirements(client_requirements)
    summary(data)
    save_to_txt(data)
    save_to_json(data)


main()