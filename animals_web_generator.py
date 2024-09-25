import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_template(file_path):
    """Loads the content of an HTML template file."""
    with open(file_path, "r") as template_file:
        return template_file.read()


def serialize_animal(animal_obj):
    """Serializes a single animal object into an HTML string with additional fields."""
    output = '<li class="cards__item">\n'
    output += '<div class="card__content">\n'

    if 'name' in animal_obj:
        output += f"<div class='card__title'>Name: {animal_obj['name']}</div>\n"

    if 'taxonomy' in animal_obj and 'scientific_name' in animal_obj['taxonomy']:
        output += f"<div class='card__text'>Scientific Name: {animal_obj['taxonomy']['scientific_name']}</div>\n"

    if 'characteristics' in animal_obj:
        characteristics = animal_obj['characteristics']

        # Processing all relevant characteristics
        if 'diet' in characteristics:
            output += f"<div class='card__text'>Diet: {characteristics['diet']}</div>\n"
        if 'lifespan' in characteristics:
            output += f"<div class='card__text'>Lifespan: {characteristics['lifespan']}</div>\n"
        if 'color' in characteristics:
            output += f"<div class='card__text'>Color: {characteristics['color']}</div>\n"
        if 'top_speed' in characteristics:
            output += f"<div class='card__text'>Top Speed: {characteristics['top_speed']}</div>\n"
        if 'weight' in characteristics:
            output += f"<div class='card__text'>Weight: {characteristics['weight']}</div>\n"
        if 'length' in characteristics:
            output += f"<div class='card__text'>Length: {characteristics['length']}</div>\n"
        if 'habitat' in characteristics:
            output += f"<div class='card__text'>Habitat: {characteristics['habitat']}</div>\n"
        if 'behavior' in characteristics:
            output += f"<div class='card__text'>Behavior: {characteristics['behavior']}</div>\n"
        if 'distinctive_feature' in characteristics:
            output += f"<div class='card__text'>Distinctive Feature: {characteristics['distinctive_feature']}</div>\n"

    if 'locations' in animal_obj and animal_obj['locations']:
        output += f"<div class='card__text'>Location: {animal_obj['locations'][0]}</div>\n"

    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        output += f"<div class='card__text'>Type: {animal_obj['characteristics']['type']}</div>\n"

    output += '</div>\n'
    output += '</li>\n'

    return output


def generate_animal_info(animals):
    """Generates a string with the HTML representation of all animals."""
    output = ''
    for animal_obj in animals:
        output += serialize_animal(animal_obj)
    return output


def create_animal_html(template_content, animal_info):
    """Replaces the placeholder in the template with actual animal information."""
    return template_content.replace("__REPLACE_ANIMALS_INFO__", animal_info)


def save_html(output_path, content):
    """Writes the content to an HTML file."""
    with open(output_path, "w") as output_file:
        output_file.write(content)


if __name__ == "__main__":
    # Load the animal data from the JSON file
    animals_data = load_data('animals_data.json')

    # Load the HTML template
    template_content = load_template('animals_template.html')

    # Generate the animal information string as HTML
    animal_info = generate_animal_info(animals_data)

    # Print the generated animal info to ensure it's correct
    print(animal_info)  # <- Überprüfe hier die Ausgabe

    # Create the final HTML content
    final_html_content = create_animal_html(template_content, animal_info)

    # Save the final HTML content to a new file
    save_html('animals.html', final_html_content)

    print("HTML file generated: animals.html")
