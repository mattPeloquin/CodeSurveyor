#---- Code Surveyor, Copyright 2020 Matt Peloquin, MIT License
'''
    Cobol counting
'''

import re
from .Code import Code

class customCobol( Code ):
    '''
    Cobol example of overriding the default NBNC Code class to work
    with comment syntax that is in conflict with the Surveyor defaults
    '''
    def __init__(self, options):
        super(customCobol, self).__init__(options)

    @classmethod
    def _cs_config_options(cls):
        return {}

    def _cs_init_config_options(self):
        super(customCobol, self)._cs_init_config_options()

        self.reBlankLine = re.compile(r"^\s*$")
        self.reSingleLineComments = re.compile(r"^\s*(\*|/)", self._reFlags)
        self.reMultiLineCommentsOpen = None
        self.reMultiLineCommentsClose = None


