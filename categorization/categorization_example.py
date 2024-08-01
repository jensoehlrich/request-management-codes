import json

def load_categories(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def print_categories(categories):
    for category in categories['categories']:
        print(f"ID: {category['id']}, Name: {category['name']}, Description: {category['description']}")

if __name__ == "__main__":
    categories = load_categories('categorization/categorization-template.json')
    print_categories(categories)
