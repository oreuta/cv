import bpy

def make_voxel(loc=(0,0,0), dim=(1,1,1)):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    v = bpy.context.active_object
    v.dimensions = dim
    return v
