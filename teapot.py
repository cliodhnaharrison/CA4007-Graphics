#!/usr/bin/env python3

"""
CA4007 - Computer Graphics & Image Processing Assignment
Student Name: Cliodhna Harrison
Student ID: 15440568
"""

from matplotlib import pyplot as plt
import numpy as np

def original_3d(teapot):
    """
    Code from assignment spec to plot 3D point cloud of teapot
    """
    ax = plt.axes(projection ='3d')
    ax.plot3D(teapot[: , 0], teapot[: , 1], teapot[: , 2], 'r.')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def objective_one(teapot, focal_length, cx, cy):
    """
    Objective one from assignment spec. Camera position move to [0, 0, 10] and
    performed projection. Image saving commented out.
    """

    # Intrinsics matrix, fx = fy = 1000, no skew so set to 0
    intrinsics = np.array([[focal_length, 0, cx, 0],
                           [0, focal_length, cy, 0],
                           [0, 0, 1, 0]])

    # Identity matrix and translation vector [0, 0, 10] given in spec
    # Tried to create identity matrix with np.eye(3) and np.append the translation vector
    # Couldn't quite figure this out in time so just wrote the matrix
    """
    camera = np.eye(3)
    translation = np.array([[0, 0, 10]])
    camera = np.append(camera, translation, axis=1)
    """
    camera = np.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 10],
                       [0, 0, 0, 1]])

    projection = intrinsics.dot(camera)
    teapot_one = np.append(teapot, np.ones((1177, 1)), axis=1)
    teapot_one = np.transpose(teapot_one)
    teapot_one = projection.dot(teapot_one)
    teapot_one[0] = np.divide(teapot_one[0], teapot_one[2])
    teapot_one[1] = np.divide(teapot_one[1], teapot_one[2])
    teapot_one = np.transpose(teapot_one)

    ax = plt.axes()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.ylim(0, 200)
    plt.xlim(0, 300)
    ax.plot(teapot_one[:, 0],teapot_one[:, 1], 'r.')
    #plt.savefig("teapot_one.png")
    plt.show()

def objective_two(teapot, focal_length):
    """
    Objective two from assignment spec. Resolution of image changed to 1920x1080.
    Camera position moved to [0, 0, 5] to get closer view of teapot.
    Image saving commented out.
    """
    # Edited cx, cy values as per objective two, resolution 1920 x 1080
    cx = 960
    cy = 540
    # Intrinsics matrix, fx = fy = 1000, no skew so set to 0
    intrinsics = np.array([[focal_length, 0, cx, 0],
                           [0, focal_length, cy, 0],
                           [0, 0, 1, 0]])

    #  identity matrix and translation vector [0, 0]
    camera = np.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 5],
                       [0, 0, 0, 1]])

    projection = intrinsics.dot(camera)
    teapot_two = np.append(teapot, np.ones((1177, 1)), axis=1)
    teapot_two = np.transpose(teapot_two)
    teapot_two = projection.dot(teapot_two)
    teapot_two[0] = np.divide(teapot_two[0], teapot_two[2])
    teapot_two[1] = np.divide(teapot_two[1], teapot_two[2])
    teapot_two = np.transpose(teapot_two)

    ax = plt.axes()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.ylim(0, 1080)
    plt.xlim(0, 1920)
    ax.plot(teapot_two[:, 0],teapot_two[:, 1], 'r.')
    #plt.savefig("teapot_two.png")
    plt.show()

def main():
    # Properties from assignment spec
    focal_length = 1000
    cx = cy = 0
    teapot = np.load('teapot.npy')
    objective_one(teapot, focal_length, cx, cy)
    objective_two(teapot, focal_length)

if __name__ == "__main__":
    main()
