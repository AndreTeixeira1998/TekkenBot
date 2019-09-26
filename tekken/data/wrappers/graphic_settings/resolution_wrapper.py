#!/usr/bin/env python3

# Copyright (c) 2019, Alchemy Meister
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice,this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from tekken.data.structures.graphic_settings import ResolutionStruct
from tekken.data.wrappers import StructWrapper

class ResolutionWrapper(StructWrapper):
    """
    """
    def __init__(self, block_bytes=None):
        super().__init__(ResolutionStruct, block_bytes)

    def __get_resolution(self):
        return (
            getattr(self, 'horizontal_resolution'),
            getattr(self, 'vertical_resolution')
        )

    def __set_resolution(self, resolution_tuple):
        setattr(self, 'horizontal_resolution', resolution_tuple[0])
        setattr(self, 'vertical_resolution', resolution_tuple[1])

    resolution = property(__get_resolution, __set_resolution)

    def equal_resolution(self, resolution):
        try:
            return (
                self.resolution == resolution.resolution
            )
        except AttributeError:
            return False

    def __eq__(self, resolution):
        if isinstance(resolution, ResolutionWrapper):
            return (
                getattr(self, 'horizontal_resolution')
                == resolution.horizontal_resolution
                and getattr(self, 'vertical_resolution')
                == resolution.vertical_resolution
            )
        return NotImplementedError

    def __ne__(self, resolution):
        return not self == resolution

    def __repr__(self):
        return 'resolution: ({}, {})'.format(
            getattr(self, 'horizontal_resolution'),
            getattr(self, 'vertical_resolution')
        )