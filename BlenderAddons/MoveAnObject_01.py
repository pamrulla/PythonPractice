# Move an object
bl_info = {
    "name" : "Move Object",
    "author" : "Amrulla Khan",
    "version" : (0, 0, 1),
    "blender" : (2, 76, 0),
    "location" : "View3D > Object > Move",
    "dscription" : "Moves an object",
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "Object"
}

# An Operator is class that implements specific functionality
# Our operator class should be derived from bpy.types.Operator

import bpy

class MoveObject(bpy.types.Operator):
    """ Move an object """ # is a tooltip
    
    # Operators are part of Blender's data and stored in bpy.ops
    
    bl_idname = "object.move_object" # entry will be bpy.ops.object.move_object
    
    bl_label = "Move an object" # Label displayed in the menu
    
    bl_options = { 'REGISTER', 'UNDO'} # to register and add additional features like undo etc
    
    # execute function from where execution starts
    def execute(self, context):
        context.active_object.location.x += 1
        return {'FINISHED'}
    
    # To use in Belnder we need to register operator - register function
    def register():
        bpy.utils.register_module(__name__) # register any class in a module that has REGISTER entry in bl_options
        
        bpy.types.VIEW3D_MT_object.append(menu_func) # This will create a Object menu in 3D View entry based on the function passed
        
    # To handle uninstalling an operator - unregister function
    def unregister():
        bpy.utils.unregister_module(__name__) # unregisters
        
        bpy.types.VIEW3D_MT_object.remove(menu_func) # removes menu entry
        
    def menu_func(self, context):
        self.layout.operator(MoveObject.bl_idname, icon="MESH_CUBE") # Links entry to menu to our operator using bl_idname and display Icon provided along with name from bl_label
        
