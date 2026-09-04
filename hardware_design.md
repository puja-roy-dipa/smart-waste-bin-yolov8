# Hardware design concept

The publication describes a Raspberry Pi 4-based smart-bin concept with camera-based object detection, a physical sorting mechanism, and servos/actuators directing materials to three compartments.

- `electronic`, `glass`, `metal`, `paper`, and `plastic` map to recyclable.
- `organic` maps to compostable.
- An item not recognized as one of the six trained classes follows a non-recyclable, motion-based fallback mechanism after a delay.

This distinguishes detector output from physical-system routing: non-recyclable is not a detector class. Complete Raspberry Pi, GPIO, actuator, servo, or motion-detection control source code was not provided and is not included here. Pin assignments and control behavior therefore must not be inferred from this documentation.
