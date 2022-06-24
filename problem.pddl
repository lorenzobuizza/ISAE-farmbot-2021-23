(define
	(problem motionandpicture)
	(:domain farmbot)
	(:objects
		camera - camera
		robot - robot
		A B C D E F G H I - sample
		seedbin - seedbin
		seedinj - seedinjector
		seed1 seed2 seed3 - seed
		soilsensor - soilsensor
		wateringnozzle - wateringnozzle
		a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12 a13 a14 a15 a16 a17 b0 b1 b2 b3 b4 b5 b6 - waypoint
		weeder - weeder
		weed1 weed2 - weed
	)
	(:init (at robot b6) (soilsensor-at soilsensor b0) (seedinj-at seedinj b3) (weeder-at weeder b2) (waternozzle-at wateringnozzle b1) (seedbin-at seedbin b5) (seed-at seed1 b5) (seed-at seed2 b5) (seed-at seed3 b5) (is-in A a1) (is-in B a3) (is-in C a4) (is-in D a5) (is-in E a7) (is-in F a8) (is-in G a11) (is-in H a14) (is-in I a15) (is weed1 a6) (is weed2 a10) (empty-wayp a0) (empty-wayp a2) (empty-wayp a9) (empty-wayp a13) (empty-wayp a16) (empty-wayp a17) (no-tools-mounted robot) (not (carrying-seed robot)))
	(:goal (and (at robot b6) (no-tools-mounted robot) (taken-image A) (taken-image B) (taken-image C) (taken-image D) (taken-image E) (taken-image F) (taken-image G) (taken-image H) (taken-image I) (taken-data-before-water A) (taken-data-before-water B) (taken-data-before-water C) (taken-data-before-water D) (taken-data-before-water E) (taken-data-before-water F) (taken-data-before-water G) (taken-data-before-water H) (taken-data-before-water I) (samplewatered A) (samplewatered B) (samplewatered C) (samplewatered D) (samplewatered E) (samplewatered F) (samplewatered G) (samplewatered H) (samplewatered I) (taken-data-after-water A) (taken-data-after-water B) (taken-data-after-water C) (taken-data-after-water D) (taken-data-after-water E) (taken-data-after-water F) (taken-data-after-water G) (taken-data-after-water H) (taken-data-after-water I) (seedinjected seed1 a13) (seedinjected seed2 a16) (seedinjected seed3 a9) (wayp-without-weed a6 weed1) (wayp-without-weed a10 weed2)))
)
