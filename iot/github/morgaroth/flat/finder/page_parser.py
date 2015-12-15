from iot.github.morgaroth.utils.ModuleLoad import MyModuleLoadError

try:
    from bs4 import BeautifulSoup
except:
    raise MyModuleLoadError("beatifulsoup4")
