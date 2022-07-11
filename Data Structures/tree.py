class Tree:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self  # Child is Tree Node and of parent
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|--" if spaces else "" #if spaces is basically same this as if self.parent
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def martialTree():
     martialArtsTree = Tree("Martial Arts")

     grappling = Tree("Grappling")
     grappling.add_child(Tree("Judo"))
     grappling.add_child(Tree("Bjj"))

     striking  = Tree("Striking")
     striking.add_child(Tree("Karate"))
     striking.add_child(Tree("Boxing"))
     striking.add_child(Tree("Muay Thai"))

     kicking = Tree("Kicking")
     kicking.add_child(Tree("Taekwondo"))
     kicking.add_child(Tree("Taekkyon"))

     martialArtsTree.add_child(grappling)
     martialArtsTree.add_child(striking)
     martialArtsTree.add_child(kicking)

     martialArtsTree.print_tree()


martialTree()


    