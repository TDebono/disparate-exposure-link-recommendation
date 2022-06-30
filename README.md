# The Effect of Link Recommendation on Centrality and Groups' Visibility in Online Social Networks

*Author: [Timo Debono](https://www.linkedin.com/in/timo-debono/), M.Sc. Information Studies - Data Science Student at University of Amsterdam*

*Supervisor: [Fernando P. Santos](https://www.linkedin.com/in/fernando-p-santos-96aa9159/), Assistant Professor at University of Amsterdam*

This paper investigates the effect of the Stochastic Approach for Link-Structure Analysis (SALSA), a popular link recommendation algorithm, on network centrality and disparate exposure in bi-populated networks. Previous works have primarily used some notion of degree to identify exposure inequalities. It has been established, however, that degree may not be a fully accurate measure when evaluating how link recommendation impacts groups' visibility in a social context. Hence, we use three different centrality metrics that capture more granular information: betweenness (BC), closeness (CC), and eigenvector centrality (EVC). We find that CC and EVC offer different interpretations to the conclusions inferred from degree. In line with previous studies, we also find that exposure discrepancies are a function of in-group homophily. Lastly, we propose the concept of kn-Interventions to mitigate disparate exposure effects. Within the scope of this work, we only test one specific combination of parameters and hypothesize that the effectiveness thereof depends on the class composition of the recommendations produced by SALSA. Moreover, we find that the effectiveness of the considered intervention is conditional on the specific evaluation metric. Ultimately, our findings elucidate the need for more holistic methods when evaluating the effects of link recommendation in social contexts.

<!-- <figure>
  <img
  src="https://github.com/TDebono/disparate-exposure-link-recommendation/blob/78d4f392d275338f6bd94a1b21a452a89f333377/03_plots/03-01%20Network%20Viz/networks_plot2.png"
  alt="Networks plot">
  <figcaption>Plots (a) to (d) depict exemplary synthetic networks with $|V|=20$, $f_m=0.3$, and varying levels of homophily (minority nodes in blue, majority nodes in red). These networks show how the levels of homophily per group impact the edge formation process and, consequently, the network topology.</figcaption>
</figure> -->

<figure>
  <img
  src="https://github.com/TDebono/disparate-exposure-link-recommendation/blob/main/03_plots/03-02%20Results/results_final.png?raw=true"
  alt="Results plot">
  <figcaption>Average changes in % for centrality measures after the application of SALSA as a function of in-group homophily. The y-axis indicates the magnitude and direction of change over z=10 runs and the error bars specify the standard deviation over all runs. The x-axis shows the considered centrality measures.</figcaption>
</figure>

<!-- ![Average changes in % for centrality measures after the application of SALSA as a function of in-group homophily. The y-axis indicates the magnitude and direction of change over z=10 runs and the error bars specify the standard deviation over all runs. The x-axis shows the considered centrality measures.](https://github.com/TDebono/disparate-exposure-link-recommendation/blob/main/03_plots/03-02%20Results/results_final.png?raw=true) -->


## Quick links

- [Experiments](https://github.com/TDebono/disparate-exposure-link-recommendation/blob/0952f3dc4bac68125096dcda28a7a0a37903bed9/02_results/experiments.ipynb) - This notebook contains the code that was used to conduct all experiments
- [Synthetic Network Data](01_data/01-02%20Synthetic%20networks/) - This folder contains the files for all synthetically generated networks used for the experiments
- [Visualizations](03_plots/visualizations.ipynb) - This notebook contains the code that was used to generate all figures
