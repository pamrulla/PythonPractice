# Move an object
bl_info = {
    "name" : "Select Connect",
    "author" : "Amrulla Khan",
    "version" : (0, 0, 1),
    "blender" : (2, 76, 0),
    "location" : "View3D > Edit > Select Connect",
    "description" : "Selects Connected Vertices",
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "Edit"
}

import bpy
import bmesh

class SelectConnet(bpy.types.Operator):
    """ Selects Connected Vertices """ 
    
    bl_idname = "object.select_connect"
    
    bl_label = "Select Connect"
    
    bl_options = { 'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return (context.mode == "EDIT_MESH")
        
    # execute function from where execution starts
    def execute(self, context):
        bm = bmesh.from_edit_mesh(context.object.data)
        
        to_visit = []
        
        for v in bm.verts:
            v.tag = False
            if v.select :
                to_visit.append(v)
        
        while to_visit:
            v = to_visit.pop()
            if v.tag :
                continue
            
            v.tag = True
            
            for e in v.link_edges:
                v2 = e.other_vert(v)
                if not v2.tag:
                    v2.select = True
                    to_visit.append(v2)
        
        bmesh.update_edit_mesh(context.object.data)
        
        return {'FINISHED'}
    
# To use in Belnder we need to register operator - register function
def register():
    bpy.utils.register_module(__name__) # register any class in a module that has REGISTER entry in bl_options
    
    bpy.types.VIEW3D_MT_edit_mesh.append(menu_func) # This will create a Object menu in 3D View entry based on the function passed
    
# To handle uninstalling an operator - unregister function
def unregister():
    bpy.utils.unregister_module(__name__) # unregisters
    
    bpy.types.VIEW3D_MT_edit_mesh.remove(menu_func) # removes menu entry
    
def menu_func(self, context):
    self.layout.operator(SelectConnet.bl_idname, icon="MESH_CUBE") # Links entry to menu to our operator using bl_idname and display Icon provided along with name from bl_label
    
