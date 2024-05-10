import os
import traceback

import game

base_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    game = game.Game()
    try:
        game.run()
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()
        game.quit()
    finally:
        print("finally statement closed game")
        game.quit()
