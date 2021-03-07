from node import Node
# Dla chętnych insert, lookup (przeszukiwanie listy), sortowanie
# Lista dwukierunkowa (Node będzie z dwoma linkami)


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def prepend(self, new_value):
        new_node = Node(value=new_value)
        new_node.set_link_node(self.head_node)
        self.head_node = new_node

    def remove(self, value_to_remove):
        current_node = self.head_node

        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_link_node()
        else:
            while current_node:
                next_node = current_node.get_link_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_link_node(next_node.get_link_node())
                    current_node = None
                else:
                    current_node = next_node

    def stringify_list(self):
        stringified_list = ""
        current_node = self.get_head_node()

        while current_node:
            stringified_list += str(current_node)
            if not current_node.get_link_node() is None:
                stringified_list += " -> "
            current_node = current_node.get_link_node()

        return stringified_list


if __name__ == "__main__":
    l = LinkedList(12)
    l.prepend(14)
    l.prepend(23)
    l.prepend(30)
    print(l.stringify_list())
