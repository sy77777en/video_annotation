# Rare Labels
Labels with less than 30 positive examples
| Definition | Positive Examples | Negative Examples | Label Name |
| --- | --- | --- | --- |
| Does the video show a broadcast-style viewpoint used in television production? | 27 | 5200 | cam_setup.point_of_view.broadcast_pov |
| Is this a forward-facing dashcam view from a vehicle-mounted camera, capturing the scene ahead? | 27 | 5200 | cam_setup.point_of_view.dashcam_pov |
| Does the camera use focus tracking to keep a subject in focus in the video? | 27 | 4356 | cam_setup.focus.is_focus_tracking |
| Does the camera’s height relative to the subject start below and end at the subject’s height? | 24 | 3539 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_below_subject_to_at_subject |
| Does the camera’s height relative to the subject start below and end above? | 24 | 3539 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_below_subject_to_above_subject |
| Does the camera’s height relative to the subject start at the subject’s height and end below? | 22 | 3541 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_at_subject_to_below_subject |
| Does the camera transition from underwater to above water? | 22 | 3752 | cam_setup.height_wrt_ground.underwater_to_above_water |
| Does the video end with the camera completely out of focus? | 22 | 1570 | cam_setup.focus.end_with.focus_end_with_out_of_focus |
| Does the camera transition from above water to underwater? | 21 | 3753 | cam_setup.height_wrt_ground.above_water_to_underwater |
| Does the camera start in sharp focus and then shift out of focus? | 21 | 5206 | cam_setup.focus.focus_change_from_in_to_out_of_focus |
| Does the video start with the camera focused on the middle ground and then shift the focus to the foreground? | 21 | 1532 | cam_setup.focus.from_to.focus_from_middle_ground_to_foreground |
| Is this a screen recording of a software or system interface (e.g., menus, windows, toolbars)? | 20 | 5207 | cam_setup.point_of_view.screen_recording_pov |
| Does the video start with the camera focused on the background and then shift the focus to the foreground? | 18 | 1577 | cam_setup.focus.from_to.focus_from_background_to_foreground |
| Does the video start with the camera focused on the foreground and then shift the focus to the background? | 18 | 1571 | cam_setup.focus.from_to.focus_from_foreground_to_background |
| Does the camera’s height relative to the subject start above and end below? | 13 | 3550 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_above_subject_to_below_subject |
| Does the video start with the camera focused on the background and then shift the focus to the middleground? | 7 | 1587 | cam_setup.focus.from_to.focus_from_background_to_middle_ground |
| Does the video start with the camera focused on the middle ground and then shift the focus to the background? | 7 | 1588 | cam_setup.focus.from_to.focus_from_middle_ground_to_background |
| Is the camera consistently out of focus throughout? | 1 | 1593 | cam_setup.focus.is_always.focus_is_out_of_focus |
