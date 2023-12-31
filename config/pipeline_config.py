import numpy as np

#vhicle danger zone
x0_danger_zone=400#300#400
x1_danger_zone=800#900#800
y0_danger_zone=300
y1_danger_zone=250#150#200
w_danger_zone=100#150#100

# x0 = x0_danger_zone
# x1 = x1_danger_zone
# y0 = y0_danger_zone
# y1 = y1_danger_zone
# w = w_danger_zone

#image augmentation
INFERENCE_W = 1280
INFERENCE_H = 288
CROP_TOP = 100
INFERENCE_SCALE = 1

#camera callibaration data of kitti
KITTI_P2_0 = np.array([[ 7.215377000000e+02, 0.000000000000e+00, 6.095593000000e+02, 4.485728000000e+01,],
                 [0.000000000000e+00, 7.215377000000e+02, 1.728540000000e+02, 2.163791000000e-01,],
                 [0.000000000000e+00, 0.000000000000e+00, 1.000000000000e+00, 2.745884000000e-03],])
                
KITTI_P3_0 = np.array([[ 7.215377000000e+02, 0.000000000000e+00, 6.095593000000e+02, -3.395242000000e+02,],
                 [ 0.000000000000e+00, 7.215377000000e+02, 1.728540000000e+02, 2.199936000000e+00,],
                 [ 0.000000000000e+00, 0.000000000000e+00, 1.000000000000e+00, 2.729905000000e-03],])

#camera callibaration data of CARLA simulation
CARLA_P2_0 = np.array([[6.27370e+02, 0.000000000000e+00, 6.4e+02, 0.000000000000e+00,],
 [0.000000000000e+00, 6.27370e+02, 1.92e+02, 0.000000000000e+00,],
 [0.000000000000e+00, 0.000000000000e+00, 1.000000000000e+00, 0.000000000000e+00],])

CARLA_P3_0 = np.array([[6.27370e+02, 0.000000000000e+00, 6.4e+02, 0.000000000000e+00,],
 [0.000000000000e+00, 6.27370e+02, 1.92e+02, 0.000000000000e+00,],
 [0.000000000000e+00, 0.000000000000e+00, 1.000000000000e+00, 0.000000000000e+00],])


#camera callibaration data of CARLA simulation
CARLA_P21_0 = np.array([[2.849402008100e+02, 0.000000000000e+00, 1.777973651900e+02, 0.000000000000e+00,],
 [0.000000000000e+00, 2.849402008100e+02, 1.344622583400e+02, 0.000000000000e+00,],
 [0.000000000000e+00, 0.000000000000e+00, 1.000000000000e+00, 0.000000000000e+00],])

CARLA_P31_0 = np.array([[ 2.84940201e+02,  0.00000000e+00,  1.77797365e+02, -1.47113186e+04],
 [ 0.00000000e+00,  2.84940201e+02,  1.34462258e+02,  0.00000000e+00],
 [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00,  0.00000000e+00],])



CARLA_P22_0 = np.array([[9.5107990705e+02,  0.000000000000e+00, 6.91e+02, 0.000000000000e+00 ],[0.000000000000e+00        , 9.5107990705e+02, 2.56e+02        ,   0.000000000000e+00     ],
                       [0.000000000000e+00, 0.000000000000e+00, 1.00000000e+00, 0.000000000000e+00 ]])
CARLA_P32_0 = np.array([[9.5107990705e+02,  0.000000000000e+00, 6.91e+02, 0.000000000000e+00 ],[0.000000000000e+00        , 9.5107990705e+02, 2.56e+02        ,   0.000000000000e+00     ],
                       [0.000000000000e+00, 0.000000000000e+00, 1.00000000e+00, 0.000000000000e+00 ]])

#camera callibaration data of stereo camera
LOCAL_P2_0 = np.array([[2.849402008100e+02, 0.000000000000e+00, 1.777973651900e+02, 0.000000000000e+00,],
                 [0.000000000000e+00, 2.849402008100e+02, 1.344622583400e+02, 0.000000000000e+00,],
                 [0.000000000000e+00, 0.000000000000e+00, 1.000000000000e+00, 0.000000000000e+00],]) 

LOCAL_P3_0 = np.array([[2.849402008100e+02, 0.000000000000e+00, 1.777973650000e+02, -1.471131860000e+04,],
                 [0.000000000000e+00, 2.849402010000e+02, 1.344622580000e+02, 0.000000000000e+00,],
                 [0.000000000000e+00, 0.000000000000e+00, 1.000000000000e+00, 0.000000000000e+00],]) 

#camera callibaration data
P2 = KITTI_P2_0
P3 = KITTI_P3_0

#kalman filter configs
#KalmanBoxTracker
Tracker_dim_x=7
Tracker_dim_z=4
Tracker_kf_F = np.array([[1,0,0,0,1,0,0],[0,1,0,0,0,1,0],[0,0,1,0,0,0,1],[0,0,0,1,0,0,0],  [0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]])
Tracker_kf_H = np.array([[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0]])

Tracker_kf_R22 = 10.
Tracker_kf_P44 = 1000. #give high uncertainty to the unobservable initial velocities
Tracker_kf_P = 10.
Tracker_kf_Q11 = 0.01
Tracker_kf_Q44 = 0.01

#KalmanBoxTrajectory
Trajectory_dim_x=7
Trajectory_dim_z=4
Trajectory_kf_F = np.array([[1,0,0,0,1,0,0],[0,1,0,0,0,1,0],[0,0,1,0,0,0,1],[0,0,0,1,0,0,0],  [0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]])
Trajectory_kf_H = np.array([[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0]])

Trajectory_kf_R22 = 10.
Trajectory_kf_P44 = 1000. #give high uncertainty to the unobservable initial velocities
Trajectory_kf_P = 10.
Trajectory_kf_Q11 = 0.01
Trajectory_kf_Q44 = 0.01