from . import panda

import argparse
def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")

    parser.add_argument("--no-rotate", help="Suppress Rotation", action="store_true")
    parser.add_argument("--scale", help="Set the scale", type=float,  default=1.0)
    parser.add_argument("--remove-panda", help="Remove the panda", action="store_true")
    parser.add_argument("--stop-walk", help="Stop walking", action="store_true")
    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()