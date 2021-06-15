import numpy as np
import os


def parse_simple_obj_file(obj_file):
    with open(obj_file, "r") as fin:
        lines = fin.readlines()
    vertices = []
    faces = []
    for line in lines:
        if line.startswith("v "):
            vertices.append(np.asarray(line[2:-1].split(" ")).astype(float))
        else:
            faces.append(np.asarray(line[2:-1].split(" ")).astype(float))
    vertices = np.asarray(vertices)
    faces = np.asarray(faces)
    if np.min(faces) == 1:
        faces = faces - 1
    return vertices, faces


in_dir = "/media/graphicslab/BigData/zavou/ANNFASS_CODE/mesh-fusion/examples/0_buildnet"
out_dir = "/media/graphicslab/BigData/zavou/ANNFASS_CODE/mesh-fusion/examples/1_buildnet"
for in_file in os.listdir(in_dir):
    v, f = parse_simple_obj_file(os.path.join(in_dir, in_file))
    f = f.astype(int)
    out_file = os.path.join(out_dir, in_file.replace(".obj", ".off"))
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, "w") as fout:
        fout.write("OFF\n")
        fout.write(f"{len(v)} {len(f)} 0\n")
        for vi in v:
            fout.write(f"{vi[0]} {vi[1]} {vi[2]}\n")
        for fi in f:
            fout.write(f"3 {fi[0]} {fi[1]} {fi[2]}\n")
