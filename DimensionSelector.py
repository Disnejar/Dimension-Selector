bl_info = {
    'name': 'Dimension Selector',
    'blender': (3, 1, 2),
    'category': 'Tools',
    'version': (1, 1, 3),
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
        
        for obj in context.selectable_objects:
            if round(obj.dimensions.x, 3) == round(new_dim[0], 3) and round(obj.dimensions.y, 3) == round(new_dim[1], 3) and round(obj.dimensions.z, 3) == round(new_dim[2], 3):
                obj.select_set(True)
                context.view_layer.objects.active = obj
            else: 
                if round(obj.dimensions.x, 3) == round(new_dim[0], 3) and round(obj.dimensions.y, 3) == round(new_dim[2], 3) and round(obj.dimensions.z, 3) == round(new_dim[1], 3):
                    obj.select_set(True)
                    context.view_layer.objects.active = obj
                else:
                    if round(obj.dimensions.x, 3) == round(new_dim[2], 3) and round(obj.dimensions.y, 3) == round(new_dim[1], 3) and round(obj.dimensions.z, 3) == round(new_dim[0], 3):
                        obj.select_set(True)
                        context.view_layer.objects.active = obj
                    else:
                        if round(obj.dimensions.x, 3) == round(new_dim[1], 3) and round(obj.dimensions.y, 3) == round(new_dim[0], 3) and round(obj.dimensions.z, 3) == round(new_dim[2], 3):
                            obj.select_set(True)
                            context.view_layer.objects.active = obj
                            
            if context.scene.smaller:
                if round(obj.dimensions.x, 3) <= round(new_dim[0], 3) and round(obj.dimensions.y, 3) <= round(new_dim[1], 3) and round(obj.dimensions.z, 3) <= round(new_dim[2], 3):
                    if context.scene.allSmaller:
                        obj.select_set(True)
                        context.view_layer.objects.active = obj
                    else:
                        if round(obj.dimensions.x, 3) >= round(new_dim[0], 3) * float(context.scene.smallerPercentage) / 100.0 and round(obj.dimensions.y, 3) >= round(new_dim[1], 3) * float(context.scene.smallerPercentage) / 100.0 and round(obj.dimensions.z, 3) >= round(new_dim[2], 3) * float(context.scene.smallerPercentage) / 100.0:
                            obj.select_set(True)
                            context.view_layer.objects.active = obj
                if round(obj.dimensions.x, 3) <= round(new_dim[1], 3) and round(obj.dimensions.y, 3) <= round(new_dim[0], 3) and round(obj.dimensions.z, 3) <= round(new_dim[2], 3):
                    if context.scene.allSmaller:
                        obj.select_set(True)
                        context.view_layer.objects.active = obj
                    else:
                        if round(obj.dimensions.x, 3) >= round(new_dim[1], 3) * float(context.scene.smallerPercentage) / 100.0 and round(obj.dimensions.y, 3) >= round(new_dim[0], 3) * float(context.scene.smallerPercentage) / 100.0 and round(obj.dimensions.z, 3) >= round(new_dim[2], 3) * float(context.scene.smallerPercentage) / 100.0:
                            obj.select_set(True)
                            context.view_layer.objects.active = obj
                if round(obj.dimensions.x, 3) <= round(new_dim[2], 3) and round(obj.dimensions.y, 3) <= round(new_dim[1], 3) and round(obj.dimensions.z, 3) <= round(new_dim[0], 3):
                    if context.scene.allSmaller:
                        obj.select_set(True)
                        context.view_layer.objects.active = obj
                    else:
                        if round(obj.dimensions.x, 3) >= round(new_dim[2], 3) * float(context.scene.smallerPercentage) / 100.0 and round(obj.dimensions.y, 3) >= round(new_dim[1], 3) * float(context.scene.smallerPercentage) / 100.0 and round(obj.dimensions.z, 3) >= round(new_dim[0], 3) * float(context.scene.smallerPercentage) / 100.0:
                            obj.select_set(True)
                            context.view_layer.objects.active = obj
                if round(obj.dimensions.x, 3) <= round(new_dim[0], 3) and round(obj.dimensions.y, 3) <= round(new_dim[2], 3) and round(obj.dimensions.z, 3) <= round(new_dim[1], 3):
                    if context.scene.allSmaller:
                        obj.select_set(True)
                        context.view_layer.objects.active = obj
                    else:
                        if round(obj.dimensions.x, 3) >= round(new_dim[0], 3) * float(context.scene.smallerPercentage) / 100.0 and round(obj.dimensions.y, 3) >= round(new_dim[2], 3) * float(context.scene.smallerPercentage) / 100.0 and round(obj.dimensions.z, 3) >= round(new_dim[1], 3) * float(context.scene.smallerPercentage) / 100.0:
                            obj.select_set(True)
                            context.view_layer.objects.active = obj
                
            if context.scene.bigger:
                if round(obj.dimensions.x, 3) >= round(new_dim[0], 3) and round(obj.dimensions.y, 3) >= round(new_dim[1], 3) and round(obj.dimensions.z, 3) >= round(new_dim[2], 3):
                    if context.scene.allBigger:
                        obj.select_set(True)
                        context.view_layer.objects.active = obj
                    else:
                        if round(obj.dimensions.x, 3) <= round(new_dim[0], 3) * float(context.scene.biggerPercentage) / 100.0 and round(obj.dimensions.y, 3) <= round(new_dim[1], 3) * float(context.scene.biggerPercentage) / 100.0 and round(obj.dimensions.z, 3) <= round(new_dim[2], 3) * float(context.scene.biggerPercentage) / 100.0:
                            obj.select_set(True)
                            context.view_layer.objects.active = obj
                if round(obj.dimensions.x, 3) >= round(new_dim[1], 3) and round(obj.dimensions.y, 3) >= round(new_dim[0], 3) and round(obj.dimensions.z, 3) >= round(new_dim[2], 3):
                    if context.scene.allBigger:
                        obj.select_set(True)
                        context.view_layer.objects.active = obj
                    else:
                        if round(obj.dimensions.x, 3) <= round(new_dim[1], 3) * float(context.scene.biggerPercentage) / 100.0 and round(obj.dimensions.y, 3) <= round(new_dim[0], 3) * float(context.scene.biggerPercentage) / 100.0 and round(obj.dimensions.z, 3) <= round(new_dim[2], 3) * float(context.scene.biggerPercentage) / 100.0:
                            obj.select_set(True)
                            context.view_layer.objects.active = obj
                if round(obj.dimensions.x, 3) >= round(new_dim[2], 3) and round(obj.dimensions.y, 3) >= round(new_dim[1], 3) and round(obj.dimensions.z, 3) >= round(new_dim[0], 3):
                    if context.scene.allBigger:
                        obj.select_set(True)
                        context.view_layer.objects.active = obj
                    else:
                        if round(obj.dimensions.x, 3) <= round(new_dim[2], 3) * float(context.scene.biggerPercentage) / 100.0 and round(obj.dimensions.y, 3) <= round(new_dim[1], 3) * float(context.scene.biggerPercentage) / 100.0 and round(obj.dimensions.z, 3) <= round(new_dim[0], 3) * float(context.scene.biggerPercentage) / 100.0:
                            obj.select_set(True)
                            context.view_layer.objects.active = obj
                if round(obj.dimensions.x, 3) >= round(new_dim[0], 3) and round(obj.dimensions.y, 3) >= round(new_dim[2], 3) and round(obj.dimensions.z, 3) >= round(new_dim[1], 3):
                    if context.scene.allBigger:
                        obj.select_set(True)
                        context.view_layer.objects.active = obj
                    else:
                        if round(obj.dimensions.x, 3) <= round(new_dim[0], 3) * float(context.scene.biggerPercentage) / 100.0 and round(obj.dimensions.y, 3) <= round(new_dim[2], 3) * float(context.scene.biggerPercentage) / 100.0 and round(obj.dimensions.z, 3) <= round(new_dim[1], 3) * float(context.scene.biggerPercentage) / 100.0:
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
        
        
class DIMENSIONSELTOOL_PT_dimensions_panel(bpy.types.Panel):
    bl_idname = "DIMENSIONSELTOOL_PT_dimensions_panel"
    bl_label = "Dimensions"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Dimensional Select"
    
    def draw(self, context):
            
        col = self.layout.column(align = True)
        col.prop(context.scene, "X")
        col.prop(context.scene, "Y")
        col.prop(context.scene, "Z")
        
        row = self.layout.row()
        row.operator('dimensionseltool.use_active')
        
class DIMENSIONSELTOOL_PT_selection_panel(bpy.types.Panel):
    bl_idname = "DIMENSIONSELTOOL_PT_selection_panel"
    bl_label = "Selection Options"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Dimensional Select"
    
    def draw(self, context):
            
        row = self.layout.row()
        row.prop(context.scene, 'add')
        
        
        row = self.layout.row()
        row.prop(context.scene, 'bigger')
        
        if context.scene.bigger:
            row = self.layout.row()
            row.prop(context.scene, 'allBigger')
                
            if not context.scene.allBigger:
                row = self.layout.row()
                row.prop(context.scene, 'biggerPercentage')
                
                
        row = self.layout.row()
        row.prop(context.scene, 'smaller')
        
        if context.scene.smaller:
            row = self.layout.row()
            row.prop(context.scene, 'allSmaller')
                
            if not context.scene.allSmaller:
                row = self.layout.row()
                row.prop(context.scene, 'smallerPercentage')
                    
        row = self.layout.row()
        row.operator('dimensionseltool.select')
        


PROPS = [
    ('X', bpy.props.FloatProperty(name='X', default=0, precision = 3, unit = 'LENGTH', subtype = 'DISTANCE')),
    ('Y', bpy.props.FloatProperty(name='Y', default=0, precision = 3, unit = 'LENGTH', subtype = 'DISTANCE')),
    ('Z', bpy.props.FloatProperty(name='Z', default=0, precision = 3, unit = 'LENGTH', subtype = 'DISTANCE')),
    ('add', bpy.props.BoolProperty(name='Add To Selection', default=False)),
    ('bigger', bpy.props.BoolProperty(name='Select Bigger Objects', default=True)),
    ('smaller', bpy.props.BoolProperty(name='Select Smaller Objects', default=True)),
    ('allSmaller', bpy.props.BoolProperty(name='Select All Smaller Objects', default=False)),
    ('allBigger', bpy.props.BoolProperty(name='Select All Bigger Objects', default=False)),
    ('biggerPercentage', bpy.props.IntProperty(name='Percantage', default=150, soft_max = 500, min = 100, soft_min = 100, subtype = 'PERCENTAGE')),
    ('smallerPercentage', bpy.props.IntProperty(name='Percantage', default=50, max = 100, min = 0, subtype = 'PERCENTAGE')),
]

CLASSES = [
    DIMENSIONSELTOOL_OT_select,
    DIMENSIONSELTOOL_OT_use_active,
    DIMENSIONSELTOOL_PT_dimensions_panel,
    DIMENSIONSELTOOL_PT_selection_panel
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
