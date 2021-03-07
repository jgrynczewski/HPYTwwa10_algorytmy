class Node:
    def __init__(self, value, link=None):
        self.value = value
        self.link = link

    def __str__(self):
        return f"{self.value}"
        # return f"{self.value} -> {self.link}"

    def get_link_node(self):
        return self.link

    def set_link_node(self, next_node):
        self.link = next_node

    def get_value(self):
        return self.value


if __name__ == "__main__":
    n1 = Node(33)
    n2 = Node(12, n1)

    print(n2.get_value())
    print(n2.get_link_node())