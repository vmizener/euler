from ..p0018.main import main as main18

def main():
    with open('triangle.txt', 'r') as fh:
        triangle = ''.join(fh.readlines()).strip()
    return main18(triangle)
