---
layout: text-page
title: Handwriting Decoder
---
# Handwriting decoder

While transcribing text for the Smithsonian Digital Volunteers project I often struggled to decipher older, handwritten entries.
Rather than learn 19th century handwriting conventions, I opted to create a python script that would fill in the blanks when only certain
letters were legible. This mini-project upon completion turned into an experiment into the mechanisms of predictive text.

The script works by taking a partially decoded word from the user, where uncertainties are represented by underscores. For example, if the
word was "underscore", but the letters e, r, and o were unclear, the user might enter "und__sc_re". A list of variations is then created
where each underscore is replace by a character representing either zero, one, or two unknown letters to allow for some margin of error
in the original guess. From there, we iterate over a dictionary list containing over 400K words to search for matches.
![Terminal output of handwriting decoder](/static/images/MiscImages/handwriting-decoder.png){:.content-image style="width: 100%;"}