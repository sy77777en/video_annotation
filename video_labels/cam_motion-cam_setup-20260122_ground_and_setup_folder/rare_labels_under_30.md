# Rare Labels
Labels with less than 30 positive examples
| Definition | Positive Examples | Negative Examples | Label Name |
| --- | --- | --- | --- |
| Does the video end with the camera completely out of focus? | 29 | 1893 | cam_setup.focus.end_with.focus_end_with_out_of_focus |
| Does the camera start in sharp focus and then shift out of focus? | 28 | 5844 | cam_setup.focus.focus_change_from_in_to_out_of_focus |
| Does the video start with the camera focused on the middle ground and then shift the focus to the foreground? | 27 | 1850 | cam_setup.focus.from_to.focus_from_middle_ground_to_foreground |
| Is it a rear-side tracking shot where the camera follows the moving subject at a rear-side angle? | 26 | 5847 | cam_motion.object_centric_movement.rear_side_tracking_shot |
| Does the camera only roll counterclockwise without any other camera movements? | 26 | 6092 | cam_motion.camera_centric_movement.roll_counterclockwise.only_roll_counterclockwise |
| Does the video show a broadcast-style viewpoint used in television production? | 26 | 5846 | cam_setup.point_of_view.broadcast_pov |
| Does the camera’s height relative to the subject start at the subject’s height and end below? | 26 | 4119 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_at_subject_to_below_subject |
| Does the camera use focus tracking to keep a subject in focus in the video? | 25 | 4926 | cam_setup.focus.is_focus_tracking |
| Does the camera’s height relative to the subject start below and end above? | 24 | 4121 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_below_subject_to_above_subject |
| Is this a forward-facing dashcam view from a vehicle-mounted camera, capturing the scene ahead? | 23 | 5849 | cam_setup.point_of_view.dashcam_pov |
| Does the camera’s height relative to the subject start below and end at the subject’s height? | 23 | 4122 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_below_subject_to_at_subject |
| Does the camera transition from underwater to above water? | 23 | 4246 | cam_setup.height_wrt_ground.underwater_to_above_water |
| Does the camera transition from above water to underwater? | 21 | 4248 | cam_setup.height_wrt_ground.above_water_to_underwater |
| Is this a screen recording of a software or system interface (e.g., menus, windows, toolbars)? | 20 | 5852 | cam_setup.point_of_view.screen_recording_pov |
| Does the video start with the camera focused on the foreground and then shift the focus to the background? | 19 | 1901 | cam_setup.focus.from_to.focus_from_foreground_to_background |
| Does the video start with the camera focused on the background and then shift the focus to the foreground? | 18 | 1906 | cam_setup.focus.from_to.focus_from_background_to_foreground |
| Is the camera craning downward in an arc relative to its own frame? | 16 | 5459 | cam_motion.arc_crane_movement.crane_down.has_crane_down |
| Does the video contain a frame freezing effect at any point? | 14 | 6104 | cam_motion.has_frame_freezing |
| Does the camera’s height relative to the subject start above and end below? | 13 | 4132 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_above_subject_to_below_subject |
| Does the video start with the camera focused on the background and then shift the focus to the middleground? | 9 | 1915 | cam_setup.focus.from_to.focus_from_background_to_middle_ground |
| Does the video start with the camera focused on the middle ground and then shift the focus to the background? | 7 | 1917 | cam_setup.focus.from_to.focus_from_middle_ground_to_background |
| Is the camera consistently out of focus throughout? | 1 | 1923 | cam_setup.focus.is_always.focus_is_out_of_focus |
| Is the scene in the video dynamic and features movement? | 0 | 0 | cam_motion.scene_movement.dynamic_scene |
| Is the scene in the video mostly static with minimal movement? | 0 | 0 | cam_motion.scene_movement.mostly_static_scene |
| Is the scene in the video completely static? | 0 | 0 | cam_motion.scene_movement.static_scene |
| Does the camera move backward (not zooming out) with respect to the initial frame? | 0 | 2483 | cam_motion.camera_centric_movement.backward.has_backward_wrt_camera |
| Does the camera move only physically backward (not zooming out) with respect to the initial frame, without any other movement? | 0 | 6118 | cam_motion.camera_centric_movement.backward.only_backward_wrt_camera |
| Does the camera move physically upward (or pedestals up) with respect to the initial frame? | 0 | 2483 | cam_motion.camera_centric_movement.upward.has_upward_wrt_camera |
| Does the camera only move physically upward (or pedestals up) without any other camera movements? | 0 | 6118 | cam_motion.camera_centric_movement.upward.only_upward_wrt_camera |
| Does the camera only move physically downward (or pedestals down) without any other camera movements? | 0 | 6118 | cam_motion.camera_centric_movement.downward.only_downward_wrt_camera |
| Does the camera move physically downward (or pedestals down) with respect to the initial frame? | 0 | 2483 | cam_motion.camera_centric_movement.downward.has_downward_wrt_camera |
| Does the camera move only physically forward (not zooming in) with respect to the initial frame, without any other movement? | 0 | 6118 | cam_motion.camera_centric_movement.forward.only_forward_wrt_camera |
| Does the camera physically move forward (not zooming in) with respect to the initial frame? | 0 | 2483 | cam_motion.camera_centric_movement.forward.has_forward_wrt_camera |
