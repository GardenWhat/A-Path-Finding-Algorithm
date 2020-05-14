# rect = [(2,1), (2,6), (17,1), (17,6)]
# pentagon = [(1,9), (0,14), (6,19), (9,15), (7,8)]
# tri1 = [(12,15), (10,8), (14,8)]
# rhombus = [(14,19), (18,20), (14,13), (20,17)]
# tri2 = [(18,10), (19,3), (23,6)]
# rect2 = [(22,19), (28,19), (22,9), (28,9)]
# poly = [(29,17), (31,19), (34,16), (32,8)]
# hexagon = [(29,8), (31,6), (31,2), (28,1), (25,2), (25,6)]
# start = (1,3)
# goal = (34,19)

import pygame

pygame.init()


class Node:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.parent = None
        self.H = 0
        self.G = 0
        self.children = []

    def cost(self):
        if self.parent:
            return abs(self.x - self.parent.x) + abs(self.y - self.parent.y)
        else:
            return 0


# start
S = Node(1, 3, "S")

# goal
G = Node(34, 19, "G")

# rect = [(2,1), (2,6), (17,1), (17,6)]
A1 = Node(2, 1, "A1")
A2 = Node(2, 6, "A2")
A3 = Node(17, 6, "A3")
A4 = Node(17, 1, "A4")

# pentagon = [(1,9), (0,14), (6,19), (9,15), (7,8)]
B1 = Node(1, 9, "B1")
B2 = Node(0, 14, "B2")
B3 = Node(6, 19, "B3")
B4 = Node(9, 15, "B4")
B5 = Node(7, 8, "B5")

# tri1 = [(12,15), (10,8), (14,8)]
C1 = Node(12, 15, "C1")
C2 = Node(10, 8, "C2")
C3 = Node(14, 8, "C3")

# rhombus = [(14,19), (18,20), (14,13), (20,17)]
D1 = Node(14, 19, "D1")
D2 = Node(18, 20, "D2")
D3 = Node(20, 17, "D3")
D4 = Node(14, 13, "D4")

# tri2 = [(18,10), (19,3), (23,6)]
E1 = Node(18, 10, "E1")
E2 = Node(19, 3, "E2")
E3 = Node(23, 6, "E3")

# rect2 = [(22,19), (28,19), (22,9), (28,9)]
F1 = Node(22, 19, "F1")
F2 = Node(28, 19, "F2")
F3 = Node(28, 9, "F3")
F4 = Node(22, 9, "F4")

# poly = [(29,17), (31,19), (34,16), (32,8)]
G1 = Node(29, 17, "G1")
G2 = Node(31, 19, "G2")
G3 = Node(34, 16, "G3")
G4 = Node(32, 8, "G4")

# hexagon = [(29,8), (31,6), (31,2), (28,1), (25,2), (25,6)]
H1 = Node(29, 8, "H1")
H2 = Node(31, 6, "H2")
H3 = Node(31, 2, "H3")
H4 = Node(28, 1, "H4")
H5 = Node(25, 2, "H5")
H6 = Node(25, 6, "H6")

graph = {
    S.name: [A1.name, A2.name, B1.name, B2.name],
    A1.name: [S.name, A3.name, A2.name],
    A2.name: [S.name, A1.name, A3.name, B1.name, B5.name, C2.name, C3.name],
    A3.name: [A2.name, A4.name, C2.name, C3.name, D4.name, E1.name, E2.name],
    A4.name: [A1.name, A3.name, E1.name, E2.name, F3.name, H4.name, H5.name, H6.name],
    B1.name: [S.name, A2.name, B2.name, B5.name],
    B2.name: [S.name, B1.name, B3.name],
    B3.name: [B2.name, B4.name, C1.name, D1.name],
    B4.name: [B3.name, B5.name, C1.name, C2.name, D1.name],
    B5.name: [B1.name, B4.name, A2.name, C1.name, C2.name],
    C1.name: [B3.name, B4.name, B5.name, C2.name, C3.name, D1.name, D4.name],
    C2.name: [A2.name, A4.name, B4.name, B4.name, B5.name, C1.name, C3.name],
    C3.name: [A2.name, A4.name, C1.name, C2.name, D3.name, D4.name, E1.name],
    D1.name: [B3.name, B4.name, C1.name, D2.name, D4.name],
    D2.name: [D1.name, D3.name, F1.name],
    D3.name: [D2.name, D4.name, C3.name, E1.name, F1.name, F4.name],
    D4.name: [A4.name, C1.name, C3.name, E1.name, E2.name, F4.name, D3.name, D1.name],
    E1.name: [A4.name, C3.name, D4.name, D3.name, F4.name, E2.name, E3.name],
    E2.name: [A3.name, A4.name, D4.name, E1.name, E3.name, H4.name, H5.name, H6.name],
    E3.name: [E1.name, E2.name, F4.name, F3.name, H1.name, H5.name, H6.name],
    F1.name: [D2.name, D3.name, F2.name, F4.name],
    F2.name: [F1.name, F3.name, G1.name, G2.name],
    F3.name: [E3.name, F2.name, F4.name, G1.name, G4.name, H1.name, H6.name],
    F4.name: [D3.name, D4.name, E1.name, E3.name, F1.name, F3.name, H1.name, H6.name],
    G1.name: [F2.name, F3.name, G2.name, G4.name, H1.name, H2.name],
    G2.name: [F2.name, G1.name, G3.name, G.name],
    G3.name: [G2.name, G4.name, G.name],
    G4.name: [F3.name, G1.name, G3.name, H1.name, H2.name, H3.name],
    H1.name: [E3.name, F3.name, F4.name, G1.name, G4.name, H2.name, H6.name],
    H2.name: [F2.name, G1.name, G4.name, H1.name, H3.name],
    H3.name: [H2.name, H4.name],
    H4.name: [A3.name, E3.name, H3.name, H5.name],
    H5.name: [A3.name, E2.name, E3.name, H4.name, H6.name],
    H6.name: [A3.name, E2.name, E3.name, F4.name, F3.name, H1.name, H5.name]
}

