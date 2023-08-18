# Quick and dirty script to rank Aplhafold output files based on model confidence

## Usage
```shell
python rank_pickle_output.py path_to/ranking_debug.json
```

## Example Alphafold output before rank_pickle_output.py
```shell
.
├── features.pkl
├── msas
│   ├── bfd_uniref_hits.a3m
│   ├── mgnify_hits.sto
│   ├── pdb_hits.hhr
│   └── uniref90_hits.sto
├── ranked_0.pdb
├── ranked_1.pdb
├── ranked_2.pdb
├── ranked_3.pdb
├── ranked_4.pdb
├── ranking_debug.json
├── relaxed_model_3_pred_0.pdb
├── relax_metrics.json
├── result_model_1_pred_0.pkl
├── result_model_2_pred_0.pkl
├── result_model_3_pred_0.pkl
├── result_model_4_pred_0.pkl
├── result_model_5_pred_0.pkl
├── timings.json
├── unrelaxed_model_1_pred_0.pdb
├── unrelaxed_model_2_pred_0.pdb
├── unrelaxed_model_3_pred_0.pdb
├── unrelaxed_model_4_pred_0.pdb
└── unrelaxed_model_5_pred_0.pdb
```
## Example of running rank_pickle_output.py

```shell
Renamed 'result_model_3_pred_0.pkl' to 'ranked_0_results.pkl'
Renamed 'result_model_5_pred_0.pkl' to 'ranked_1_results.pkl'
Renamed 'result_model_4_pred_0.pkl' to 'ranked_2_results.pkl'
Renamed 'result_model_2_pred_0.pkl' to 'ranked_3_results.pkl'
Renamed 'result_model_1_pred_0.pkl' to 'ranked_4_results.pkl'
File renaming completed.
```
## Example Alphafold output after running rank_pickle_output.py
```shell
.
├── features.pkl
├── msas
│   ├── bfd_uniref_hits.a3m
│   ├── mgnify_hits.sto
│   ├── pdb_hits.hhr
│   └── uniref90_hits.sto
├── ranked_0.pdb
├── ranked_0_results.pkl
├── ranked_1.pdb
├── ranked_1_results.pkl
├── ranked_2.pdb
├── ranked_2_results.pkl
├── ranked_3.pdb
├── ranked_3_results.pkl
├── ranked_4.pdb
├── ranked_4_results.pkl
├── ranking_debug.json
├── relaxed_model_3_pred_0.pdb
├── relax_metrics.json
├── timings.json
├── unrelaxed_model_1_pred_0.pdb
├── unrelaxed_model_2_pred_0.pdb
├── unrelaxed_model_3_pred_0.pdb
├── unrelaxed_model_4_pred_0.pdb
└── unrelaxed_model_5_pred_0.pdb
```
