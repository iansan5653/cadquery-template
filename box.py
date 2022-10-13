from cq_server.ui import ui, show_object
import cadquery as cq

result = cq.Workplane('XY').box(1, 2, 3)

show_object(result)
ui
