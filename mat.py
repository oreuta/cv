import bpy

class Mat:
    __mat_cash = {}

    def __init__(self, R=1.0, G=1.0, B=1.0, A=1.0):
        key = (R,G,B,A)
        m = Mat.__mat_cash.get(key)
        if not m:
            m = bpy.data.materials.new("M-{}_{}_{}-{}".format(R,G,B,A))
            m.diffuse_color = (R,G,B)
            m.alpha = A
            m.use_transparency = True
            Mat.__mat_cash.get[key] = m        	
        self._material = m


    def set_for(self, o):
        o.active_material = self._material

        
