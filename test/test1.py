import numpy as np
import trimesh
import mesh_opt
import open3d as o3d
from ipdb import set_trace


mesh = o3d.io.read_triangle_mesh('plane.ply')
vertices = np.asarray(mesh.vertices)
normals = np.asarray(mesh.vertex_normals)
faces = np.asarray(mesh.triangles)
# set_trace()

new_v, new_f, new_n = mesh_opt.normal_postprocess(vertices, faces, normals)

new_mesh = o3d.geometry.TriangleMesh()
new_mesh.vertices = o3d.utility.Vector3dVector(new_v)
new_mesh.triangles = o3d.utility.Vector3iVector(new_f)
new_mesh.vertex_normals = o3d.utility.Vector3dVector(new_n)
o3d.io.write_triangle_mesh('output.ply', new_mesh)
