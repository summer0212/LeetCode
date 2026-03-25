json = {
  "company": {
    "name": "TechCorp",
    "location": "Silicon Valley",
    "employees": [
      {
        "id": "e001",
        "name": "Bob",
        "role": "Engineer",
        "skills": ["Python", "Java"]
      },
      {
        "id": "e002",
        "name": "Charlie",
        "role": "Designer",
        "skills": ["Figma", "Sketch"]
      }
    ],
    "departments": {
      "engineering": {
        "head": "Bob",
        "team_size": 10
      },
      "design": {
        "head": "Charlie",
        "team_size": 5
      }
    }
  }
}

# Get Company Name: 
print(json["company"]["name"])

# List All Employee Names:
all_employee_name = [employee["name"] for employee in json["company"]["employees"]]
print(all_employee_name)

# Get Bob's Skills: 


# Access Design Team Size: How many people are in the "design" department?
# Find Charlie's Role: What is Charlie's role?
# Add a Skill to Bob: If Bob just learned "JavaScript", how would you add it to his skills? (Show the updated structure or explain the steps)
# Iterate and Print All Employee IDs: