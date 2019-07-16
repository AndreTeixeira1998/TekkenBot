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

"""
"""
import math
import tkinter as tk
from gui.my_tkinter import Textbox

class AttackTextbox(Textbox):
    """
    """
    def __init__(self, master, max_lines, **kwargs):
        super().__init__(master=master, **kwargs)
        self.max_lines = max_lines

        self.configure(height=self.max_lines, state='disable')
        self.bind('<MouseWheel>', AttackTextbox.__disable_mouse_wheel)

        self.font = ['Consolas', 11]
        self.configure(font=tuple(self.font))

    def is_clear(self, include_header=False):
        line_count = int(self.index('end-1c').split('.')[0])
        if include_header:
            return line_count == 0
        return line_count <= 1

    def clear(self, clear_header=False):
        self.configure(state='normal')
        if clear_header:
            self.delete('1.0', tk.END)
        else:
            self.delete('2.0', tk.END)
        self.configure(state='disable')

    def insert(self, index, chars, *args):
        line_count = int(self.index('end-1c').split('.')[0])
        self.configure(state='normal')
        if line_count > self.max_lines:
            self.delete('2.0', '3.0')
        super().insert(index, chars, *args)
        self.configure(state='disable')

    def resize_to_scale(self, scale):
        self.configure(font=(self.font[0], math.ceil(self.font[1] * scale[0])))

    @staticmethod
    def __disable_mouse_wheel(_event):
        return 'break'