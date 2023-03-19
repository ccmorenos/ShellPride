"""Colors codes for the flags."""
import re


class ColorsBase:
    """
    Base class for all the color classes for the flags.

    Parameters
    ----------
    colors_codes: Dictionary.
        Hex codes of the colors in the flag. Pairs of name of the color, hex
        code.

    """

    def __init__(self, colors_codes):
        """Define colors and convert to output."""
        # Set color hex codes.
        self.colors_codes = colors_codes

        # Foreground and background colors.
        self.frg = dict()
        self.bkg = dict()

        for color, hexcode in self.colors_codes.items():
            rgb_codes = self.hex2rgb(hexcode)

            self.frg[color] = (
                f"\033[38;2;{rgb_codes[0]};{rgb_codes[1]};{rgb_codes[2]}m"
            )
            self.bkg[color] = (
                f"\033[48;2;{rgb_codes[0]};{rgb_codes[1]};{rgb_codes[2]}m"
            )

        # Font config.
        self.bold = "\033[1m"

        self.frg["BT"] = "\033[38;2;0;0;0m"
        self.frg["WT"] = "\033[38;2;255;255;255m"

        # Reset everything.
        self.reset = "\033[0m"

    def hex2rgb(self, color):
        """
        Convert color codes from Hex to rgb.

        Parameters
        ----------
        color: Str.
            Hex code of the color.

        """
        color = re.match(r"#?([A-Z\d]{6})", color)[1]

        return [int(color[i:i + 2], 16) for i in (0, 2, 4)]

    def add_color(self, name, color_code):
        """
        Add a color to the list.

        Parameters
        ----------
        name: Str.
            Name of the color.

        color_code: Str.
            Hex code of the color.

        """
        # Add the code.
        self.colors_codes[name] = color_code

        # Get rgb code.
        rgb_codes = self.hex2rgb(color_code)

        # Add foreground and background.
        self.frg[name] = (
            f"\033[38;2;{rgb_codes[0]};{rgb_codes[1]};{rgb_codes[2]}m"
        )
        self.bkg[name] = (
            f"\033[48;2;{rgb_codes[0]};{rgb_codes[1]};{rgb_codes[2]}m"
        )

    def get_bkg(self, name):
        """Return the background code of the color."""
        return self.bkg[name]

    def get_frg(self, name):
        """Return the foreground code of the color."""
        return self.frg[name]


class RainbowColors (ColorsBase):
    """Colors of the rainbow pride flag (LGBTQ+)."""

    def __init__(self):
        """Define the colors of the rainbow pride flag."""
        super(RainbowColors, self).__init__(
            {
                "RED": "#FF0000",
                "ORANGE": "#FF8E00",
                "YELLOW": "#FFFF00",
                "GREEN": "#008E00",
                "BLUE": "#00C0C0",
                "PURPLE": "#400098"
            }
        )


class ProgressColors (RainbowColors):
    """Colors of the progress pride flag (LGBTQ+)."""

    def __init__(self):
        """Define the colors of the progress pride flag."""
        super(ProgressColors, self).__init__()
        self.add_color("PINK", "#F5A9B8")
        self.add_color("BLUE2", "#5BCEFA")
        self.add_color("WHITE", "#FFFFFF")
        self.add_color("BLACK", "#000000")
        self.add_color("BROWN", "#613915")


class GayColors (ColorsBase):
    """Colors of the gay pride flag (NWLNW)."""

    def __init__(self):
        """Define the colors of the gay pride flag."""
        super(GayColors, self).__init__(
            {
                "DARK_GREEN": "#078D70",
                "GREEN": "#26CEAA",
                "LIGHT_GREEN": "#98E8C1",
                "WHITE": "#FFFFFF",
                "LIGHT_BLUE": "#7BADE2",
                "BLUE": "#5049CC",
                "DARK_BLUE": "#3D1A78"
            }
        )


class LesbianColors (ColorsBase):
    """Colors of the lesbian pride flag (NMLNM)."""

    def __init__(self):
        """Define the colors of the lesbian flag."""
        super(LesbianColors, self).__init__(
            {
                "DARK_ORANGE": "#D52D00",
                "ORANGE": "#EF7627",
                "LIGHT_ORANGE": "#FF9A56",
                "WHITE": "#FFFFFF",
                "LIGHT_PINK": "#D162A4",
                "PINK": "#B55690",
                "DARK_PINK": "#A30262"
            }
        )


class BisexualColors (ColorsBase):
    """Colors of the bisexual pride flag."""

    def __init__(self):
        """Define the colors of the bisexual pride flag."""
        super(BisexualColors, self).__init__(
            {
                "PINK": "#D60270",
                "PURPLE": "#9B4F96",
                "BLUE": "#0038A8"
            }
        )


class TransColors (ColorsBase):
    """Colors of the trans pride flag."""

    def __init__(self):
        """Define the colors of the trans pride flag."""
        super(TransColors, self).__init__(
            {
                "PINK": "#F5A9B8",
                "BLUE": "#5BCEFA",
                "WHITE": "#FFFFFF"
            }
        )


class NonBinaryColors (ColorsBase):
    """Colors of the non-binary pride flag."""

    def __init__(self):
        """Define the colors of the non-binary pride flag."""
        super(NonBinaryColors, self).__init__(
            {
                "YELLOW": "#FCF434",
                "WHITE": "#FFFFFF",
                "PURPLE": "#9C59D1",
                "BLACK": "#2C2C2C"
            }
        )


class GenderFluidColors (ColorsBase):
    """Colors of the gender fluid pride flag."""

    def __init__(self):
        """Define the colors of the gender fluid pride flag."""
        super(GenderFluidColors, self).__init__(
            {
                "PINK": "#FF76A4",
                "WHITE": "#FFFFFF",
                "PURPLE": "#C011D7",
                "BLACK": "#2C2C2C",
                "BLUE": "#2F3CBE"
            }
        )
