# Processing circular dichroism data

## Deconvolution
Code for CD deconvolution into ellipticity

Ellipticity according to:
>Greenfield NJ. Using circular dichroism spectra to estimate protein secondary structure. 
>Nat Protoc. 2006;1(6):2876-2890. [doi:10.1038/nprot.2006.202](https://www.nature.com/articles/nprot.2006.202)

### Usage:
Modify these parameters in the notebook:

- **molecular_weight**: protein mass in daltons;

- **aa**: number of amino acids residues;

- **path_length**: cuvette path in mm;

- **molarity**: protein concentration in micromolar;

## Plotting
For plotting, there is a google colab notebook attached for CD spectra plotting associated with Savitzky–Golay filter smoothing (optional).
> Abraham. Savitzky and M. J. E. Golay
> Analytical Chemistry 1964 36 (8), 1627-1639
> DOI: [10.1021/ac60214a047](https://pubs.acs.org/doi/10.1021/ac60214a047)
