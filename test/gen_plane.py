import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_plane_mesh(width, height, resolution):
    x = np.linspace(-width/2, width/2, resolution)
    y = np.linspace(-height/2, height/2, resolution)
    x, y = np.meshgrid(x, y)
    z = np.zeros_like(x)
    

    vertices = np.vstack([x.ravel(), y.ravel(), z.ravel()]).T
    
    
    faces = []
    for i in range(resolution-1):
        for j in range(resolution-1):
            idx = i * resolution + j
            faces.append([idx, idx + 1, idx + resolution])
            faces.append([idx + 1, idx + resolution + 1, idx + resolution])
    
    faces = np.array(faces)
    
    
    normals = np.zeros_like(vertices)
    normals[:, 2] = 1  
    
    
    noise_strength = 0.3  
    noise = np.random.uniform(-noise_strength, noise_strength, size=vertices.shape)
    normals += noise
    
    
    norms = np.linalg.norm(normals, axis=1, keepdims=True)
    normals /= norms
    
    return vertices, faces, normals


width = 10
height = 10
resolution = 50

vertices, faces, normals = generate_plane_mesh(width, height, resolution)

# save mesh
mesh = o3d.geometry.TriangleMesh()
mesh.vertices = o3d.utility.Vector3dVector(vertices)
mesh.triangles = o3d.utility.Vector3iVector(faces)
mesh.vertex_normals = o3d.utility.Vector3dVector(normals)
o3d.io.write_triangle_mesh('plane.ply', mesh)