S.children = [A1, A2, B1, B2]
A1.children = [S, A3, A2]
A2.children = [S, A1, A3, B1, B5, C2, C3]
A3.children = [A2, A4, C2, C3, D4, E1, E2]
A4.children = [A1, A3, E1, E2, F3, H4, H5, H6]
B1.children = [S, A2, B2, B5]
B2.children = [S, B1, B3]
B3.children = [B2, B4, C1, D1]
B4.children = [B3, B5, C1, C2, D1]
B5.children = [B1, B4, A2, C1, C2]
C1.children = [B3, B4, B5, C2, C3, D1, D4]
C2.children = [A2, A4, B4, B4, B5, C1, C3]
C3.children = [A2, A4, C1, C2, D3, D4, E1]
D1.children = [B3, B4, C1, D2, D4]
D2.children = [D1, D3, F1]
D3.children = [D2, D4, C3, E1, F1, F4]
D4.children = [A4, C1, C3, E1, E2, F4, D3, D1]
E1.children = [A4, C3, D4, D3, F4, E2, E3]
E2.children = [A3, A4, D4, E1, E3, H4, H5, H6]
E3.children = [E1, E2, F4, F3, H1, H5, H6]
F1.children = [D2, D3, F2, F4]
F2.children = [F1, F3, G1, G2]
F3.children = [E3, F2, F4, G1, G4, H1, H6]
F4.children = [D3, D4, E1, E3, F1, F3, H1, H6]
G1.children = [F2, F3, G2, G4, H1, H2]
G2.children = [F2, G1, G3, G]
G3.children = [G2, G4, G]
G4.children = [F3, G1, G3, H1, H2, H3]
H1.children = [E3, F3, F4, G1, G4, H2, H6]
H2.children = [F2, G1, G4, H1, H3]
H3.children = [H2, H4]
H4.children = [A3, E3, H3, H5]
H5.children = [A3, E2, E3, H4, H6]
H6.children = [A3, E2, E3, F4, F3, H1, H5]


def ED(current, goal):
    return abs(current.x - goal.x) + abs(current.y - goal.y)


def aStar(start, goal, grid):
    openList = set()
    closedList = set()
    current = start

    openList.add(current)
    while openList:
        current = min(openList, key=lambda o: o.G + o.H)

        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]

        openList.remove(current)

        closedList.add(current)

        for node in current.children:
            if node in closedList:
                continue
            if node in openList:
                new_g = current.G + current.cost()
                if node.G > new_g:
                    node.G = new_g
                    node.parent = current
            else:
                node.G = current.G + current.cost()
                node.H = ED(current, goal)
                node.parent = current
                openList.add(node)
    print("No path found to goal")


path = aStar(S, G, graph)

GRID_SIZE = 30
GRID_X = 35
GRID_Y = 20
screen = pygame.display.set_mode((GRID_X * GRID_SIZE, GRID_Y * GRID_SIZE))
pygame.display.set_caption('A* Algorithm')
WHITE = (255, 255, 255)
screen.fill(WHITE)
# START POINT
start = pygame.draw.circle(screen, (0, 255, 0), (S.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - S.y * GRID_Y), 7)

# RECTANGLE1
pygame.draw.line(screen, 0, (A1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A1.y * GRID_Y),
                 (A2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A2.y * GRID_Y))
