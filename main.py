#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx

def main():
    app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
    frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
    frame.Show(True)     # Show the frame.
    app.MainLoop()
    
if __name__ == "__main__":
    main()
