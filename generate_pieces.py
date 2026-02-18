import os

ASSETS_DIR = "assets/pieces"
os.makedirs(ASSETS_DIR, exist_ok=True)

# Standard piece paths (Cburnett style simplified)
PAWN_PATH = 'd="m 22.5,9 c -2.21,0 -4,1.79 -4,4 0,0.89 0.29,1.71 0.78,2.38 C 17.33,16.5 16,18.59 16,21 c 0,2.03 0.94,3.84 2.41,5.03 C 15.41,27.09 11,31.58 11,39.5 H 34 C 34,31.58 29.59,27.09 26.59,26.03 28.06,24.84 29,23.03 29,21 29,18.59 27.67,16.5 25.72,15.38 26.21,14.71 26.5,13.89 26.5,13 c 0,-2.21 -1.79,-4 -4,-4 z"'
ROOK_PATH = 'd="M 9,39 L 36,39 L 36,36 L 9,36 L 9,39 z M 12,36 L 12,32 L 33,32 L 33,36 L 12,36 z M 11,14 L 11,9 L 15,9 L 15,11 L 20,11 L 20,9 L 25,9 L 25,11 L 30,11 L 30,9 L 34,9 L 34,14 M 34,14 L 31,17 L 14,17 L 11,14 M 31,17 L 31,29.5 L 14,29.5 L 14,17 M 31,29.5 L 32.5,32 L 12.5,32 L 14,29.5 M 11,14 L 34,14"'
KNIGHT_PATH = 'd="M 22,10 C 32.5,11 38.5,18 38,39 L 15,39 C 15,30 25,32.5 23,18 M 24,18 C 24.38,20.91 18.45,25.37 16,27 C 13,29 13.18,31.34 11,31 C 9.958,30.06 12.41,27.96 11,28 C 10,28 11.19,29.23 10,30 C 9,30 5.997,31 6,26 C 6,24 12,14 12,14 C 12,14 13.89,12.1 14,10.5 C 13.27,9.506 13.5,8.5 13.5,7.5 C 14.5,6.5 16.5,10 16.5,10 L 18.5,10 C 18.5,10 19.28,8.008 21,7 C 22,7 22,10 22,10 M 9.5 25.5 A 0.5 0.5 0 1 1 8.5,25.5 A 0.5 0.5 0 1 1 9.5 25.5 z M 15 15.5 A 0.5 1.5 0 1 1 14,15.5 A 0.5 1.5 0 1 1 15 15.5 z"'
BISHOP_PATH = 'd="M 9,36 C 12.39,35.03 19.11,36.43 22.5,34 C 25.89,36.43 32.61,35.03 36,36 C 36,36 37.65,36.54 39,38 C 38.32,38.97 37.35,38.99 36,38.5 C 32.61,37.53 25.89,38.96 22.5,37.5 C 19.11,38.96 12.39,37.53 9,38.5 C 7.65,38.99 6.68,38.97 6,38 C 7.35,36.54 9,36 9,36 z M 15,32 C 17.5,34.5 27.5,34.5 30,32 C 30.5,30.5 30,30 30,30 C 30,27.5 27.5,26 27.5,26 C 33,24.5 33.5,14.5 22.5,10.5 C 11.5,14.5 12,24.5 17.5,26 C 17.5,26 15,27.5 15,30 C 15,30 14.5,30.5 15,32 z M 25 8 A 2.5 2.5 0 1 1 20,8 A 2.5 2.5 0 1 1 25 8 z"'
QUEEN_PATH = 'd="M 9,26 C 17.5,24.5 30,24.5 36,26 L 38.5,13.5 L 31,25 L 30.7,10.9 L 25.5,24.5 L 22.5,10 L 19.5,24.5 L 14.3,10.9 L 14,25 L 6.5,13.5 L 9,26 z M 9,26 C 9,28 10.5,28 11.5,30 C 12.5,31.5 12.5,31 12,33.5 C 10.5,34.5 11,36 11,36 C 9.5,37.5 11,38.5 11,38.5 C 17.5,39.5 27.5,39.5 34,38.5 C 34,38.5 35.5,37.5 34,36 C 34,36 34.5,34.5 33,33.5 C 32.5,31 32.5,31.5 33.5,30 C 34.5,28 36,28 36,26 C 27.5,24.5 17.5,24.5 9,26 z M 11.5,30 C 15,29 30,29 33.5,30 M 12,33.5 C 18,32.5 27,32.5 33,33.5"'
KING_PATH = 'd="M 22.5 11.63 V 6 M 20 8 h 5 M 22.5 25 s 4.5 -7.5 3 -10.5 c 0 0 -1 -2.5 -3 -2.5 s -3 2.5 -3 2.5 c -1.5 3 3 10.5 3 10.5 M 12.5 37 c 5.5 3.5 14.5 3.5 20 0 v -7 s 9 -4.5 6 -10.5 c -4 -6.5 -13.5 -3.5 -16 4 V 27 v -3.5 c -2.5 -7.5 -12 -10.5 -16 -4 -3 6 6 10.5 6 10.5 v 7 M 12.5 30 c 5.5 -3 14.5 -3 20 0 m -20 3.5 c 5.5 -3 14.5 -3 20 0 m -20 3.5 c 5.5 -3 14.5 -3 20 0"'

def create_svg(filename, content, width=45, height=45):
    with open(os.path.join(ASSETS_DIR, filename), 'w') as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n')
        f.write(content)
        f.write('</svg>')

