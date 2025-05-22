# mlops
it's about creating a ml model and automating its execution, isolating it 

1-preparing environnement


ce dépot contient une pipeline de ml 
"Code -> codespace"
"install github codespace" -> if not already installed
"this is a test"

Install anaconda
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
bash Anaconda3-2022.05-Linux-x86_64.sh

Installer pyarrow pour lire des fichiers parquet

A chaque fois éteindre le codespace pour economiser l'utilisation
    CODE -> ... -> stop codespace

ML PIPELINE = load & prepare data -> Vectorize -> Train 
    charger les données
    vectorize consiste à transformer le dataframe en 
    entrainer le modèle
2- Ml model
 https://www.youtube.com/watch?v=iRunifGSHFc&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK
 https://github.com/DataTalksClub/mlops-zoomcamp/blob/main/01-intro/duration-prediction.ipynb
3- Mlops Automation levels:
    0: only ml model in a jupyter notebook
    1:Devops but no mlops 
        CICD
        Automated releases
        Unit & integration test
        ops metrics ( les métriques opérationnelles utilisées pour monitorer des modèles de machine learning en production.)
            Type	            Exemple
            Data Quality	    Missing values, schema drift
            Model Performance	Accuracy, RMSE, AUC, F1
            Drift Detection	    Data drift, concept drift
            Serving Metrics	    Latency, throughput
            Usage Metrics	    Number of predictions, requests/sec
            Resource Metrics	CPU/memory usage, GPU usage
    2- Automated training:
        Training pipeline
        Experiment tracking
        Model registry
        Low friction deployement
        Os work with engineers
    3- Automated deployement:
        it's easy to deploy model
        generaly the model is on ML plateform and called by API
        DATA PREP -> TRAIN MODEL -> DEPLOY MODEL
    4-Full automation mlops
4-Experiment Tracking:

                