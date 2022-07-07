class Tree:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self  # Child is Tree Node and of parent
        self.children.append(child)

    def print_tree(self):
        print(self.data)
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


    