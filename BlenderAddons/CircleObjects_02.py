bl_info = {
    "name" : "Circle Objects",
    "author" : "Amrulla Khan",
    "version" : (0, 0, 1),
    "blender" : (2, 76, 0),
    "location" : "View3D > Object > Circle",
    "dscription" : "Arranges selected objects in a circle",
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "Object"
}

# An Operator is class that implements specific functionality
# Our operator class should be derived from bpy.types.Operator

import bpy
from bpy.props import FloatProperty # this is float property type
from bpy.props import FloatVectorProperty
from bpy.props import EnumProperty

class CircleObjects(bpy.types.Operator):
    """ Arranges selected objects in a circle in xy plane """ # is a tooltip
    
    # Operators are part of Blender's data and stored in bpy.ops
    
    bl_idname = "object.circle_objects" # entry will be bpy.ops.object.move_object
    
    bl_label = "Circle Objects" # Label displayed in the menu
    
    bl_options = { 'REGISTER', 'UNDO', 'PRESET'} # PRESET shows preset option in tool bar to save values for later use
    
    # Now scale is a property, a slider displays in tool bar for customization of scale value
    scale = FloatProperty (
        name = "Scale",
        description = "Scale the radius of the circle",
        default = 100,
        min = 0,
        subtype = "PERCENTAGE"
    )
    
    axis = FloatVectorProperty (
        name = "Axis",
        description = "Arbitrary circle orientation",
        default = (0,0,1),
        subtype = "DIRECTION"
    )
    
    orientation = EnumProperty(
        name="Orientation",
        description="Circle orientation",
        items=[
                ('X','X-Axis','X-Axis'),
                ('Y','Y-Axis','Y-Axis'),
                ('Z','Z-Axis','Z-Axis'),
                ('A','Arbitrary Axis','Arbitrary Axis')],
        default='Z'
    )
    
    cardinals = { 'X' : Vector((1,0,0)), 'Y' : Vector((0,1,0)), 'Z' : Vector((0,0,1)) }
    
    # the poll method decides when to enable and disable operator
    # When more than 2 objetcs are selected and mode is object then only circle objetcs operator is enables otherwise it is disabled.
    @classmethod
    def poll(cls, context):
        return ((len(context.selected_objects) > 2) and (context.mode == "OBJECT"))
    
    # execute function from where execution starts
    def execute(self, context):
        xyz = [ob.location for ob in context.selected_objects]
        
        center = sum(xyz, Vector()) / len(xyz)
        
        radius = sum((loc.xy - center.xy).length for loc in xyz)
        
        radius /= len(xyz)
        
        if self.orientation in self.cardinals:
            orientation = self.cardinals[self.orientation]
        else:
            orientation = self.axis
        
        rotation = self.cardinals['Z'].rotation_difference(orientation)
        
        for loc, ob in zip(xyz, context.selected_objects):
            direction = (loc.xy - center.xy).normalized().to_3d()
            direction = rotation * direction
            ob.location = center + self.scale * 0.01 * radius * direction
        
        return {'FINISHED'}
    
    def dar(self, context):
		layout = self.layout
		layout.prop(self, 'scale')
		layout.prop(self, 'orientation')
		if self.orientation == 'A':
			layout.prop(self, 'axis', text="")
        
    # To use in Belnder we need to register operator - register function
    def register():
        bpy.utils.register_module(__name__) # register any class in a module that has REGISTER entry in bl_options
        
        bpy.types.VIEW3D_MT_object.append(menu_func) # This will create a Object menu in 3D View entry based on the function passed
        
    # To handle uninstalling an operator - unregister function
    def unregister():
        bpy.utils.unregister_module(__name__) # unregisters
        
        bpy.types.VIEW3D_MT_object.remove(menu_func) # removes menu entry
        
    def menu_func(self, context):
        self.layout.operator(CircleObjects.bl_idname, icon='PLUGIN')
    
    
    
    