def get_style(color):
    fill = "#ffffff" if color == "white" else "#000000"
    stroke = "#000000" if color == "white" else "#ffffff" # Using white stroke for black pieces for visibility
    # Standard black pieces usually have black fill and black stroke but on white background.
    # On a board, black pieces need to be visible on dark squares.
    # Often black pieces have a white outline or just black fill.
    # Let's stick to black fill and thin white stroke for black pieces to make them pop on dark squares.
    # Or standard Cburnett uses black fill and black stroke but relies on the board color being lighter than black.
    # But dark squares are #b58863 (brown). Black is visible.
    stroke = "#000000"
    if color == "black":
        stroke = "#ffffff" # Adding white stroke for black pieces for better visibility on dark squares
        stroke_width = "1.5"
    else:
        stroke_width = "1.5"

    return f'style="fill:{fill};stroke:{stroke};stroke-width:{stroke_width};stroke-linejoin:round;stroke-linecap:round;"'

def generate_standard_pieces():
    pieces = {
        'pawn': PAWN_PATH,
        'rook': ROOK_PATH,
        'knight': KNIGHT_PATH,
        'bishop': BISHOP_PATH,
        'queen': QUEEN_PATH,
        'king': KING_PATH
    }

    for color in ['white', 'black']:
        for piece, path in pieces.items():
            content = f'<path {path} {get_style(color)} />'
            if piece == 'queen': # Add circles for queen crown
                content += f'<circle cx="6" cy="12" r="2" fill="{("#ffffff" if color=="white" else "#000000")}" stroke="{("#000000" if color=="white" else "#ffffff")}" stroke-width="1"/>'
                content += f'<circle cx="14" cy="9" r="2" fill="{("#ffffff" if color=="white" else "#000000")}" stroke="{("#000000" if color=="white" else "#ffffff")}" stroke-width="1"/>'
                content += f'<circle cx="22.5" cy="8" r="2" fill="{("#ffffff" if color=="white" else "#000000")}" stroke="{("#000000" if color=="white" else "#ffffff")}" stroke-width="1"/>'
                content += f'<circle cx="31" cy="9" r="2" fill="{("#ffffff" if color=="white" else "#000000")}" stroke="{("#000000" if color=="white" else "#ffffff")}" stroke-width="1"/>'
                content += f'<circle cx="39" cy="12" r="2" fill="{("#ffffff" if color=="white" else "#000000")}" stroke="{("#000000" if color=="white" else "#ffffff")}" stroke-width="1"/>'

            create_svg(f'{color}_{piece}.svg', content)

def generate_custom_pieces():
    for color in ['white', 'black']:
        style = get_style(color)
        fill_color = "#ffffff" if color == "white" else "#000000"
        stroke_color = "#000000" if color == "white" else "#ffffff"

        # Guardian: Pawn + Knight elements + Sword/Shield
        guardian_content = f'<g transform="translate(0,0)">'
        # Pawn body
        guardian_content += f'<path {PAWN_PATH} {style} />'
        # Sword
        guardian_content += f'<path d="M 38 15 L 35 25 L 37 25 L 36 28 L 39 28 L 38 25 L 40 25 Z" {style} />' # Rough sword shape
        # Shield
        guardian_content += f'<path d="M 8 18 Q 12 15 16 18 L 16 22 Q 12 25 8 22 Z" {style} />'
        guardian_content += '</g>'
        create_svg(f'{color}_guardian.svg', guardian_content)

        # Cannon: Wheels + Barrel
        cannon_content = f'<g transform="translate(0,0)">'
        # Wheels
        cannon_content += f'<circle cx="15" cy="35" r="5" {style} />'
        cannon_content += f'<circle cx="30" cy="35" r="5" {style} />'
        # Barrel
        cannon_content += f'<path d="M 10 35 L 35 20 L 38 25 L 13 40 Z" {style} />'
        cannon_content += '</g>'
        create_svg(f'{color}_cannon.svg', cannon_content)

        # Wall: Rook + Ladder
        wall_content = f'<g transform="translate(0,0)">'
        # Rook body
        wall_content += f'<path {ROOK_PATH} {style} />'
        # Ladder overlay
        ladder_style = f'style="fill:none;stroke:{stroke_color};stroke-width:2;stroke-linecap:round;"'
        wall_content += f'<path d="M 18 18 V 35" {ladder_style} />'
        wall_content += f'<path d="M 27 18 V 35" {ladder_style} />'
        wall_content += f'<path d="M 18 22 H 27" {ladder_style} />'
        wall_content += f'<path d="M 18 26 H 27" {ladder_style} />'
        wall_content += f'<path d="M 18 30 H 27" {ladder_style} />'
        wall_content += '</g>'
        create_svg(f'{color}_wall.svg', wall_content)

        # Archer: Pawn + Bow
        archer_content = f'<g transform="translate(0,0)">'
        # Pawn body
        archer_content += f'<path {PAWN_PATH} {style} />'
        # Bow
        bow_style = f'style="fill:none;stroke:{stroke_color};stroke-width:2;stroke-linecap:round;"'
        archer_content += f'<path d="M 30 15 Q 40 22 30 29" {bow_style} />'
        archer_content += f'<path d="M 30 15 L 30 29" style="fill:none;stroke:{stroke_color};stroke-width:0.5;" />' # String
        archer_content += '</g>'
        create_svg(f'{color}_archer.svg', archer_content)

if __name__ == "__main__":
    generate_standard_pieces()
    generate_custom_pieces()
    print("All pieces generated.")
