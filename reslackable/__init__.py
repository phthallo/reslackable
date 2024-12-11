import argparse

from reslackable.classes import reMarkable
from reslackable.views.MessageView import MessageView


def quit_hook(clicked):
    
    if clicked and clicked[0] == "exit":
            return "exit"



def main():
    parser = argparse.ArgumentParser(
        prog="reslackable",
        description="Example carta application",
    )
    parser.add_argument(
        "--simple-executable",
        help="Path to the simple application",
        action="store",
        default=None,
        dest="simple",
    )
    args = parser.parse_args()

    rm = reMarkable(simple=args.simple) if args.simple is not None else reMarkable()

    rm.eclear()
    
    rm.update_view(MessageView(rm))
    print("Updated base view")
    while True:
        clicked = rm.display()
        if quit_hook(clicked) == "exit":
            break
        
        rm.view.handle_buttons(clicked) # type: ignore

