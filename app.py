from taipy.gui import Gui
from taipy_designer import Page as DesignerPage
stock_symbol = "TSLA"

page = DesignerPage("live_stock.xprjson")

gui = Gui()
gui.add_page( "live_stock", page)
gui.run(port=2034)