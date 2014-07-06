
Surface
*******

The surface shader defines the light interaction at the surface of the mesh. One or more
:abbr:`BSDF (Bidirectional scattering distribution function)` s specify if incoming light is
reflected back, refracted into the mesh, or absorbed.

Emission defines how light is emitted from the surface,
allowing any surface to become a light source.


Terminology
===========

- **BSDF** stands for bidirectional scattering distribution function. It defines how light is reflected and refracted at a surface.
- **Reflection**  :abbr:`BSDF (Bidirectional scattering distribution function)` s reflect an incoming ray on the same side of the surface.
- **Transmission**  :abbr:`BSDF (Bidirectional scattering distribution function)` s transmit an incoming ray through the surface, leaving on the other side.
- **Refraction**  :abbr:`BSDF (Bidirectional scattering distribution function)` s are a type of **Transmission**, transmitting an incoming ray and changing its direction as it exits on the other side of the surface.


BSDF Parameters
===============

A major difference from non-physically based renderers is that direct light reflection from
lamps and indirect light reflection of other surfaces are not decoupled, but rather handled
using a single :abbr:`BSDF (Bidirectional scattering distribution function)`.
This limits the possibilities a bit, but we believe overall it is helpful in creating
consistent-looking renders with fewer parameters to tune.

For glossy :abbr:`BSDF (Bidirectional scattering distribution function)` s,
**roughness** parameters control the sharpness of the reflection, from 0.0 (perfectly sharp)
to 1.0 (very soft). Compared to **hardness** or **exponent** parameters,
it has the advantage of being in the range 0.0..1.0,
and as a result gives more linear control and is more easily textureable.
The relation is roughly: *roughness = 1 - 1/hardness*