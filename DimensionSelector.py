bl_info = {
    'name': 'Dimension Selector',
    'blender': (3, 1, 2),
    'category': 'Tools',
    'version': (1, 0, 0),
    'author': 'Disnejar',
    'description': 'A simple add on for selecting all objects with the same dimensions',
}

import bpy


class DIMENSIONSELTOOL_OT_select(bpy.types.Operator):
    bl_idname = "dimensionseltool.select"
    bl_options = {'REGISTER', 'UNDO'}
    
    bl_label = "Select"
    bl_description = "Select all objects with the same dimensions (rounded up to 3 decimals)"

    def execute(self, context):
        
        new_dim = [0, 0, 0]
        new_dim[0] = context.scene.X
        new_dim[1] = context.scene.Y
        new_dim[2] = context.scene.Z
        
        if not context.scene.add:
            for obj in context.selected_objects:
                obj.select_set(False)
        
        for obj in context.scene.objects:
            if round(obj.dimensions.x, 3) == round(new_dim[0], 3) and round(obj.dimensions.y, 3) == round(new_dim[1], 3) and round(obj.dimensions.z, 3) == round(new_dim[2], 3):
                obj.select_set(True)
                context.view_layer.objects.active = obj

                
        return {'FINISHED'}
    
    
class DIMENSIONSELTOOL_OT_use_active(bpy.types.Operator):
    bl_idname = "dimensionseltool.use_active"
    bl_options = {'REGISTER', 'UNDO'}
    
    bl_label = "Use Active Dimensions"
    bl_description = "Use the dimensions of the active object"

    def execute(self, context):
        if not context.active_object == None:
            context.scene.X = context.active_object.dimensions.x
            context.scene.Y = context.active_object.dimensions.y
            context.scene.Z = context.active_object.dimensions.z
                
        return {'FINISHED'}
    

class DIMENSIONSELTOOL_PT_panel(bpy.types.Panel):
    bl_idname = "DIMENSIONSELTOOL_PT_panel"
    bl_label = "Dimension Selector"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"

    def draw(self, context):
        
        box = self.layout.box()
        
        row = box.row()
        row.label(text = 'Dimensions')
            
        col = box.column(align = True)
        col.prop(context.scene, "X")
        col.prop(context.scene, "Y")
        col.prop(context.scene, "Z")
            
        row = box.row()
        row.operator('dimensionseltool.use_active')
        
        row = box.row()
        row.prop(context.scene, "add")
        
        row = self.layout.row()
        row.operator('dimensionseltool.select')
        
        #self.layout.row.prop(context.scene.boundaryseltool.select.my_dim, "Dimensions")
        #props = self.layout.operator('boundaryseltool.select')



PROPS = [
    ('X', bpy.props.FloatProperty(name='X', default=0, precision = 3)),
    ('Y', bpy.props.FloatProperty(name='Y', default=0, precision = 3)),
    ('Z', bpy.props.FloatProperty(name='Z', default=0, precision = 3)),
    ('add', bpy.props.BoolProperty(name='Add To Selection', default=False)),
]


CLASSES = [
    DIMENSIONSELTOOL_OT_select,
    DIMENSIONSELTOOL_OT_use_active,
    DIMENSIONSELTOOL_PT_panel
]


def register():
    for (prop_name, prop_value) in PROPS:
        setattr(bpy.types.Scene, prop_name, prop_value)
    
    for klass in CLASSES:
        bpy.utils.register_class(klass)

def unregister():
    for klass in CLASSES:
        bpy.utils.unregister_class(klass)
        

print("new Run")
