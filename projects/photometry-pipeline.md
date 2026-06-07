---
layout: text-page
title: Photometry Pipeline
---

# photometry pipeline

During the summer of 2023 I worked alongside Juan Santisteban of the
University of St Andrews to develop a source identification and photometry
pipeline. The goal was to feed this pipeline a folder of astronomical
.fits images, have it identify all astronomical sources, then produce a
series of light curves from selected targets.

The most significant
challenges in this project stemmed from target tracking and ensuring
that the code would be able to reliably identify the same source
regardless of image transformation or rotation.

This pipeline will be used
to characterise the OPTICAM imaging system, then produce and analyse
photometric data from selected cataclysmic binary systems.

## Current status

The pipeline can now load all fits images from a specified directory,
identify sources within those images, and perform photometry on them
automatically. Most importantly, it can assign IDs to each star so that
they can be tracked across each image. This was achieved using the
AstroAlign library and by storing sequences of coordinates corresponding
to the positions of each star across the different images. As of now
AstroAlign itself is used to detect sources, but the issue we're currently
facing is that if it fails to detect the transform between two images then
we cannot assign the correct ID to stars in subsequent images.

It seems to be that if the list of coordinates passed into the find_transform
function is too short, AA exhausts the possible configurations in which
those sources could be matched to those in the subsequent image before
finding the correct transform.

This is the first successful lightcurve output from a series of one
thousand images.

![Light curve for GK Persei along with two reference stars at 4770 Angstroms](/static/images/MiscImages/lightcurve.png){: .content-image}

## Next steps

We now know that errors returned by AstroAlign from the find_transform
function are not due to issues with the fits images themselves, but with
the list of source coordinates passsed into that function. Once a method
has been found to correct this fault, the next step will be to implement a
function which determines the optimum aperture size for photometry. This
will require a curve of growth to be created for all stars, but should
only be required to run on the first image of the dataset.