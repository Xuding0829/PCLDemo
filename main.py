import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt


def point_show(path, point_type):
    pcd = o3d.io.read_point_cloud(path, format=point_type, remove_nan_points=True, remove_infinite_points=True, print_progress=True)
    # 路径、输入格式、删除包含NAN的所有点、删除包含无限值的所有点、可视化进度条
    print(pcd)  # 输出点云点的个数
    print(np.asarray(pcd.points))  # 输出点的三维坐标
    """
       格式	    描述
       xyz	    每一行包含[x,y,z]，其中x,y,z是三维坐标
       xyz n	每一行包含[x,y,z,nx,ny,nz]，其中x,y,z是三维坐标，nx,ny,nz是法向量
       xyz rgb	每一行包含[x,y,z,r,g,b]，其中x,y,z是三维坐标，r,g,b是颜色信息，取值范围是[0,1]
       pts	    第一行是表示点数的整数。随后的行遵循以下一种格式：[x,y,z,i,r,g,b],[x,y,z,r,g,b],[x,y,z,i]或[x,y,z],，其中x,y,z,i是double类型，r,g,b是un int8类型
       ply	    见：多边形文件格式，ply文件可同时包含点云和网格数据
       pcd	    见：点云数据
    """
    # pcd.paint_uniform_color([0, 1, 1])  # 固定颜色显示
    # pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, (1,3)))  # 随机颜色显示
    o3d.visualization.draw_geometries([pcd], window_name='Point Cloud View', width=1920, height=1080, left=50, top=50,
                                      point_show_normal=False, mesh_show_wireframe=False, mesh_show_back_face=False)
    # zoom=0.3412,front=[0.4257, -0.2125, -0.8795],lookat=[2.6172, 2.0475, 1.532],up=[-0.0694, -0.9768, 0.2024]
    # 显示内容、窗口标题、长、宽、左边距、右边距、是否可视化法线、是否可视化网络线框、是否可视化网络三角形背面
    o3d.io.write_point_cloud(r'temp.xyz', pcd, write_ascii=False, compressed=False, print_progress=True)
    # 路径、文件、以ascii格式输出否则使用二进制输出、以压缩格式写入、可视化进度条


if __name__ == "__main__":
    Path = r'cow.ply'
    Type = 'ply'
    point_show(Path, Type)