#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file contains API calls for all Plecost functions
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

from plecost.reporters import *  # noqa
from plecost.data import PlecostOptions
from plecost.versions import find_versions  # noqa


#--------------------------------------------------------------------------
#
# Command line options
#
#--------------------------------------------------------------------------
def run(config):
    """
    Main function of plecost:
    - Find WordPress versions
    - Find outdated plugins

    :param config: PlecostOptions option instance
    :type config: `PlecostOptions`

    :raises: PlecostTargetNotAvailable, PlecostNotWordPressFound, PlecostWordListNotFound
    """
    # Check reporter
    if config.report_filename is not None:
        # Select appropriate report.
        reporter_function = get_reporter(config.report_filename)

    # Looking for redirects

    # Find versions
    data = find_versions(config)

    # Generate reports
    if config.report_filename is not None:
        # Generate report
        report = reporter_function(config.report_filename)
        report.generate(data)


__all__ = ["run"]