#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unicodedata
import os
from optparse import OptionParser
from fontTools.ttLib import TTFont

fonts = []

def char_in_font(unicode_char, font):
    for cmap in font['cmap'].tables:
        if cmap.isUnicode():
            if ord(unicode_char) in cmap.cmap:
                return True
    return False

def test(char):
    for fontpath in fonts:
        font = TTFont(fontpath)   # specify the path to the font in question
        if char_in_font(char, font):
            print(char + " "+ unicodedata.name(char) + " in " + fontpath)

if __name__ == "__main__":
    # parse command-line options
    disc = """\
"""
    parser = OptionParser(description=disc)
    parser.add_option(
        "-c",
        "--character",
        dest="char",
        help="",
    )
    (options, args) = parser.parse_args()


    for root,dirs,files in os.walk("/usr/share/fonts"):
        for file in files:
          if file.endswith(".ttf"): fonts.append(os.path.join(root,file))

    #test(u"╿")
    test(options.char)
    #test(u"🐈")
