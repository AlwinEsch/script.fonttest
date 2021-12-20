import xbmcaddon
import xbmcgui

f = open(xbmcaddon.Addon().getAddonInfo("path") + "/example.txt", "r")
xbmcgui.Dialog().textviewer('Font test', f.read())
