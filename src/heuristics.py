heuristic = {
    "Bole": 7,
    "MeskelSquare": 3,
    "Medhanialem": 5,
    "Piazza": 0,
    "Lideta": 2,
    "Kazanchis": 6,
    "Gofa": 4,
    "Merkato": 2,
    "AratKilo": 3,
    "PiassaStation": 1
}

def h(node, goal="Piazza"):
    return heuristic.get(node, 0)
