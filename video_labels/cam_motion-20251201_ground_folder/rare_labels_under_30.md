# Rare Labels
Labels with less than 30 positive examples
| Definition | Positive Examples | Negative Examples | Label Name |
| --- | --- | --- | --- |
| Does the camera only tilt upward without any other camera movements? | 29 | 5086 | cam_motion.camera_centric_movement.tilt_up.only_tilt_up |
| Does the camera only pan rightward without any other camera movements? | 27 | 5088 | cam_motion.camera_centric_movement.pan_right.only_pan_right |
| Does the camera move only physically upward (not tilting up) relative to the ground (even if it's a bird's or worm's eye view)? | 25 | 5090 | cam_motion.ground_centric_movement.upward.only_upward_wrt_ground_birds_worms_included |
| Does the camera only roll counterclockwise without any other camera movements? | 25 | 5090 | cam_motion.camera_centric_movement.roll_counterclockwise.only_roll_counterclockwise |
| Is it a rear-side tracking shot where the camera follows the moving subject at a rear-side angle? | 22 | 4874 | cam_motion.object_centric_movement.rear_side_tracking_shot |
| Does the video contain a frame freeze effect at any point? | 15 | 5100 | cam_motion.has_frame_freezing |
| Is the camera craning downward in an arc relative to its own frame? | 14 | 4545 | cam_motion.arc_crane_movement.crane_down.has_crane_down |
| Is the scene in the video dynamic and features movement? | 0 | 0 | cam_motion.scene_movement.dynamic_scene |
| Is the scene in the video mostly static with minimal movement? | 0 | 0 | cam_motion.scene_movement.mostly_static_scene |
| Is the scene in the video completely static? | 0 | 0 | cam_motion.scene_movement.static_scene |
| Does the camera move backward (not zooming out) with respect to the initial frame? | 0 | 1933 | cam_motion.camera_centric_movement.backward.has_backward_wrt_camera |
| Does the camera move only physically backward (not zooming out) with respect to the initial frame, without any other movement? | 0 | 5115 | cam_motion.camera_centric_movement.backward.only_backward_wrt_camera |
| Does the camera move physically upward (or pedestals up) with respect to the initial frame? | 0 | 1933 | cam_motion.camera_centric_movement.upward.has_upward_wrt_camera |
| Does the camera only move physically upward (or pedestals up) without any other camera movements? | 0 | 5115 | cam_motion.camera_centric_movement.upward.only_upward_wrt_camera |
| Does the camera only move physically downward (or pedestals down) without any other camera movements? | 0 | 5115 | cam_motion.camera_centric_movement.downward.only_downward_wrt_camera |
| Does the camera move physically downward (or pedestals down) with respect to the initial frame? | 0 | 1933 | cam_motion.camera_centric_movement.downward.has_downward_wrt_camera |
| Does the camera move only physically forward (not zooming in) with respect to the initial frame, without any other movement? | 0 | 5115 | cam_motion.camera_centric_movement.forward.only_forward_wrt_camera |
| Does the camera physically move forward (not zooming in) with respect to the initial frame? | 0 | 1933 | cam_motion.camera_centric_movement.forward.has_forward_wrt_camera |
