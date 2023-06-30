import json

# Define safe_get function again


def safe_get(dictionary, key, default=''):
    return dictionary.get(key, default)


# Read the JSON file
file_path = 'michaellustig.jsonresume.json'
with open(file_path, 'r') as file:
    resume = json.load(file)


# Create a markdown string with error handling for missing keys
markdown = ""

# Basics
markdown += "# Resume\n\n"
markdown += "## Basics\n"
markdown += f"- Name: {safe_get(resume['basics'], 'name')}\n"
markdown += f"- Label: {safe_get(resume['basics'], 'label')}\n"
markdown += f"- Email: {safe_get(resume['basics'], 'email')}\n"
markdown += f"- Phone: {safe_get(resume['basics'], 'phone')}\n"
markdown += f"- URL: {safe_get(resume['basics'], 'url')}\n"
markdown += f"- Summary: {safe_get(resume['basics'], 'summary')}\n"
markdown += "### Location\n"
location = safe_get(resume['basics'], 'location', {})
markdown += f"- Address: {safe_get(location, 'address')}\n"
markdown += f"- Postal Code: {safe_get(location, 'postalCode')}\n"
markdown += f"- City: {safe_get(location, 'city')}\n"
markdown += f"- Country Code: {safe_get(location, 'countryCode')}\n"
markdown += f"- Region: {safe_get(location, 'region')}\n"
markdown += "### Profiles\n"
for profile in resume['basics'].get('profiles', []):
    markdown += f"- {safe_get(profile, 'network')}\nUsername: {safe_get(profile, 'username')}\nURL: {safe_get(profile, 'url')}\n"

# Work
markdown += "\n## Work Experience\n"
for work in resume.get('work', []):
    markdown += f"- Name: {safe_get(work, 'name')}, Position: {safe_get(work, 'position')}, URL: {safe_get(work, 'url')}, Start Date: {safe_get(work, 'startDate')}, End Date: {safe_get(work, 'endDate')}\n"
    markdown += f"  - Summary: {safe_get(work, 'summary')}\n"
    markdown += f"  - Highlights: {', '.join(safe_get(work, 'highlights', []))}\n"

# Volunteer
markdown += "\n## Volunteer Experience\n"
for vol in resume.get('volunteer', []):
    markdown += f"- Organization: {safe_get(vol, 'organization')}, Position: {safe_get(vol, 'position')}, URL: {safe_get(vol, 'url')}, Start Date: {safe_get(vol, 'startDate')}, End Date: {safe_get(vol, 'endDate')}\n"
    markdown += f"  - Summary: {safe_get(vol, 'summary')}\n"
    markdown += f"  - Highlights: {', '.join(safe_get(vol, 'highlights', []))}\n"

# Education
markdown += "\n## Education\n"
for edu in resume.get('education', []):
    markdown += f"- Institution: {safe_get(edu, 'institution')}, Area: {safe_get(edu, 'area')}, Study Type: {safe_get(edu, 'studyType')}, Start Date: {safe_get(edu, 'startDate')}, End Date: {safe_get(edu, 'endDate')}, Score: {safe_get(edu, 'score')}\n"
    markdown += f"  - Courses: {', '.join(safe_get(edu, 'courses', []))}\n"

# Awards

# Awards
markdown += "\n## Awards\n"
for award in resume.get('awards', []):
    markdown += f"- Title: {safe_get(award, 'title')}, Date: {safe_get(award, 'date')}, Awarder: {safe_get(award, 'awarder')}, Summary: {safe_get(award, 'summary')}\n"

# Certificates
markdown += "\n## Certificates\n"
for cert in resume.get('certificates', []):
    markdown += f"- Name: {safe_get(cert, 'name')}, Date: {safe_get(cert, 'date')}, Issuer: {safe_get(cert, 'issuer')}, URL: {safe_get(cert, 'url')}\n"

# Publications
markdown += "\n## Publications\n"
for pub in resume.get('publications', []):
    markdown += f"- Name: {safe_get(pub, 'name')}, Publisher: {safe_get(pub, 'publisher')}, Release Date: {safe_get(pub, 'releaseDate')}, URL: {safe_get(pub, 'url')}, Summary: {safe_get(pub, 'summary')}\n"

# Skills
markdown += "\n## Skills\n"
for skill in resume.get('skills', []):
    markdown += f"- Name: {safe_get(skill, 'name')}, Level: {safe_get(skill, 'level')}, Keywords: {', '.join(safe_get(skill, 'keywords', []))}\n"

# Languages
markdown += "\n## Languages\n"
for lang in resume.get('languages', []):
    markdown += f"- Language: {safe_get(lang, 'language')}, Fluency: {safe_get(lang, 'fluency')}\n"

# Interests
markdown += "\n## Interests\n"
for interest in resume.get('interests', []):
    markdown += f"- Name: {safe_get(interest, 'name')}, Keywords: {', '.join(safe_get(interest, 'keywords', []))}\n"

# References
markdown += "\n## References\n"
for ref in resume.get('references', []):
    markdown += f"- Name: {safe_get(ref, 'name')}, Reference: {safe_get(ref, 'reference')}\n"

# Projects
markdown += "\n## Projects\n"
for project in resume.get('projects', []):
    markdown += f"- Name: {safe_get(project, 'name')}, Start Date: {safe_get(project, 'startDate')}, End Date: {safe_get(project, 'endDate')}, URL: {safe_get(project, 'url')}\n"
    markdown += f"  - Summary: {safe_get(project, 'summary')}\n"
    markdown += f"  - Highlights: {', '.join(safe_get(project, 'highlights', []))}\n"

# Write markdown to file
output_file_path = 'auto.md'
with open(output_file_path, 'w') as file:
    file.write(markdown)