pygame.draw.line(screen, 0, (A2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A2.y * GRID_Y),
                 (A3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A3.y * GRID_Y))
pygame.draw.line(screen, 0, (A3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A3.y * GRID_Y),
                 (A4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A4.y * GRID_Y))
pygame.draw.line(screen, 0, (A4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A4.y * GRID_Y),
                 (A1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A1.y * GRID_Y))

# PENTAGON
pygame.draw.line(screen, 0, (B1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B1.y * GRID_Y),
                 (B2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B2.y * GRID_Y))
pygame.draw.line(screen, 0, (B2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B2.y * GRID_Y),
                 (B3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B3.y * GRID_Y))
pygame.draw.line(screen, 0, (B3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B3.y * GRID_Y),
                 (B4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B4.y * GRID_Y))
pygame.draw.line(screen, 0, (B4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B4.y * GRID_Y),
                 (B5.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B5.y * GRID_Y))
pygame.draw.line(screen, 0, (B5.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B5.y * GRID_Y),
                 (B1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B1.y * GRID_Y))

# TRI1
pygame.draw.line(screen, 0, (C1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - C1.y * GRID_Y),
                 (C2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - C2.y * GRID_Y))
pygame.draw.line(screen, 0, (C2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - C2.y * GRID_Y),
                 (C3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - C3.y * GRID_Y))
pygame.draw.line(screen, 0, (C3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - C3.y * GRID_Y),
                 (C1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - C1.y * GRID_Y))

# RHOMBUS
pygame.draw.line(screen, 0, (D1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D1.y * GRID_Y),
                 (D2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D2.y * GRID_Y))
pygame.draw.line(screen, 0, (D2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D2.y * GRID_Y),
                 (D3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D3.y * GRID_Y))
pygame.draw.line(screen, 0, (D3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D3.y * GRID_Y),
                 (D4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D4.y * GRID_Y))
pygame.draw.line(screen, 0, (D4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D4.y * GRID_Y),
                 (D1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D1.y * GRID_Y))

# TRI1
pygame.draw.line(screen, 0, (E1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - E1.y * GRID_Y),
                 (E2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - E2.y * GRID_Y))
pygame.draw.line(screen, 0, (E2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - E2.y * GRID_Y),
                 (E3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - E3.y * GRID_Y))
pygame.draw.line(screen, 0, (E3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - E3.y * GRID_Y),
                 (E1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - E1.y * GRID_Y))

# RECTANGLE2
pygame.draw.line(screen, 0, (F1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F1.y * GRID_Y),
                 (F2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F2.y * GRID_Y))
pygame.draw.line(screen, 0, (F2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F2.y * GRID_Y),
                 (F3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F3.y * GRID_Y))
pygame.draw.line(screen, 0, (F3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F3.y * GRID_Y),
                 (F4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F4.y * GRID_Y))
pygame.draw.line(screen, 0, (F4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F4.y * GRID_Y),
                 (F1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F1.y * GRID_Y))

# POLYGON
pygame.draw.line(screen, 0, (G1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G1.y * GRID_Y),
                 (G2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G2.y * GRID_Y))
pygame.draw.line(screen, 0, (G2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G2.y * GRID_Y),
                 (G3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G3.y * GRID_Y))
pygame.draw.line(screen, 0, (G3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G3.y * GRID_Y),
                 (G4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G4.y * GRID_Y))
pygame.draw.line(screen, 0, (G4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G4.y * GRID_Y),
                 (G1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G1.y * GRID_Y))

# HEXAGON
pygame.draw.line(screen, 0, (H1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H1.y * GRID_Y),
                 (H2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H2.y * GRID_Y))
pygame.draw.line(screen, 0, (H2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H2.y * GRID_Y),
                 (H3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H3.y * GRID_Y))
pygame.draw.line(screen, 0, (H3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H3.y * GRID_Y),
                 (H4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H4.y * GRID_Y))
pygame.draw.line(screen, 0, (H4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H4.y * GRID_Y),
                 (H5.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H5.y * GRID_Y))
pygame.draw.line(screen, 0, (H5.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H5.y * GRID_Y),
                 (H6.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H6.y * GRID_Y))
pygame.draw.line(screen, 0, (H6.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H6.y * GRID_Y),
                 (H1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H1.y * GRID_Y))

# GOAL POINT
goal = pygame.draw.circle(screen, (255, 0, 0), (G.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G.y * GRID_Y), 7)

t = len(path)
for p in path:
    if not p == S:
        pygame.draw.line(screen, (255, 0, 0), (p.parent.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - p.parent.y * GRID_Y),
                         (p.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - p.y * GRID_Y))


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()