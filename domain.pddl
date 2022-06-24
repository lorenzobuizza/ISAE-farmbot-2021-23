(define
	(domain farmbot)
	(:requirements :strips :typing)
	(:types
		camera
		robot
		sample
		seed
		seedbin
		seedinj
		soilsensor
		wateringnozzle
		waypoint
		weed
		weeder
	)
	(:predicates
		(at ?r - robot ?wp - waypoint)
		(carrying-SeedInj ?sinj - seedinjector)
		(carrying-SoilSensor ?ss - soilsensor)
		(carrying-WateringNozzle ?wn - wateringnozzle)
		(carrying-Weeder ?wdr - weeder)
		(carrying-seed ?r - robot)
		(empty-wayp ?wp - waypoint)
		(is ?weed - weed ?wp - waypoint)
		(is-in ?s - sample ?wp - waypoint)
		(no-tools-mounted ?r - robot)
		(samplewatered ?s - sample)
		(seed-at ?seed - seed ?wp - waypoint)
		(seedbin-at ?sb - seedbin ?wp - waypoint)
		(seedinj-at ?sinj - seedinjector ?wp - waypoint)
		(seedinjected ?seed - seed ?wp - waypoint)
		(soilsensor-at ?ss - soilsensor ?wp - waypoint)
		(taken-data-after-water ?s - sample)
		(taken-data-before-water ?s - sample)
		(taken-image ?s - sample)
		(waternozzle-at ?wn - wateringnozzle ?wp - waypoint)
		(wayp-without-weed ?wp - waypoint ?weed - weed)
		(weeder-at ?wdr - weeder ?wp - waypoint)
	)
	(:action dismount-seed-injector
		:parameters (?wp - waypoint ?r - robot ?sinj - seedinjector)
		:precondition (and (seedinj-at ?sinj ?wp) (at ?r ?wp) (carrying-SeedInj ?sinj) (not (no-tools-mounted ?r)) (not (carrying-seed ?r)))
		:effect (and (not (carrying-SeedInj ?sinj)) (no-tools-mounted ?r))
	)
	(:action dismount-soilsensor
		:parameters (?wp - waypoint ?r - robot ?ss - soilsensor)
		:precondition (and (soilsensor-at ?ss ?wp) (at ?r ?wp) (carrying-SoilSensor ?ss) (not (no-tools-mounted ?r)))
		:effect (and (not (carrying-SoilSensor ?ss)) (no-tools-mounted ?r))
	)
	(:action dismount-waternozzle
		:parameters (?wp - waypoint ?r - robot ?wn - wateringnozzle)
		:precondition (and (waternozzle-at ?wn ?wp) (at ?r ?wp) (carrying-WateringNozzle ?wn) (not (no-tools-mounted ?r)))
		:effect (and (not (carrying-WateringNozzle ?wn)) (no-tools-mounted ?r))
	)
	(:action dismount-weeder
		:parameters (?wp - waypoint ?r - robot ?wdr - weeder)
		:precondition (and (weeder-at ?wdr ?wp) (at ?r ?wp) (carrying-Weeder ?wdr) (not (no-tools-mounted ?r)))
		:effect (and (not (carrying-Weeder ?wdr)) (no-tools-mounted ?r))
	)
	(:action eliminate-weed
		:parameters (?wp - waypoint ?r - robot ?wdr - weeder ?weed - weed)
		:precondition (and (is ?weed ?wp) (at ?r ?wp) (carrying-Weeder ?wdr))
		:effect (and (not (is ?weed ?wp)) (wayp-without-weed ?wp ?weed))
	)
	(:action grab-seed
		:parameters (?seed - seed ?wp - waypoint ?r - robot ?sinj - seedinjector)
		:precondition (and (seed-at ?seed ?wp) (at ?r ?wp) (carrying-SeedInj ?sinj) (not (carrying-seed ?r)))
		:effect (carrying-seed ?r)
	)
	(:action inject-seed
		:parameters (?seed - seed ?wp - waypoint ?r - robot ?sinj - seedinjector)
		:precondition (and (empty-wayp ?wp) (at ?r ?wp) (carrying-SeedInj ?sinj) (carrying-seed ?r))
		:effect (and (seedinjected ?seed ?wp) (not (empty-wayp ?wp)) (not (carrying-seed ?r)))
	)
	(:action irrigate
		:parameters (?s - sample ?wp - waypoint ?r - robot ?wn - wateringnozzle)
		:precondition (and (is-in ?s ?wp) (at ?r ?wp) (carrying-WateringNozzle ?wn))
		:effect (samplewatered ?s)
	)
	(:action mount-seed-injector
		:parameters (?wp - waypoint ?r - robot ?sinj - seedinjector)
		:precondition (and (seedinj-at ?sinj ?wp) (at ?r ?wp) (no-tools-mounted ?r))
		:effect (and (carrying-SeedInj ?sinj) (not (no-tools-mounted ?r)))
	)
	(:action mount-soilsensor
		:parameters (?wp - waypoint ?r - robot ?ss - soilsensor)
		:precondition (and (soilsensor-at ?ss ?wp) (at ?r ?wp) (no-tools-mounted ?r))
		:effect (and (carrying-SoilSensor ?ss) (not (no-tools-mounted ?r)))
	)
	(:action mount-waternozzle
		:parameters (?wp - waypoint ?r - robot ?wn - wateringnozzle)
		:precondition (and (waternozzle-at ?wn ?wp) (at ?r ?wp) (no-tools-mounted ?r))
		:effect (and (carrying-WateringNozzle ?wn) (not (no-tools-mounted ?r)))
	)
	(:action mount-weeder
		:parameters (?wp - waypoint ?r - robot ?wdr - weeder)
		:precondition (and (weeder-at ?wdr ?wp) (at ?r ?wp) (no-tools-mounted ?r))
		:effect (and (carrying-Weeder ?wdr) (not (no-tools-mounted ?r)))
	)
	(:action move
		:parameters (?r - robot ?wp1 - waypoint ?wp2 - waypoint)
		:precondition (at ?r ?wp1)
		:effect (and (not (at ?r ?wp1)) (at ?r ?wp2))
	)
	(:action take-data-after-water
		:parameters (?s - sample ?wp - waypoint ?r - robot ?ss - soilsensor)
		:precondition (and (is-in ?s ?wp) (at ?r ?wp) (carrying-SoilSensor ?ss) (samplewatered ?s))
		:effect (taken-data-after-water ?s)
	)
	(:action take-data-before-water
		:parameters (?s - sample ?wp - waypoint ?r - robot ?ss - soilsensor)
		:precondition (and (is-in ?s ?wp) (at ?r ?wp) (carrying-SoilSensor ?ss) (not (samplewatered ?s)))
		:effect (taken-data-before-water ?s)
	)
	(:action take-image
		:parameters (?r - robot ?s - sample ?wp - waypoint ?c - camera)
		:precondition (and (at ?r ?wp) (is-in ?s ?wp))
		:effect (taken-image ?s)
	)
)