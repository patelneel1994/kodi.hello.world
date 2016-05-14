import xbmcaddon
import xbmcgui
 
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

m1 = 'Hello Sam'
m2 = 'Testing------'
m3 = 'TEsting 22222'

xbmcgui.Dialog().ok(addonname, m1, m2, m3)