# Rare Labels
Labels with less than 30 positive examples
| Definition | Positive Examples | Negative Examples | Label Name |
| --- | --- | --- | --- |
| Is it a fast-motion video with forward playback speed slightly faster than real-time (about 1.5×–3×), but not a time-lapse where the speed is greatly accelerated over a long duration? | 29 | 5388 | cam_setup.video_speed.fast_motion_without_time_lapse |
| Does the video show a broadcast-style viewpoint used in television production? | 26 | 5517 | cam_setup.point_of_view.broadcast_pov |
| Does the camera’s height relative to the subject start at the subject’s height and end below? | 26 | 3814 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_at_subject_to_below_subject |
| Does the video end with the camera completely out of focus? | 26 | 1708 | cam_setup.focus.end_with.focus_end_with_out_of_focus |
| Does the camera start in sharp focus and then shift out of focus? | 25 | 5518 | cam_setup.focus.focus_change_from_in_to_out_of_focus |
| Does the camera use focus tracking to keep a subject in focus in the video? | 25 | 4648 | cam_setup.focus.is_focus_tracking |
| Is this a forward-facing dashcam view from a vehicle-mounted camera, capturing the scene ahead? | 24 | 5519 | cam_setup.point_of_view.dashcam_pov |
| Does the camera’s height relative to the subject start below and end above? | 24 | 3816 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_below_subject_to_above_subject |
| Does the camera transition from underwater to above water? | 23 | 3952 | cam_setup.height_wrt_ground.underwater_to_above_water |
| Does the camera’s height relative to the subject start below and end at the subject’s height? | 22 | 3818 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_below_subject_to_at_subject |
| Does the video start with the camera focused on the middle ground and then shift the focus to the foreground? | 22 | 1673 | cam_setup.focus.from_to.focus_from_middle_ground_to_foreground |
| Does the camera transition from above water to underwater? | 21 | 3954 | cam_setup.height_wrt_ground.above_water_to_underwater |
| Is this a screen recording of a software or system interface (e.g., menus, windows, toolbars)? | 20 | 5523 | cam_setup.point_of_view.screen_recording_pov |
| Does the video start with the camera focused on the background and then shift the focus to the foreground? | 19 | 1718 | cam_setup.focus.from_to.focus_from_background_to_foreground |
| Does the video start with the camera focused on the foreground and then shift the focus to the background? | 18 | 1714 | cam_setup.focus.from_to.focus_from_foreground_to_background |
| Does the camera’s height relative to the subject start above and end below? | 13 | 3827 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_above_subject_to_below_subject |
| Does the video start with the camera focused on the background and then shift the focus to the middleground? | 8 | 1728 | cam_setup.focus.from_to.focus_from_background_to_middle_ground |
| Does the video start with the camera focused on the middle ground and then shift the focus to the background? | 7 | 1729 | cam_setup.focus.from_to.focus_from_middle_ground_to_background |
| Is the camera consistently out of focus throughout? | 1 | 1735 | cam_setup.focus.is_always.focus_is_out_of_focus |
