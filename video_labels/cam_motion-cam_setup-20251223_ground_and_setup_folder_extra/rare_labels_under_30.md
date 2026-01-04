# Rare Labels
Labels with less than 30 positive examples
| Definition | Positive Examples | Negative Examples | Label Name |
| --- | --- | --- | --- |
| Is it a follow tracking shot where the camera moves behind the subject, traveling in the same direction as they move away from the camera? | 29 | 395 | cam_motion.object_centric_movement.tail_tracking_shot |
| Does the camera angle decrease noticeably relative to the ground, moving between bird's eye, high angle, level, low angle, or worm's eye view? | 29 | 9 | cam_setup.angle.camera_angle_change_from_high_to_low |
| Does the video feature multiple subjects, but one clearly stands out as the main focus? | 29 | 394 | cam_setup.shot_type.is_just_many_subject_one_focus_shot |
| Does the video start with the camera positioned high at an aerial level? | 29 | 268 | cam_setup.height_wrt_ground.start_with.height_wrt_ground_start_with_aerial_level |
| Does the video show the main subject disappearing or leaving the frame? | 28 | 349 | cam_setup.shot_size.subject_disappearing |
| Does the video end with the camera positioned high at an aerial level? | 28 | 269 | cam_setup.height_wrt_ground.end_with.height_wrt_ground_end_with_aerial_level |
| Is the camera positioned at an aerial level throughout the video? | 28 | 269 | cam_setup.height_wrt_ground.is_always.height_wrt_ground_is_aerial_level |
| Does the camera move backward relative to the scene (backward normally, south from a bird's-eye view, or north from a worm's eye view)? | 27 | 293 | cam_motion.ground_centric_movement.backward.has_backward_wrt_ground_birds_worms_included |
| Is the camera moving physically backward (or dollies out) in the scene? | 27 | 249 | cam_motion.ground_centric_movement.backward.has_backward_wrt_ground |
| Is there an obvious Dutch (canted) angle (more than 15 degrees) that occurs in the video? | 26 | 349 | cam_setup.angle.is_dutch_angle |
| Is this an over-the-hip third-person view, framing the character from the hip up? | 25 | 398 | cam_setup.point_of_view.third_person_over_hip_pov |
| Does the video show scenery or environment without focusing on any subjects? | 25 | 398 | cam_setup.shot_type.is_just_scenery_shot |
| Does the video end with the camera at an overhead level, above eye level but below aerial (around second-floor height)? | 25 | 272 | cam_setup.height_wrt_ground.end_with.height_wrt_ground_end_with_overhead_level |
| Is it an arc tracking shot where the camera follows the moving subject while arcing around them? | 24 | 403 | cam_motion.object_centric_movement.arc_tracking_shot |
| Does the camera pan to the left? | 23 | 273 | cam_motion.camera_centric_movement.pan_left.has_pan_left |
| Does the video start with the camera at ground level, positioned close to the ground? | 23 | 274 | cam_setup.height_wrt_ground.start_with.height_wrt_ground_start_with_ground_level |
| Is the camera motion minimal, hard to discern, or very subtle? | 22 | 339 | cam_motion.motion_complexity.is_minor_motion |
| Does the camera only tilt upward without any other camera movements? | 22 | 414 | cam_motion.camera_centric_movement.tilt_up.only_tilt_up |
| Does the video end with the camera at ground level, positioned close to the ground? | 22 | 275 | cam_setup.height_wrt_ground.end_with.height_wrt_ground_end_with_ground_level |
| Does the video start with the camera at hip level, roughly between knee and waist height, whether or not a human subject is present? | 22 | 275 | cam_setup.height_wrt_ground.start_with.height_wrt_ground_start_with_hip_level |
| Does the video begin with the camera at an overhead level, above eye level but below aerial (around second-floor height)? | 22 | 275 | cam_setup.height_wrt_ground.start_with.height_wrt_ground_start_with_overhead_level |
| Does the video end with the camera at hip level, roughly between knee and waist height, whether or not a human subject is present? | 21 | 276 | cam_setup.height_wrt_ground.end_with.height_wrt_ground_end_with_hip_level |
| Is the camera positioned at an overhead level throughout the video, above eye level but below aerial (around second-floor height)? | 21 | 276 | cam_setup.height_wrt_ground.is_always.height_wrt_ground_is_overhead_level |
| Does the camera only zoom in with no other movement? | 20 | 416 | cam_motion.camera_centric_movement.zoom_in.only_zoom_in |
| Does the video start with an extreme wide shot that emphasizes the vast environment over any subjects? | 19 | 338 | cam_setup.shot_size.start_with.shot_size_start_with_extreme_wide |
| Does the video start with a medium-full shot that frames the human subject from mid-thigh (or knee) upward? | 19 | 338 | cam_setup.shot_size.start_with.shot_size_start_with_medium_full |
| Is the camera positioned at ground level throughout the video, positioned close to the ground? | 19 | 278 | cam_setup.height_wrt_ground.is_always.height_wrt_ground_is_ground_level |
| Is the camera positioned at hip level throughout the video, roughly between knee and waist height, whether or not a human subject is present? | 19 | 278 | cam_setup.height_wrt_ground.is_always.height_wrt_ground_is_hip_level |
| Does the video feature a clear subject whose anatomy looks unnatural or exaggerated compared to real-world counterparts, making the exact shot size difficult to classify? | 18 | 405 | cam_setup.shot_type.is_just_clear_subject_atypical_shot |
| Does the video feature multiple subjects in focus, with no single subject standing out as dominant? | 18 | 405 | cam_setup.shot_type.is_just_many_subject_no_focus_shot |
| Does the camera move physically upward (or pedestals up) relative to the ground (even if it's a bird's or worm's eye view)? | 17 | 270 | cam_motion.ground_centric_movement.upward.has_upward_wrt_ground_birds_worms_included |
| Does the degree of the Dutch (canted) angle stay the same throughout the video? | 17 | 358 | cam_setup.angle.is_dutch_angle_fixed |
| Does the video end with a medium full shot that frames the human subject from the mid-thigh (or knee) upward? | 17 | 315 | cam_setup.shot_size.end_with.shot_size_end_with_medium_full |
| Does the video start with a medium close-up shot that frames the human subject from the chest upward? | 17 | 340 | cam_setup.shot_size.start_with.shot_size_start_with_medium_close_up |
| Does the camera move in a counterclockwise arc? | 16 | 410 | cam_motion.arc_crane_movement.arc_counterclockwise.has_arc_counterclockwise |
| Does the camera zoom out? | 16 | 277 | cam_motion.camera_centric_movement.zoom_out.has_zoom_out |
| Does the video start with the camera positioned below the subject? | 16 | 338 | cam_setup.height_wrt_subject.start_with.height_wrt_subject_start_with_below_subject |
| Does the camera move in a clockwise arc? | 15 | 411 | cam_motion.arc_crane_movement.arc_clockwise.has_arc_clockwise |
| Does the camera move physically upward (or pedestals up) relative to the ground? | 15 | 226 | cam_motion.ground_centric_movement.upward.has_upward_wrt_ground |
| Does the video end with a medium close-up shot that frames the human subject from the chest upward? | 15 | 317 | cam_setup.shot_size.end_with.shot_size_end_with_medium_close_up |
| Does the video end with the camera positioned below the subject? | 15 | 339 | cam_setup.height_wrt_subject.end_with.height_wrt_subject_end_with_below_subject |
| Does the shot feature a dolly zoom effect with the camera moving forward and zooming out? | 14 | 422 | cam_motion.dolly_zoom_movement.has_dolly_in_zoom_out |
| Does the camera move physically downward relative to the ground (even if it's a bird's or worm's eye view)? | 14 | 273 | cam_motion.ground_centric_movement.downward.has_downward_wrt_ground_birds_worms_included |
| Does the camera pan to the right? | 14 | 279 | cam_motion.camera_centric_movement.pan_right.has_pan_right |
| Is there a mismatch between the subject and scene framing that makes it hard to classify the shot size? | 14 | 409 | cam_setup.shot_type.is_just_subject_scene_mismatch_shot |
| Does the camera move physically leftward (or trucks left)? | 13 | 269 | cam_motion.camera_centric_movement.leftward.has_leftward |
| Does the video include a shot transition? | 13 | 423 | cam_setup.has_shot_transition_cam_setup |
| Does the video end with an extreme wide shot, emphasizing the vast environment over any subjects? | 13 | 319 | cam_setup.shot_size.end_with.shot_size_end_with_extreme_wide |
| Does the camera's height relative to the subject change significantly, moving between positions above, at level with, or below the subject? | 13 | 302 | cam_setup.height_wrt_subject.height_wrt_subject_change |
| Does the camera move physically downward (or pedestals down) relative to the ground? | 12 | 230 | cam_motion.ground_centric_movement.downward.has_downward_wrt_ground |
| Does the camera move physically rightward (or trucks right)? | 12 | 272 | cam_motion.camera_centric_movement.rightward.has_rightward |
| Does the video start with the camera at a high angle and transition to a level angle? | 12 | 363 | cam_setup.angle.from_to.camera_angle_from_high_to_level |
| Does the video maintain a medium close-up shot throughout, consistently framing the human subject from the chest upward? | 12 | 348 | cam_setup.shot_size.is_always.shot_size_is_medium_close_up |
| Does the video maintain an extreme wide shot throughout, consistently emphasizing the vast environment over any subjects? | 12 | 347 | cam_setup.shot_size.is_always.shot_size_is_extreme_wide |
| Does the video maintain a medium full shot throughout, consistently framing the human subject from mid-thigh (or knee) upward? | 12 | 347 | cam_setup.shot_size.is_always.shot_size_is_medium_full |
| Is it a side tracking shot with the camera moving from the side to follow the moving subject? | 11 | 412 | cam_motion.object_centric_movement.side_tracking_shot |
| Does the camera have noticeable motion at a fast speed? | 11 | 361 | cam_motion.steadiness_and_movement.fast_moving_camera |
| Does the video start with the camera at a level angle and transition to a low angle? | 11 | 364 | cam_setup.angle.from_to.camera_angle_from_level_to_low |
| Does the camera tilt to track the moving subjects? | 10 | 417 | cam_motion.object_centric_movement.tilt_tracking_shot |
| Is it an aerial tracking shot where the camera follows the moving subject from an aerial view? | 10 | 417 | cam_motion.object_centric_movement.aerial_tracking_shot |
| Does the subject appear larger during the tracking shot? | 10 | 417 | cam_motion.object_centric_movement.tracking_subject_larger_size |
| Does the camera pan to track the moving subjects? | 10 | 415 | cam_motion.object_centric_movement.pan_tracking_shot |
| Does the camera move only forward (not zooming in) in the scene, or only northward in a bird's eye view, or only southward in a worm's eye view? | 10 | 426 | cam_motion.ground_centric_movement.forward.only_forward_wrt_ground_birds_worms_included |
| Does the camera only move physically forward (not zooming in) relative to the ground? | 10 | 357 | cam_motion.ground_centric_movement.forward.only_forward_wrt_ground |
| Does the camera have noticeable motion but at a slow motion speed? | 10 | 362 | cam_motion.steadiness_and_movement.slow_moving_camera |
| Is it a first-person POV shot, filmed as if seen directly through the character’s eyes? | 10 | 413 | cam_setup.point_of_view.first_person_pov |
| Does the camera height increase noticeably in relation to the ground, shifting between levels like aerial, overhead, eye, hip, or ground? | 10 | 7 | cam_setup.height_wrt_ground.height_wrt_ground_change_from_low_to_high |
| Does the video include a shot transition? | 9 | 427 | cam_motion.has_shot_transition_cam_motion |
| Does the camera only move physically upward (not tilting up) relative to the ground? | 9 | 358 | cam_motion.ground_centric_movement.upward.only_upward_wrt_ground |
| Does the camera move only physically upward (not tilting up) relative to the ground (even if it's a bird's or worm's eye view)? | 9 | 427 | cam_motion.ground_centric_movement.upward.only_upward_wrt_ground_birds_worms_included |
| Does the camera angle increase noticeably relative to the ground, moving between worm's eye, low angle, level, high angle, or bird's eye view? | 9 | 29 | cam_setup.angle.camera_angle_change_from_low_to_high |
| Does the degree of the Dutch (canted) angle vary during the video? | 9 | 366 | cam_setup.angle.is_dutch_angle_varying |
| Is it a slow-motion video with forward playback slower than real-time? | 9 | 412 | cam_setup.video_speed.slow_motion |
| Is the camera positioned below the subject throughout the video? | 9 | 345 | cam_setup.height_wrt_subject.is_always.height_wrt_subject_is_below_subject |
| Does the main subject change to another subject? | 8 | 369 | cam_setup.shot_size.subject_switching |
| Does the subject start above and end at or below the camera’s height, or start level and end below? | 8 | 5 | cam_setup.height_wrt_subject.height_wrt_subject_change_from_high_to_low |
| Does the video start with the camera fully submerged underwater? | 8 | 289 | cam_setup.height_wrt_ground.start_with.height_wrt_ground_start_with_underwater_level |
| Does the camera tilt downward? | 7 | 277 | cam_motion.camera_centric_movement.tilt_down.has_tilt_down |
| Does the video start with the camera at a bird's eye angle, looking straight down from above? | 7 | 368 | cam_setup.angle.start_with.camera_angle_start_with_bird_eye_angle |
| Does the shot size change noticeably from a tighter to a wider framing? | 7 | 370 | cam_setup.shot_size.shot_size_change_from_small_to_large |
| Does the camera height decrease noticeably in relation to the ground, shifting between levels like aerial, overhead, eye, hip, or ground? | 7 | 10 | cam_setup.height_wrt_ground.height_wrt_ground_change_from_high_to_low |
| Does the video end with the camera fully submerged underwater? | 7 | 290 | cam_setup.height_wrt_ground.end_with.height_wrt_ground_end_with_underwater_level |
| Is the camera fully submerged underwater throughout the video, capturing scenes beneath the water’s surface? | 7 | 290 | cam_setup.height_wrt_ground.is_always.height_wrt_ground_is_underwater_level |
| Is it a lead tracking shot where the camera moves ahead of the subject, traveling in the same direction as they approach the camera? | 6 | 420 | cam_motion.object_centric_movement.lead_tracking_shot |
| Does the video end with the camera at a bird's eye angle, looking straight down from above? | 6 | 369 | cam_setup.angle.end_with.camera_angle_end_with_bird_eye_angle |
| Does the video start with the camera at a level angle and transition to a high angle? | 6 | 369 | cam_setup.angle.from_to.camera_angle_from_level_to_high |
| Does the camera maintain a bird's eye angle throughout, consistently looking straight down from above? | 6 | 369 | cam_setup.angle.is_always.camera_angle_is_bird_eye_angle |
| Does the video show mild barrel distortion or extreme fisheye distortion, where lines, especially near the frame edges, bend outward? | 6 | 417 | cam_setup.lens_distortion.with_lens_distortion |
| Does the camera’s height relative to the subject start at the subject’s height and end below? | 6 | 348 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_at_subject_to_below_subject |
| Does the video end with the camera near water level, showing the waterline clearly and not from an aerial view? | 6 | 291 | cam_setup.height_wrt_ground.end_with.height_wrt_ground_end_with_water_level |
| Does the camera use rack focus or pull focus to shift the focus plane? | 6 | 374 | cam_setup.focus.is_rack_pull_focus |
| Does the camera start in sharp focus and then shift out of focus? | 6 | 417 | cam_setup.focus.focus_change_from_in_to_out_of_focus |
| Does the video end with the camera completely out of focus? | 6 | 192 | cam_setup.focus.end_with.focus_end_with_out_of_focus |
| Does the subject appear smaller during the tracking shot? | 5 | 422 | cam_motion.object_centric_movement.tracking_subject_smaller_size |
| Is it a side tracking shot where the camera moves right to follow the subject? | 5 | 422 | cam_motion.object_centric_movement.side_tracking_shot_rightward |
| Does the shot feature a dolly zoom effect with the camera moving backward and zooming in? | 5 | 431 | cam_motion.dolly_zoom_movement.has_dolly_out_zoom_in |
| Does the camera move only physically downward (not tilting down) relative to the ground (even if it's a bird's or worm's eye view)? | 5 | 431 | cam_motion.ground_centric_movement.downward.only_downward_wrt_ground_birds_worms_included |
| Does the camera show noticable vibrations, shaking, or wobbling? | 5 | 359 | cam_motion.steadiness_and_movement.very_shaky_camera |
| Does the camera only move laterally rightward with no other movement? | 5 | 431 | cam_motion.camera_centric_movement.rightward.only_rightward |
| Does this shot contain noticeable yet slight barrel distortion? | 5 | 418 | cam_setup.lens_distortion.barrel_distortion |
| Does the subject start below and end at or above the camera’s height, or start level and end above? | 5 | 8 | cam_setup.height_wrt_subject.height_wrt_subject_change_from_low_to_high |
| Does the video end with the camera focusing on the background, using a shallow depth of field? | 5 | 193 | cam_setup.focus.end_with.focus_end_with_background |
| Does the camera move only backward (not zooming out) in the scene, or only southward in a bird's eye view, or only northward in a worm's eye view? | 4 | 432 | cam_motion.ground_centric_movement.backward.only_backward_wrt_ground_birds_worms_included |
| Does the camera only move physically backward (not zooming out) with respect to the ground? | 4 | 363 | cam_motion.ground_centric_movement.backward.only_backward_wrt_ground |
| Does the camera only move physically downward (not tilting down) with respect to the ground? | 4 | 363 | cam_motion.ground_centric_movement.downward.only_downward_wrt_ground |
| Does the camera only pan leftward without any other camera movements? | 4 | 432 | cam_motion.camera_centric_movement.pan_left.only_pan_left |
| Does the camera only move laterally leftward without any other camera movements? | 4 | 432 | cam_motion.camera_centric_movement.leftward.only_leftward |
| Does the video end with the camera at a worm's eye angle, looking straight up from below? | 4 | 371 | cam_setup.angle.end_with.camera_angle_end_with_worm_eye_angle |
| Does the camera’s height relative to the subject start above and end at the subject’s height? | 4 | 350 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_above_subject_to_at_subject |
| Is the camera positioned at water level throughout the video, above the water surface with the waterline clearly visible? | 4 | 293 | cam_setup.height_wrt_ground.is_always.height_wrt_ground_is_water_level |
| Does the video start with the camera near water level, showing the waterline clearly and not from an aerial view? | 4 | 293 | cam_setup.height_wrt_ground.start_with.height_wrt_ground_start_with_water_level |
| Does the video start with the camera focusing on the background, using a shallow depth of field? | 4 | 194 | cam_setup.focus.start_with.focus_start_with_background |
| Is it a side tracking shot where the camera moves left to follow the subject? | 3 | 424 | cam_motion.object_centric_movement.side_tracking_shot_leftward |
| Does the video start with the camera at a low angle and transition to a level angle? | 3 | 372 | cam_setup.angle.from_to.camera_angle_from_low_to_level |
| Is it a revealing shot where the subject comes into view on screen? | 3 | 374 | cam_setup.shot_size.subject_revealing |
| Does the camera’s height relative to the subject start at the subject’s height and end above? | 3 | 351 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_at_subject_to_above_subject |
| Does the focal plane shift noticeably between foreground, middleground, or background regions? | 3 | 332 | cam_setup.focus.focus_change |
| Is the camera consistently focused on the background using a shallow depth of field? | 3 | 195 | cam_setup.focus.is_always.focus_is_background |
| Is it a rear-side tracking shot where the camera follows the moving subject at a rear-side angle? | 2 | 425 | cam_motion.object_centric_movement.rear_side_tracking_shot |
| Does the video start with the camera at a high angle and transition to a low angle? | 2 | 373 | cam_setup.angle.from_to.camera_angle_from_high_to_low |
| Does the video show a speed ramp effect, where playback speed changes between faster and slower rates? | 2 | 421 | cam_setup.video_speed.speed_ramp |
| Is this a side-view gaming video where the camera is placed to the side, capturing the scene or character in profile? | 2 | 421 | cam_setup.point_of_view.third_person_side_view_game_pov |
| Is this an over-the-shoulder POV where the camera is positioned behind the character, showing their upper body and the scene ahead? | 2 | 421 | cam_setup.point_of_view.third_person_over_shoulder_pov |
| Does the video have a clear subject with back-and-forth changes in shot size? | 2 | 421 | cam_setup.shot_type.is_just_back_and_forth_change_shot |
| Does the camera’s height relative to the subject start below and end at the subject’s height? | 2 | 352 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_below_subject_to_at_subject |
| Does the focal plane shift from close to distant, moving between foreground, middleground, or background? | 2 | 333 | cam_setup.focus.focus_change_from_near_to_far |
| Does the video contain noticeable motion blur? | 1 | 435 | cam_motion.has_motion_blur |
| Is it a front-side tracking shot where the camera leads the moving subject from a front-side angle? | 1 | 426 | cam_motion.object_centric_movement.front_side_tracking_shot |
| Is the camera craning upward in an arc relative to its own frame? | 1 | 395 | cam_motion.arc_crane_movement.crane_up.has_crane_up |
| Does the camera roll counterclockwise? | 1 | 271 | cam_motion.camera_centric_movement.roll_counterclockwise.has_roll_counterclockwise |
| Does the camera roll clockwise? | 1 | 271 | cam_motion.camera_centric_movement.roll_clockwise.has_roll_clockwise |
| Does the camera only pan rightward without any other camera movements? | 1 | 435 | cam_motion.camera_centric_movement.pan_right.only_pan_right |
| Does the camera only zoom out with no other movement? | 1 | 435 | cam_motion.camera_centric_movement.zoom_out.only_zoom_out |
| Does the camera maintain a worm's eye angle throughout, consistently looking straight up from below? | 1 | 374 | cam_setup.angle.is_always.camera_angle_is_worm_eye_angle |
| Does the video start with the camera at a worm’s eye angle, looking straight up from below? | 1 | 374 | cam_setup.angle.start_with.camera_angle_start_with_worm_eye_angle |
| Does the video show extreme fisheye lens distortion, where most lines curve strongly outward? | 1 | 422 | cam_setup.lens_distortion.fisheye_distortion |
| Is it a selfie POV shot where the camera is held by the person being filmed (e.g., by hand, selfie stick, or invisible selfie rod) and faces them? | 1 | 422 | cam_setup.point_of_view.selfie_pov |
| Is this a 3D gaming video featuring a third-person perspective with the character’s full body visible? | 1 | 422 | cam_setup.point_of_view.third_person_full_body_game_pov |
| Does the video show a broadcast-style viewpoint used in television production? | 1 | 422 | cam_setup.point_of_view.broadcast_pov |
| Is this a gaming video with a top-down or oblique top-down view, where the camera is placed directly above the character and environment, looking downward to show mostly the tops of objects with limited sides? | 1 | 422 | cam_setup.point_of_view.third_person_top_down_game_pov |
| Does the camera transition from underwater to above water? | 1 | 278 | cam_setup.height_wrt_ground.underwater_to_above_water |
| Does the camera start out of focus and then become in focus? | 1 | 422 | cam_setup.focus.focus_change_from_out_to_in_focus |
| Does the focal plane shift from distant to close, moving between foreground, middleground, or background? | 1 | 334 | cam_setup.focus.focus_change_from_far_to_near |
| Does the camera use focus tracking to keep a subject in focus in the video? | 1 | 379 | cam_setup.focus.is_focus_tracking |
| Does the video start with the camera focused on the background and then shift the focus to the foreground? | 1 | 197 | cam_setup.focus.from_to.focus_from_background_to_foreground |
| Does the video start with the camera focused on the foreground and then shift the focus to the background? | 1 | 197 | cam_setup.focus.from_to.focus_from_foreground_to_background |
| Does the video start with the camera focused on the middle ground and then shift the focus to the background? | 1 | 197 | cam_setup.focus.from_to.focus_from_middle_ground_to_background |
| Does the video start with the camera completely out of focus? | 1 | 197 | cam_setup.focus.start_with.focus_start_with_out_of_focus |
| Does the video contain a frame freeze effect at any point? | 0 | 436 | cam_motion.has_frame_freezing |
| Is the camera craning downward in an arc relative to its own frame? | 0 | 396 | cam_motion.arc_crane_movement.crane_down.has_crane_down |
| Is the scene in the video dynamic and features movement? | 0 | 0 | cam_motion.scene_movement.dynamic_scene |
| Is the scene in the video mostly static with minimal movement? | 0 | 0 | cam_motion.scene_movement.mostly_static_scene |
| Is the scene in the video completely static? | 0 | 0 | cam_motion.scene_movement.static_scene |
| Does the camera move backward (not zooming out) with respect to the initial frame? | 0 | 272 | cam_motion.camera_centric_movement.backward.has_backward_wrt_camera |
| Does the camera move only physically backward (not zooming out) with respect to the initial frame, without any other movement? | 0 | 436 | cam_motion.camera_centric_movement.backward.only_backward_wrt_camera |
| Does the camera only tilt downward without any other camera movements? | 0 | 436 | cam_motion.camera_centric_movement.tilt_down.only_tilt_down |
| Does the camera move physically upward (or pedestals up) with respect to the initial frame? | 0 | 272 | cam_motion.camera_centric_movement.upward.has_upward_wrt_camera |
| Does the camera only move physically upward (or pedestals up) without any other camera movements? | 0 | 436 | cam_motion.camera_centric_movement.upward.only_upward_wrt_camera |
| Does the camera only roll counterclockwise without any other camera movements? | 0 | 436 | cam_motion.camera_centric_movement.roll_counterclockwise.only_roll_counterclockwise |
| Does the camera only move physically downward (or pedestals down) without any other camera movements? | 0 | 436 | cam_motion.camera_centric_movement.downward.only_downward_wrt_camera |
| Does the camera move physically downward (or pedestals down) with respect to the initial frame? | 0 | 272 | cam_motion.camera_centric_movement.downward.has_downward_wrt_camera |
| Does the camera only roll clockwise without any other camera movements? | 0 | 436 | cam_motion.camera_centric_movement.roll_clockwise.only_roll_clockwise |
| Does the camera move only physically forward (not zooming in) with respect to the initial frame, without any other movement? | 0 | 436 | cam_motion.camera_centric_movement.forward.only_forward_wrt_camera |
| Does the camera physically move forward (not zooming in) with respect to the initial frame? | 0 | 272 | cam_motion.camera_centric_movement.forward.has_forward_wrt_camera |
| Does the video start with the camera at a low angle and transition to a high angle? | 0 | 375 | cam_setup.angle.from_to.camera_angle_from_low_to_high |
| Is it a fast-motion video with forward playback moderately faster than real-time (about 1.5×–3×)? | 0 | 421 | cam_setup.video_speed.fast_motion |
| Is it a fast-motion video with forward playback speed slightly faster than real-time (about 1.5×–3×), but not a time-lapse where the speed is greatly accelerated over a long duration? | 0 | 421 | cam_setup.video_speed.fast_motion_without_time_lapse |
| Is this a time-lapse video played forward at greatly accelerated speed (more than 3× real-time), showing time passing rapidly over a long period? | 0 | 421 | cam_setup.video_speed.time_lapse |
| Is the camera positioned directly above the subject for a top-down perspective? | 0 | 423 | cam_setup.point_of_view.overhead_pov |
| Is this a screen recording of a software or system interface (e.g., menus, windows, toolbars)? | 0 | 423 | cam_setup.point_of_view.screen_recording_pov |
| Is the camera physically mounted on an object, keeping its perspective locked to that object? | 0 | 423 | cam_setup.point_of_view.locked_on_pov |
| Is this a third-person isometric (2.5D) gaming video with a tilted overhead angle showing both the top and side planes of the environment in a three-quarters perspective, with minimal perspective distortion? | 0 | 423 | cam_setup.point_of_view.third_person_isometric_game_pov |
| Is this a forward-facing dashcam view from a vehicle-mounted camera, capturing the scene ahead? | 0 | 423 | cam_setup.point_of_view.dashcam_pov |
| Is there a clear subject, but the framing is unstable, making the exact shot size difficult to classify? | 0 | 423 | cam_setup.shot_type.is_just_clear_subject_dynamic_size_shot |
| Does the camera’s height relative to the subject start below and end above? | 0 | 354 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_below_subject_to_above_subject |
| Does the camera’s height relative to the subject start above and end below? | 0 | 354 | cam_setup.height_wrt_subject.from_to.height_wrt_subject_from_above_subject_to_below_subject |
| Does the camera transition from above water to underwater? | 0 | 279 | cam_setup.height_wrt_ground.above_water_to_underwater |
| Does the video start with the camera focused on the background and then shift the focus to the middleground? | 0 | 198 | cam_setup.focus.from_to.focus_from_background_to_middle_ground |
| Does the video start with the camera focused on the foreground and then shift the focus to the middleground? | 0 | 196 | cam_setup.focus.from_to.focus_from_foreground_to_middle_ground |
| Does the video start with the camera focused on the middle ground and then shift the focus to the foreground? | 0 | 196 | cam_setup.focus.from_to.focus_from_middle_ground_to_foreground |
| Is the camera consistently out of focus throughout? | 0 | 198 | cam_setup.focus.is_always.focus_is_out_of_focus |
