"""Class of the pride flags."""
from ShellPride import colors


class PrideFlagBase:
    """
    Base class of the pride flag.

    Parameters
    ----------
    flag_colors: ColorsBase.
        Colors of the flag.

    colors_order: Array of string.
        Order of the colors in the flag. It must be names in the colors_codes"
        dictionary.

    length: Int.
        Length of the flag.

    """

    def __init__(self, flag_colors, colors_order, length=25):
        """Define the flag colors and parameters."""
        # Define colors.
        self.flag_colors = flag_colors

        # Define stripes.
        self.stripes = len(colors_order)
        self.colors_order = colors_order

        # Define the length of the flag.
        self.length = length

    def bkg(self, n):
        """Get background code for the n stripe."""
        if isinstance(n, int):
            return self.flag_colors.get_bkg(self.colors_order[n])
        else:
            return self.flag_colors.get_bkg(n)

    def frg(self, n):
        """Get foreground code for the n stripe."""
        if isinstance(n, int):
            return self.flag_colors.get_frg(self.colors_order[n])
        else:
            return self.flag_colors.get_frg(n)

    def center(self, messages, text_colors):
        """
        Center all the messages in the flags colors.

        Parameters
        ----------
        messages: Array of strings.
            Messages to be in the flag, it must be the same length as the
            number of stripes.

        text_colors: Array of strings.
            Colors names of the text.

        """
        max_length = max(
            [len(message) for message in messages] + [self.length]
        )

        return [
            # self.flag_colors.bold +
            self.bkg(i) +
            self.frg(text_colors[i]) +
            messages[i].center(max_length) +
            self.flag_colors.reset
            for i in range(self.stripes)
        ]


class RainbowFlag (PrideFlagBase):
    """
    Class of the rainbow pride flag (LGBTQ+).

    Parameters
    ----------
    length: Int.
        Length of the flag.

    """

    def __init__(self, length=30):
        """Define the flag colors and parameters."""
        super().__init__(
            colors.RainbowColors(),
            [
                "RED",
                "ORANGE",
                "YELLOW",
                "GREEN",
                "BLUE",
                "PURPLE"
            ],
            length=length
        )

    def center(self, messages):
        """
        Center all the messages in the flags colors.

        Parameters
        ----------
        messages: Array of strings.
            Messages to be in the flag, it must be the same length as the
            number of stripes.

        """
        return super().center(messages, ["WT", "BT", "BT", "BT", "BT", "WT"])


class ProgressFlag (PrideFlagBase):
    """
    Class of the progress pride flag (LGBTQ+).

    Parameters
    ----------
    length: Int.
        Length of the flag.

    """

    def __init__(self, length=30):
        """Define the flag colors and parameters."""
        super().__init__(
            colors.ProgressColors(),
            [
                "RED",
                "ORANGE",
                "YELLOW",
                "GREEN",
                "BLUE",
                "PURPLE"
            ],
            length=length
        )

    def center(self, messages):
        """
        Center all the messages in the flags colors.

        Parameters
        ----------
        messages: Array of strings.
            Messages to be in the flag, it must be the same length as the
            number of stripes.

        """
        return super().center(messages, ["WT", "BT", "BT", "BT", "BT", "WT"])


class GayFlagL (PrideFlagBase):
    """
    Class of the gay pride flag (NWLNW). Seven stripes.

    Parameters
    ----------
    length: Int.
        Length of the flag.

    """

    def __init__(self, length=30):
        """Define the flag colors and parameters."""
        super().__init__(
            colors.GayColors(),
            [
                "DARK_GREEN",
                "GREEN",
                "LIGHT_GREEN",
                "WHITE",
                "LIGHT_BLUE",
                "BLUE",
                "DARK_BLUE"
            ],
            length=length
        )

    def center(self, messages):
        """
        Center all the messages in the flags colors.

        Parameters
        ----------
        messages: Array of strings.
            Messages to be in the flag, it must be the same length as the
            number of stripes.

        """
        return super().center(
            messages, ["WT", "BT", "BT", "BT", "BT", "BT", "WT"]
        )


class GayFlagS (PrideFlagBase):
    """
    Class of the gay pride flag (NWLNW). five stripes.

    Parameters
    ----------
    length: Int.
        Length of the flag.

    """

    def __init__(self, length=30):
        """Define the flag colors and parameters."""
        super().__init__(
            colors.GayColors(),
            [
                "DARK_GREEN",
                "LIGHT_GREEN",
                "WHITE",
                "LIGHT_BLUE",
                "DARK_BLUE"
            ],
            length=length
        )

    def center(self, messages):
        """
        Center all the messages in the flags colors.

        Parameters
        ----------
        messages: Array of strings.
            Messages to be in the flag, it must be the same length as the
            number of stripes.

        """
        return super().center(
            messages, ["WT", "BT", "BT", "BT", "WT"]
        )


