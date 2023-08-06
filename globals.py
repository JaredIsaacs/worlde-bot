WORD_WIDTH = 100
WORD_HEIGHT = 100

BOARD_GAP = 10
BOARD_WIDTH = (WORD_WIDTH * 5) + (BOARD_GAP * 6)
BOARD_HEIGHT = (WORD_HEIGHT * 6) + (BOARD_GAP * 7)

FONT_SIZE = 65

INCORRECT_CHAR = '#787c7f'
MISPLACED_CHAR = '#c8b653'
CORRECT_CHAR = '#6ca965'

WORDLE_COLORS = {
    0 : INCORRECT_CHAR,
    1 : MISPLACED_CHAR,
    2 : CORRECT_CHAR
}

WORDLE_URL = 'https://wordle-api.vercel.app/api/wordle'

BOARD = None