📓 Project Handbook for: XXXXX
===

> 📎 **This is the foundation project to begin work in the MIS lab.**

> 📦 Replace the XXXXX placeholders.

> 📦 Set a version so you can track changes outside the repository.

Version: **DRAFT**

> 📦 Please use the Markdown template below to provide your content details. Simply replace the placeholder text with your own information. **Delete** these instructions and everything you don't need for a release.
>
> **Instructions:**  
> 1. Replace any placeholder text with your own content.  
> 2. Delete content that does not apply to your project.
> 2. When ready, save your changes and submit your pull request or issue.

You can use the markdown blockquote snips to build highlighted information:

> 📦 A TODO package task you **need to replace** with content.

> 🚫 **This is a important information!**

> 📎 Some useful additional information.


## 📚 Content of this Handbook

*Describe in a short paragraph* **why** this handbook exists, **who** should read it and **what** to expect from it.

**Example:**
This handbook template provides a documentation base setup for lab projects and can be used by lab members to document their work and share that on github. It guides you in the writing of overview documentations and is not meant for in-depth technical work.

> 📎 A good description is short and doesn't waste the reader's time.


## 🗂 Table of Contents

> 📎 Headings with spaces are linked with a dash **-** instead of a space and is written in lowercase!

> 🚫 Add additional sections **only if this is benefical** for the reader!

1. [Project Profile](#project-profile)
    - [Repositories](#repositories)
    - [Brief project abstract](#brief-project-abstract)
    - [Data](#data)
2. [Overview](#overview)
    - [Code](#Code)
    - [Datasets](#datasets)
    - [Results](#results)
3. [Prerequisites](#prerequisites)
4. [Workflow](#workflow)


## Project Profile

**Name:** Handbook template

> 📦 Add the full name of your study work, research paper, etc.

**Short name:** hbtemp

> 📦 Add the abbreviated name of your study work, research paper, etc. Could be your repository name.

**Type:** Other

> 📦 Add Studienarbeit, Abschlussarbeit, Paper, Promotion or Other.

**Topic(s):** templates, handbook

> 📦 A list of keywords to the work.

**Project stakeholder(s):**

- **Research project manager:** Prof. Dr. Gunther Github
- **External project lead:** Carlos Esaber, Buhtig GmbH

> 📦 Add a list of all stakeholders of the project (internal, external).

**Time frame:** DD.MM.YYYY - DD.MM.YYYY

> 📦 Add a project time frame. When do you work on this project?


### Repositories

> 📦 Fork the github MIS template. This is the foundation of any work in the MIS lab.

MIS template: [https://github.com/kathlab/mis-template](https://github.com/kathlab/mis-template)

> 📦 Edit README.md in your repository and provide the base information.

> 📦 Provide a link (or multiple) to the sources of the project. Regular projects must use a private github repository, NDA projects use internal gitlab.

**Git repository:** https://github.com/kathlab/templates

> 🚫 **If you need more repositories**, just fork the template and start a new project.


### Brief project abstract

> 📦 A brief description of the research project. In most cases you can paste your paper abstract here.

> 🚫 A good abstract contains: 
> - A summary of the problem your project challenges
> - Research questions
> - Results
> - Future work


### Data

> 📦 Describe datasets, models, checkpoints and raw data that are too big for a git repository. Most often you provide them as compressed archive(s). You can provide a link to an open-access internet database.


**Datasets:**

* **European indigeneous ducks:** european_ducks.csv.xz
* **African indigeneous ducks:** african_ducks.csv.xz

**Models:**

* **Reduced classification model for inference:** reduced_nn.pt
* **Full classification model for further trianing:** full_nn.pt

**Raw Data:**

* **Mixed ducks jpg:** mixed_ducks.zip

**Results:**

* **metrics_history.csv:** [./logs/] A history of training metrics.

* **training.log:** [./logs/] Technical logs of the model training.

* **Training checkpoints:** [./checkpoints/] Training checkpoints.

* **Model files:** [./models/] Trained models.


## Overview

> 📦 Describe your complete work from an birds-eye-perpective that are mandatory to allow others to gain a basic (yet complete) idea of your project.

> 🚫 **Important** are code(s), parameters to run code, datasets and outputs.

### Code

**Model training:**
train_nn.py

Train NN image classificator model.

**Hyperparameter configuration:**
config.json

```
{
  "epochs": 10,
  "batch_size": 32,
  "learning_rate": 0.001,
  "optimizer": "adam",
  "loss_function": "cross_entropy"
}
```

### Datasets

> **Hint:** Images are base64 encoded in provided CSV!

**ducks_training.csv**
Image dataset of ducks for image classification training.

**ducks_validation.csv**
Image dataset of ducks to validate a trained model performance.

**ducks_evaluation.csv**
Image dataset of ducks and similar animals to evaluate a trained model.


### Results

**ducks_classification.pt:**
Trained pytorch2 model output file.

**metrics_history.csv**
History of the metrics during model training.

## Prerequisites

> 📦 Describe the requirements to run scripts.

> 🚫 What hardware is required, what programming languages? What are the system requirements (operating system, network, databases, etc.)?

**OS:** Linux x86_64 (Ubuntu 22.04)

**Language:** Python 3.12

**Disk space:** >80GiB

**RAM:** >=64GiB

**GPU:** NVIDIA A4000 16GiB

**CUDA:** 12.4


## Workflow

> 📦 Describe the project **workflow**. Where to begin? What to run? Anything that is important to get results.

Example: Prepare datasets

```
xz -d ./datasets/european_ducks_raw.txt.xz
python convert_datasets.py ./datasets/european_ducks_raw.txt ./datasets/european_ducks.csv
```

Example: Run model training

```
python train_nn.py config.json
```

Example: Model inference

```
python run_nn.py reduced_nn.pt datasets/raw/evaluation/image_0001.jpg
```
