import sys, bpy

def create_armature(name, height_step, num, pos):
     bpy.ops.object.armature_add(enter_editmode=True)
     armature = bpy.context.object.data
     bpy.context.object.name = name
     armature.edit_bones.remove(armature.edit_bones[0])
     
     for i in range(num):
        new_bone = armature.edit_bones.new(f"NewBone{i}")
        new_bone.head = (0, 0, height_step * i)
        new_bone.tail = (0, 0, height_step * (i + 1))
        
     bpy.ops.object.mode_set(mode="OBJECT")
     bpy.context.object.location = pos
     # armature = bpy.types.Armature(bpy.data.objects["Hello"])

print("create armature")
for i in range(1, 6):
    create_armature(f"Hello{i}", 0.5, 10 * i, (0, i - 1, 0))