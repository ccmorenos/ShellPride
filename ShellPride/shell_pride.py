"""Pride Colors."""
import argparse
import sys
import re

from ShellPride.flags import flags_names
from ShellPride.messages import flags_messages
from ShellPride.colors import ColorsBase


def check_flag(name):
    """Check that the flag exists."""
    if name in flags_messages.keys():
        return name

    else:
        print(f"Error: Flag {name} not recognized.\n", file=sys.stderr)

        print("Possible flag options:\n\n", end="\t")

        i = 1
        for flag_name in flags_messages.keys():
            print(flag_name, end=" ")
            if i % 5 == 0:
                print(end="\n\t")

            i += 1

        print()
        exit(1)


# Create the parser for the console arguments.
parser = argparse.ArgumentParser(
    prog="shell_pride",
    description="Print shell decorator.",
    formatter_class=argparse.RawTextHelpFormatter
)

# Add argument for the flags that will be printed.
parser.add_argument(
    "-f",  "--flags", type=check_flag, nargs="+", required=True,
    help="List of flags to be shown"
)

# Add argument for the flags that will be printed.
parser.add_argument(
    "-L",  "--length", type=int, default=25,
    help="Length of the flags"
)

# Add argument for the decoration color.
parser.add_argument(
    "-d",  "--decorator", type=str, default="#F5A9B8",
    help="Add the color for the decorator letters"
)

# Add argument for the name.
parser.add_argument("-n",  "--name", type=str, help="Add your name")

# Add argument for the pronouns.
parser.add_argument("-p",  "--pronouns", type=str, help="Add your pronouns")

# Add argument for the zodiac sign.
parser.add_argument(
    "-zs",  "--zodiac_solar", type=str, help="Add your solar zodiac sign"
)
parser.add_argument(
    "-za",  "--zodiac_ascendant", type=str,
    help="Add your ascendant zodiac sign"
)
parser.add_argument(
    "-zm",  "--zodiac_moon", type=str, help="Add your moon zodiac sign"
)

# Parse arguments.
args = parser.parse_args()


def main():
    """Print pride flags."""
    # Create a base color.
    base_colors = ColorsBase({"decorations": args.decorator})

    # Initialize the flags.
    added_flags = [
        flags_names[
            re.search(r"([^\W_\d]+)(_var[\d+])?", name)[1]
        ](length=args.length) for name in args.flags
    ]

    # Get max length.
    max_stripes = max([
        flag.stripes
        for flag in added_flags
    ])

    # Get Stripes.
    stripes = [
        flag.center(flags_messages[name])
        for flag, name in zip(added_flags, args.flags)
    ]

    # Add decorations.
    decorations = []

    if args.name:
        decorations.append(
            f"{base_colors.bold + base_colors.get_frg('WT')}Name: "
            f"{base_colors.reset + base_colors.get_frg('decorations')}"
            f"{args.name}"
        )

    if args.pronouns:
        decorations.append(
            f"{base_colors.bold + base_colors.get_frg('WT')}Pronouns: "
            f"{base_colors.reset + base_colors.get_frg('decorations')}"
            f"{args.pronouns}"
        )

    if args.zodiac_solar:
        decorations.append(
            f"{base_colors.bold + base_colors.get_frg('WT')}Zodiac ☀: "
            f"{base_colors.reset + base_colors.get_frg('decorations')}"
            f"{args.zodiac_solar}"
        )

    if args.zodiac_ascendant:
        decorations.append(
            f"{base_colors.bold + base_colors.get_frg('WT')}Zodiac ⬆: "
            f"{base_colors.reset + base_colors.get_frg('decorations')}"
            f"{args.zodiac_ascendant}"
        )

    if args.zodiac_moon:
        decorations.append(
            f"{base_colors.bold + base_colors.get_frg('WT')}Zodiac ☾: "
            f"{base_colors.reset + base_colors.get_frg('decorations')}"
            f"{args.zodiac_moon}"
        )

    # Print the flags.
    print()
    for row in range(max_stripes):
        print(end="\t")

        for col in range(len(stripes)):
            stripe = stripes[col]

            if row < len(stripe):
                print(stripe[row], end="    ")
            else:
                print("".center(args.length), end="    ")

        if row < len(decorations):
            print(decorations[row], end="")

        print()


if __name__ == "__main__":
    main()
