#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
This file contains Plecost exceptions
"""


__license__ = """
Copyright (c) 2014:

    Francisco Jesus Gomez aka ffranz | @ffranz - ffranz-[at]-iniqua.com
    Daniel Garcia aka cr0hn | @ggdaniel - cr0hn-[at]-cr0hn.com

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted
provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions
and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions
and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or
promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.
"""


#--------------------------------------------------------------------------
class PlecostWordListNotFound(Exception):
    """Word list not found"""


#--------------------------------------------------------------------------
class PlecostTargetNotAvailable(Exception):
    """Impossible to connect to the target"""


#--------------------------------------------------------------------------
class PlecostNotWordPressFound(Exception):
    """Exception when not a valid WordPress installation found"""


#--------------------------------------------------------------------------
class PlecostInvalidReportFormat(Exception):
    """Requested report file formant is not available."""