class LesbianFlagL (PrideFlagBase):
    """
    Class of the lesbian pride flag (NMLNM). Seven stripes.

    Parameters
    ----------
    length: Int.
        Length of the flag.

    """

    def __init__(self, length=30):
        """Define the flag colors and parameters."""
        super().__init__(
            colors.LesbianColors(),
            [
                "DARK_ORANGE",
                "ORANGE",
                "LIGHT_ORANGE",
                "WHITE",
                "LIGHT_PINK",
                "PINK",
                "DARK_PINK"
            ],
            length=length
        )

    def center(self, messages):
        """
        Center all the messages in the flags colors.

        Parameters
        ----------
        messages: Array of strings.
            Messages to be in the flag, it must be the same length as the
            number of stripes.

        """
        return super().center(
            messages, ["WT", "BT", "BT", "BT", "BT", "BT", "WT"]
        )


class LesbianFlagS (PrideFlagBase):
    """
    Class of the lesbian pride flag (NMLNM). five stripes.

    Parameters
    ----------
    length: Int.
        Length of the flag.

    """

    def __init__(self, length=30):
        """Define the flag colors and parameters."""
        super().__init__(
            colors.LesbianColors(),
            [
                "DARK_ORANGE",
                "LIGHT_ORANGE",
                "WHITE",
                "LIGHT_PINK",
                "DARK_PINK"
            ],
            length=length
        )

    def center(self, messages):
        """
        Center all the messages in the flags colors.

        Parameters
        ----------
        messages: Array of strings.
            Messages to be in the flag, it must be the same length as the
            number of stripes.

        """
        return super().center(
            messages, ["WT", "BT", "BT", "BT", "WT"]
        )


class BisexualFlag (PrideFlagBase):
    """
    Class of the bisexual pride flag.

    Parameters
    ----------
    length: Int.
        Length of the flag.

    """

    def __init__(self, length=30):
        """Define the flag colors and parameters."""
        super().__init__(
            colors.BisexualColors(),
            [
                "PINK",
                "PINK",
                "PURPLE",
                "BLUE",
                "BLUE"
            ],
            length=length
        )

    def center(self, messages):
        """
        Center all the messages in the flags colors.

        Parameters
        ----------
        messages: Array of strings.
            Messages to be in the flag, it must be the same length as the
            number of stripes.

        """
        return super().center(
            messages, ["BT", "BT", "BT", "WT", "WT"]
        )


class TransFlag (PrideFlagBase):
    """
    Class of the trans pride flag.

    Parameters
    ----------
    length: Int.
        Length of the flag.

    """

    def __init__(self, length=30):
        """Define the flag colors and parameters."""
        super().__init__(
            colors.TransColors(),
            [
                "BLUE",
                "PINK",
                "WHITE",
                "PINK",
                "BLUE"
            ],
            length=length
        )

    def center(self, messages):
        """
        Center all the messages in the flags colors.

        Parameters
        ----------
        messages: Array of strings.
            Messages to be in the flag, it must be the same length as the
            number of stripes.

        """
        return super().center(
            messages, ["BT", "BT", "BT", "BT", "BT"]
        )


class NonBinaryFlag (PrideFlagBase):
    """
    Class of the non-binary pride flag.

    Parameters
    ----------
    length: Int.
        Length of the flag.

    """

    def __init__(self, length=30):
        """Define the flag colors and parameters."""
        super().__init__(
            colors.NonBinaryColors(),
            [
                "YELLOW",
                "WHITE",
                "PURPLE",
                "BLACK"
            ],
            length=length
        )

    def center(self, messages):
        """
        Center all the messages in the flags colors.

        Parameters
        ----------
        messages: Array of strings.
            Messages to be in the flag, it must be the same length as the
            number of stripes.

        """
        return super().center(
            messages, ["BT", "BT", "BT", "WT"]
        )


class GenderFluidFlag (PrideFlagBase):
    """
    Class of the gender fluid pride flag.

    Parameters
    ----------
    length: Int.
        Length of the flag.

    """

    def __init__(self, length=30):
        """Define the flag colors and parameters."""
        super().__init__(
            colors.GenderFluidColors(),
            [
                "PINK",
                "WHITE",
                "PURPLE",
                "BLACK",
                "BLUE"
            ],
            length=length
        )

    def center(self, messages):
        """
        Center all the messages in the flags colors.

        Parameters
        ----------
        messages: Array of strings.
            Messages to be in the flag, it must be the same length as the
            number of stripes.

        """
        return super().center(
            messages, ["BT", "BT", "WT", "WT", "WT"]
        )


# Set the flag names.
flags_names = {
    "rainbow": RainbowFlag,
    # "progressive": ProgressiveFlag,
    "gayL": GayFlagL,
    "gay": GayFlagS,
    "lesbianL": LesbianFlagL,
    "lesbian": LesbianFlagS,
    "bisexual": BisexualFlag,
    "trans": TransFlag,
    "nonbinary": NonBinaryFlag,
    "genderfluid": GenderFluidFlag,
}
