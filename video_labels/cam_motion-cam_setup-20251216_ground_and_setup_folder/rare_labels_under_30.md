# Rare Labels
Labels with less than 30 positive examples
| Definition | Positive Examples | Negative Examples | Label Name |
| --- | --- | --- | --- |
| Does the video start with the camera at a high angle and transition to a low angle? | 29 | 4444 | cam_setup.angle.from_to.camera_angle_from_high_to_low |
| Is it a fast-motion video with forward playback speed slightly faster than real-time (about 1.5×–3×), but not a time-lapse where the speed is greatly accelerated over a long duration? | 29 | 4938 | cam_setup.video_speed.fast_motion_without_time_lapse |
| Does the video have a clear subject with back-and-forth changes in shot size? | 29 | 5061 | cam_setup.shot_type.is_just_back_and_forth_change_shot |
| Does the camera only pan rightward without any other camera movements? | 28 | 5294 | cam_motion.camera_centric_movement.pan_right.only_pan_right |
| Is the camera consistently focused on the background using a shallow depth of field? | 28 | 1514 | cam_setup.focus.is_always.focus_is_background |
| Does the camera move only physically upward (not tilting up) relative to the ground (even if it's a bird's or worm's eye view)? | 27 | 5295 | cam_motion.ground_centric_movement.upward.only_upward_wrt_ground_birds_worms_included |
| Does the camera only roll counterclockwise without any other camera movements? | 25 | 5297 | cam_motion.camera_centric_movement.roll_counterclockwise.only_roll_counterclockwise |
| Does the video show a broadcast-style viewpoint used in television production? | 25 | 5065 | cam_setup.point_of_view.broadcast_pov |
| Is this a forward-facing dashcam view from a vehicle-mounted camera, capturing the scene ahead? | 24 | 5066 | cam_setup.point_of_view.dashcam_pov |
| Does the camera’s height relative to the subject start below and end above? | 24 | 3448 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_below_subject_to_above_subject |
| Does the camera use focus tracking to keep a subject in focus in the video? | 24 | 4238 | cam_setup.focus.is_focus_tracking |
| Does the camera only move physically upward (not tilting up) relative to the ground? | 23 | 4261 | cam_motion.ground_centric_movement.upward.only_upward_wrt_ground |
| Is it a rear-side tracking shot where the camera follows the moving subject at a rear-side angle? | 22 | 5064 | cam_motion.object_centric_movement.rear_side_tracking_shot |
| Does the camera transition from underwater to above water? | 22 | 3652 | cam_setup.height_wrt_ground.underwater_to_above_water |
| Does the video start with the camera focused on the middle ground and then shift the focus to the foreground? | 22 | 1480 | cam_setup.focus.from_to.focus_from_middle_ground_to_foreground |
| Does the camera transition from above water to underwater? | 21 | 3653 | cam_setup.height_wrt_ground.above_water_to_underwater |
| Is this a screen recording of a software or system interface (e.g., menus, windows, toolbars)? | 20 | 5070 | cam_setup.point_of_view.screen_recording_pov |
| Does the camera’s height relative to the subject start below and end at the subject’s height? | 20 | 3452 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_below_subject_to_at_subject |
| Does the camera’s height relative to the subject start at the subject’s height and end below? | 20 | 3452 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_at_subject_to_below_subject |
| Does the video end with the camera completely out of focus? | 19 | 1521 | cam_setup.focus.end_with.focus_end_with_out_of_focus |
| Does the camera start in sharp focus and then shift out of focus? | 18 | 5072 | cam_setup.focus.focus_change_from_in_to_out_of_focus |
| Does the video start with the camera focused on the background and then shift the focus to the foreground? | 18 | 1525 | cam_setup.focus.from_to.focus_from_background_to_foreground |
| Does the video start with the camera focused on the foreground and then shift the focus to the background? | 17 | 1521 | cam_setup.focus.from_to.focus_from_foreground_to_background |
| Does the video contain a frame freeze effect at any point? | 14 | 5308 | cam_motion.has_frame_freezing |
| Is the camera craning downward in an arc relative to its own frame? | 14 | 4723 | cam_motion.arc_crane_movement.crane_down.has_crane_down |
| Does the camera’s height relative to the subject start above and end below? | 13 | 3459 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_above_subject_to_below_subject |
| Does the video start with the camera focused on the background and then shift the focus to the middleground? | 8 | 1534 | cam_setup.focus.from_to.focus_from_background_to_middle_ground |
| Does the video start with the camera focused on the middle ground and then shift the focus to the background? | 6 | 1536 | cam_setup.focus.from_to.focus_from_middle_ground_to_background |
| Is the camera consistently out of focus throughout? | 1 | 1541 | cam_setup.focus.is_always.focus_is_out_of_focus |
| Is the scene in the video dynamic and features movement? | 0 | 0 | cam_motion.scene_movement.dynamic_scene |
| Is the scene in the video mostly static with minimal movement? | 0 | 0 | cam_motion.scene_movement.mostly_static_scene |
| Is the scene in the video completely static? | 0 | 0 | cam_motion.scene_movement.static_scene |
| Does the camera move backward (not zooming out) with respect to the initial frame? | 0 | 2047 | cam_motion.camera_centric_movement.backward.has_backward_wrt_camera |
| Does the camera move only physically backward (not zooming out) with respect to the initial frame, without any other movement? | 0 | 5322 | cam_motion.camera_centric_movement.backward.only_backward_wrt_camera |
| Does the camera move physically upward (or pedestals up) with respect to the initial frame? | 0 | 2047 | cam_motion.camera_centric_movement.upward.has_upward_wrt_camera |
| Does the camera only move physically upward (or pedestals up) without any other camera movements? | 0 | 5322 | cam_motion.camera_centric_movement.upward.only_upward_wrt_camera |
| Does the camera only move physically downward (or pedestals down) without any other camera movements? | 0 | 5322 | cam_motion.camera_centric_movement.downward.only_downward_wrt_camera |
| Does the camera move physically downward (or pedestals down) with respect to the initial frame? | 0 | 2047 | cam_motion.camera_centric_movement.downward.has_downward_wrt_camera |
| Does the camera move only physically forward (not zooming in) with respect to the initial frame, without any other movement? | 0 | 5322 | cam_motion.camera_centric_movement.forward.only_forward_wrt_camera |
| Does the camera physically move forward (not zooming in) with respect to the initial frame? | 0 | 2047 | cam_motion.camera_centric_movement.forward.has_forward_wrt_camera |
