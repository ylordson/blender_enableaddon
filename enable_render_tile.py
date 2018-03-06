import bpy
import addon_utils
addon_utils.enable('render_auto_tile_size', default_set=True, persistent=False, handle_error=None)
bpy.ops.wm.save_userpref()
