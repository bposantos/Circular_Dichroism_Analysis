# circular_dicrhoism_spectra_deconvolution
Code for CD deconvolution into ellipticity

Ellipticity according to:
>Greenfield NJ. Using circular dichroism spectra to estimate protein secondary structure. 
>Nat Protoc. 2006;1(6):2876-2890. [doi:10.1038/nprot.2006.202](https://www.nature.com/articles/nprot.2006.202)

## Usage:
```
python3 deconvolution.py -f data.txt -p parameters.py
```
The data.txt file is the user file with CD data.

## Parameters.py

File to be modified according to the experiment conditions.

- **molecular_weight**: protein mass in daltons;

- **aa**: number of amino acids residues;

- **path_length**: cuvette path in mm;

- **molarity**: protein concentration in micromolar;
