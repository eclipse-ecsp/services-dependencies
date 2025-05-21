# create a python script which reads the pom.xml dependencies and update the artifacts name and its version in readme file
import xml.etree.ElementTree as ET
import re

def parse_pom_dependencies(pom_file):
    """Parse dependencies from pom.xml."""
    tree = ET.parse(pom_file)
    root = tree.getroot()
    namespaces = {'m': 'http://maven.apache.org/POM/4.0.0'}
    dependencies = []

    # Get the actual project version
    project_version = root.find("m:version", namespaces)
    project_version_text = project_version.text if project_version is not None else "N/A"

    for dependency in root.findall(".//m:dependency", namespaces):
        artifact_id = dependency.find("m:artifactId", namespaces).text
        group_id = dependency.find("m:groupId", namespaces).text
        version = dependency.find("m:version", namespaces)
        if version is not None and version.text.startswith("${") and version.text.endswith("}"):
            # Extract the property name from the placeholder
            property_name = version.text[2:-1]
            # Find the actual version in the properties section
            property_version = root.find(f"m:properties/m:{property_name}", namespaces)
            version_text = property_version.text if property_version is not None else "N/A"
        else:
            version_text = version.text if version is not None else "N/A"
        dependencies.append((f"{group_id}:{artifact_id}", version_text))

    return dependencies

def update_readme(readme_file, dependencies):
    """Update the README file with dependencies."""
    with open(readme_file, 'r') as file:
        content = file.read()

    # Find the "Built With Dependencies" section
    built_with_section = re.search(r"(## Dependencies\nThe following table lists the dependencies and their versions used in this project.\n\n)(.*?)(\n##|$)", content, re.DOTALL)
    if not built_with_section:
        print("Could not find 'Dependencies' section in README.")
        return

    # Generate the new dependencies table
    new_table = "| Library name                     |   version   |\n"
    new_table += "|----------------------------------|:-----------:|\n"
    seen = set()
    for artifact_id, version in dependencies:
        if artifact_id not in seen:
            new_table += f"| {artifact_id:<32} | {version:<10} |\n"
            seen.add(artifact_id)

    # Replace the old table with the new one
    updated_content = (
            content[:built_with_section.start(2)]
            + new_table
            + content[built_with_section.end(2):]
    )

    with open(readme_file, 'w') as file:
        file.write(updated_content)

    print("README updated successfully.")

if __name__ == "__main__":
    pom_file = "pom.xml"
    readme_file = "README.md"

    dependencies = parse_pom_dependencies(pom_file)
    update_readme(readme_file, dependencies)
