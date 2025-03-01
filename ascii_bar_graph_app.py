def create_ascii_bar_graph(labels, values):
    max_len = max(len(label) for label in labels)
    max_value = max(values)
    graph = []
    header = " " * max_len + " " + " ".join(str(v) for v in range(max_value + 1))
    graph.append(header)
    for label, value in zip(labels, values):
        bar = "█" * value
        padded_label = label.ljust(max_len)
        line = f"{padded_label} {bar}"
        graph.append(line)
    return "\n".join(graph)

# Data for plotting
labels = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 10, 20]

# Create ASCII bar graph
ascii_graph = create_ascii_bar_graph(labels, values)
print(ascii_graph)
