# MISSION: Create a Graphical User Interfave 'ore MightyMaxims.
# STATUS: Public
# VERSION: 1.0.0
# NOTES: https://github.com/TotalPythoneering and https://www.youtube.com/@TotalPythoneering
# DATE: 2026-07-03 00:57:07
# FILE: __main__.py
# AUTHOR: Randall Nagy + Google A.I.
#

from . import TkMaxims

if __name__ == '__main__':
    try:
        TkMaxims.main()
    except:
        import MightyMaxims
        MightyMaxims.GetQuote()

