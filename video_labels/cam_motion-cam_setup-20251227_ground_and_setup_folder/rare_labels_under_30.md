# Rare Labels
Labels with less than 30 positive examples
| Definition | Positive Examples | Negative Examples | Label Name |
| --- | --- | --- | --- |
| Is it a fast-motion video with forward playback speed slightly faster than real-time (about 1.5×–3×), but not a time-lapse where the speed is greatly accelerated over a long duration? | 29 | 5359 | cam_setup.video_speed.fast_motion_without_time_lapse |
| Does the video show a broadcast-style viewpoint used in television production? | 26 | 5487 | cam_setup.point_of_view.broadcast_pov |
| Does the camera’s height relative to the subject start at the subject’s height and end below? | 26 | 3799 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_at_subject_to_below_subject |
| Does the video end with the camera completely out of focus? | 26 | 1708 | cam_setup.focus.end_with.focus_end_with_out_of_focus |
| Does the camera only roll counterclockwise without any other camera movements? | 25 | 5733 | cam_motion.camera_centric_movement.roll_counterclockwise.only_roll_counterclockwise |
| Does the camera start in sharp focus and then shift out of focus? | 25 | 5488 | cam_setup.focus.focus_change_from_in_to_out_of_focus |
| Does the camera use focus tracking to keep a subject in focus in the video? | 25 | 4618 | cam_setup.focus.is_focus_tracking |
| Is it a rear-side tracking shot where the camera follows the moving subject at a rear-side angle? | 24 | 5489 | cam_motion.object_centric_movement.rear_side_tracking_shot |
| Is this a forward-facing dashcam view from a vehicle-mounted camera, capturing the scene ahead? | 24 | 5489 | cam_setup.point_of_view.dashcam_pov |
| Does the camera’s height relative to the subject start below and end above? | 24 | 3801 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_below_subject_to_above_subject |
| Does the camera transition from underwater to above water? | 23 | 3929 | cam_setup.height_wrt_ground.underwater_to_above_water |
| Does the camera’s height relative to the subject start below and end at the subject’s height? | 22 | 3803 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_below_subject_to_at_subject |
| Does the video start with the camera focused on the middle ground and then shift the focus to the foreground? | 22 | 1673 | cam_setup.focus.from_to.focus_from_middle_ground_to_foreground |
| Does the camera transition from above water to underwater? | 21 | 3931 | cam_setup.height_wrt_ground.above_water_to_underwater |
| Is this a screen recording of a software or system interface (e.g., menus, windows, toolbars)? | 20 | 5493 | cam_setup.point_of_view.screen_recording_pov |
| Does the video start with the camera focused on the background and then shift the focus to the foreground? | 19 | 1718 | cam_setup.focus.from_to.focus_from_background_to_foreground |
| Does the video start with the camera focused on the foreground and then shift the focus to the background? | 18 | 1714 | cam_setup.focus.from_to.focus_from_foreground_to_background |
| Does the video contain a frame freeze effect at any point? | 14 | 5744 | cam_motion.has_frame_freezing |
| Is the camera craning downward in an arc relative to its own frame? | 14 | 5118 | cam_motion.arc_crane_movement.crane_down.has_crane_down |
| Does the camera’s height relative to the subject start above and end below? | 13 | 3812 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_above_subject_to_below_subject |
| Does the video start with the camera focused on the background and then shift the focus to the middleground? | 8 | 1728 | cam_setup.focus.from_to.focus_from_background_to_middle_ground |
| Does the video start with the camera focused on the middle ground and then shift the focus to the background? | 7 | 1729 | cam_setup.focus.from_to.focus_from_middle_ground_to_background |
| Is the camera consistently out of focus throughout? | 1 | 1735 | cam_setup.focus.is_always.focus_is_out_of_focus |
| Is the scene in the video dynamic and features movement? | 0 | 0 | cam_motion.scene_movement.dynamic_scene |
| Is the scene in the video mostly static with minimal movement? | 0 | 0 | cam_motion.scene_movement.mostly_static_scene |
| Is the scene in the video completely static? | 0 | 0 | cam_motion.scene_movement.static_scene |
| Does the camera move backward (not zooming out) with respect to the initial frame? | 0 | 2315 | cam_motion.camera_centric_movement.backward.has_backward_wrt_camera |
| Does the camera move only physically backward (not zooming out) with respect to the initial frame, without any other movement? | 0 | 5758 | cam_motion.camera_centric_movement.backward.only_backward_wrt_camera |
| Does the camera move physically upward (or pedestals up) with respect to the initial frame? | 0 | 2315 | cam_motion.camera_centric_movement.upward.has_upward_wrt_camera |
| Does the camera only move physically upward (or pedestals up) without any other camera movements? | 0 | 5758 | cam_motion.camera_centric_movement.upward.only_upward_wrt_camera |
| Does the camera only move physically downward (or pedestals down) without any other camera movements? | 0 | 5758 | cam_motion.camera_centric_movement.downward.only_downward_wrt_camera |
| Does the camera move physically downward (or pedestals down) with respect to the initial frame? | 0 | 2315 | cam_motion.camera_centric_movement.downward.has_downward_wrt_camera |
| Does the camera move only physically forward (not zooming in) with respect to the initial frame, without any other movement? | 0 | 5758 | cam_motion.camera_centric_movement.forward.only_forward_wrt_camera |
| Does the camera physically move forward (not zooming in) with respect to the initial frame? | 0 | 2315 | cam_motion.camera_centric_movement.forward.has_forward_wrt_camera |
