graph_neighbours = {}


def generate_graph():
    add_neighbours('0', ['4', '1'])
    add_neighbours('1', ['0', '2'])
    add_neighbours('2', ['6', '1'])
    add_neighbours('3', ['7'])
    add_neighbours('4', ['0', '5','8'])
    add_neighbours('5', ['4'])
    add_neighbours('6', ['2','10'])
    add_neighbours('7', ['3','11'])
    add_neighbours('8', ['4', '12', '9'])
    add_neighbours('9', ['8'])
    add_neighbours('10', ['6', '11'])
    add_neighbours('11', ['7'])
    add_neighbours('12', ['8','13'])
    add_neighbours('13', ['12', '14'])

    add_neighbours(14, [13, 15])
    add_neighbours(15, [14])
    
    return graph_neighbours


def add_neighbours(node, neighbours):
    new_list = []
    for val in neighbours:
        if val is not None and not val == '':
            new_list.append(str(val))
    graph_neighbours[str(node)] = new_list

