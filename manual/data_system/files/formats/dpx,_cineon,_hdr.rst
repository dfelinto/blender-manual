
DPX and Cineon
**************

Cineon is Kodak's standard for film scanning, 10 bits/channel and logarithmic.
DPX has been derived from Cineon as the ANSI/SMPTE industry standard.
DPX supports 16 bits color/channel, linear as well as logarithmic.
DPX is currently a widely adopted standard used in the film hardware/software industry.

DPX as well as Cineon only stores and converts the "visible" color range of values between 0.0
and 1.0 (as result of rendering or composite). No alpha is written.

The code has been gratefully copied from CinePaint. According to CinePaint's main developer
Robin Rowe the DPX code defaults to logarithmic colorspace.
We cannot find yet how to disable this, but it seems to read/write fine without visible loss.

Blender DPX files (entire Elephants Dream movie)
have been succesfully imported in a Quantel IQ HD/2K finishing/grading set without problems,
so for now we assume it's compliant for professional usage.


Radiance HDR
************

Radiance is a suite of tools for lighting simulation originally written by Greg Ward.
Since Radiance had the first (and for a long time the only) HDR image format,
this format is supported by many other software packages.

Radiance (.hdr) files store colors still in 8 bits per component, but with an additional
(shared) 8 bits exponent value, making it 32 bits per pixel.
Only RGB can be stored in these files.

