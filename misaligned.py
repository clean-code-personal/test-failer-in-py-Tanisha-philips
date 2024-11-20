
def compute_color_pair_number(i, j, num_minor_colors):
    return i * num_minor_colors + j

def format_row(index, major_color, minor_color):
    return f'{index} | {major_color} | {minor_color}'

def generate_color_map(major_colors, minor_colors):
    rows = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            pair_number = compute_color_pair_number(i, j, len(minor_colors))
            rows.append(format_row(pair_number, major, minor))
    return rows

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    rows = generate_color_map(major_colors, minor_colors)
    for row in rows:
        print(row)
    return len(rows)

result = print_color_map()
assert result == 20, "Error: Expected 20 rows"
print("All is well (maybe!)\n")
