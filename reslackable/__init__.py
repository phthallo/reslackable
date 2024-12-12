import argparse

from reslackable.classes import reMarkable
from reslackable.views.Channels import ChannelView


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

    parser.add_argument(
        "--rm2fb",
        "-r",
        help="Flag if the program is being run on a reMarkable 2.",
        action="store_false",
        default=True
    )
    args = parser.parse_args()

    rm = reMarkable(simple=args.simple, rm2fb=args.rm2fb) if args.simple is not None else reMarkable(rm2fb=args.rm2fb)

    rm.eclear()
    
    rm.update_view(ChannelView(rm))
    print("Updated base view")
    while True:
        clicked = rm.display()
        if quit_hook(clicked) == "exit":
            break
        
        rm.view.handle_buttons(clicked) # type: ignore

