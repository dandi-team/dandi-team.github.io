.. dandi-team documentation master file, created by
   sphinx-quickstart on Wed Mar 18 14:08:03 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

DANDI team
==========

.. container:: index-paragraph

    The DANDI (*Domain Adaptation for Neural Data Integration*) team is a 
    joint initiative between Prof. `Bertrand Thirion`_ (INRIA) and 
    Prof. `Lune Bellec`_ (University of Montreal). 
    
    Sparse, noisy data significantly limits the potential of artificial intelligence 
    (AI) in health applications. 
    One promising approach is to leverage related data-rich systems through transfer learning; 
    for example, by pre-training models that can be fine-tuned for clinical settings. 
    Importantly, however, this approach can degrade performance if target applications have limited data.

    In DANDI, we aim to address this gap by developing novel transfer procedures, 
    building either on Optimal Transport theory or leveraging domain-specific data structure via
    e.g., graph convolutional networks.
    We develop these methods using functional magnetic resonance imaging (fMRI) datasets;
    in particular, leveraging the deep-phenotyping dataset `Courtois-NeuroMod`_, collected at
    the University of Montreal.

.. _Bertrand Thirion: https://pages.saclay.inria.fr/bertrand.thirion/

.. _Lune Bellec: https://psy.umontreal.ca/repertoire-departement/professeures/professeures/in/in19348/sg/Lune%20Bellec/

.. _Courtois-NeuroMod: https://www.cneuromod.ca/


Funding
-------

This work is generously supported as an Équipe Associée award from INRIA,
an international collaborative research project (PRCI) award from ANR and NSERC,
and a European Union - University of Montreal Partnership award.


.. list-table:: 
    :header-rows: 0
    :widths: 1 1

    * - .. figure:: images/inr_logo_rouge.svg
            :align: center
      - .. figure:: images/Universite_de_Montreal_logo.svg
            :align: center
    * - .. figure:: images/ANR-logo-2021-complet.svg
            :align: center
      - .. figure:: images/NSERC_RGB.svg
            :align: center