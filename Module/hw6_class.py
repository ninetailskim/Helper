# -*- coding: utf-8 -*-
from human import *


def main():
    x = American('Obama')
    # should be `Obama says Hello`
    x.sai_hi()

    x = French('Napoléon')
    # should be `Napoléon says Bonjour`
    x.sai_hi()

    x = Spanish('Picasso')
    # should be `Picasso says Hola`
    x.sai_hi()

    x = Janpanese('Aragaki Yui')
    # should be `Aragaki Yui says Konnichiwa`
    x.sai_hi()

    x = Korean('Yoona')
    # should be `Yoona says Yeoboseyo`
    x.sai_hi()

    x = Indian('Gandhi‎')
    # should be `Gandhi‎ says Namaste`
    x.sai_hi()


if __name__ == '__main__':
    main()
