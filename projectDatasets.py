from collections import namedtuple
from pathlib import Path

# Dataset root directory
_DATASET_ROOT = Path('/content/drive/MyDrive/Colab Notebooks/BugLocalization/Dataset')

Dataset = namedtuple('Dataset', ['name', 'src', 'bug_repo', 'repo_url', 'features'])

# Source codes and bug repositories

aspectj = Dataset(
    'aspectj',
    _DATASET_ROOT / 'source files/org.aspectj-bug433351/',
    _DATASET_ROOT / 'bug reports/AspectJ.txt',
    "https://github.com/eclipse/org.aspectj/tree/bug433351.git",
    _DATASET_ROOT / 'features_aspectj.csv'
)

eclipse = Dataset(
    'eclipse',
    _DATASET_ROOT / 'source files/eclipse.platform.ui-johna-402445/',
    _DATASET_ROOT / 'bug reports/Eclipse_Platform_UI.txt',
    "https://github.com/eclipse/eclipse.platform.ui.git",
    _DATASET_ROOT / 'features_eclipse.csv'
)

swt = Dataset(
    'swt',
    _DATASET_ROOT / 'source files/eclipse.platform.swt-xulrunner-31/',
    _DATASET_ROOT / 'bug reports/SWT.txt',
    "https://github.com/eclipse/eclipse.platform.swt.git",
    _DATASET_ROOT / 'features_swt.csv'
)

tomcat = Dataset(
    'tomcat',
    _DATASET_ROOT / 'source files/tomcat-7.0.51',
    _DATASET_ROOT / 'bug reports/Tomcat.txt',
    "https://github.com/apache/tomcat.git",
    _DATASET_ROOT / 'features_tomcat.csv/'
)

birt = Dataset(
    'birt',
    _DATASET_ROOT / 'source files/birt-20140211-1400',
    _DATASET_ROOT / 'bug reports/Birt.txt',
    "https://github.com/apache/birt.git",
    _DATASET_ROOT / 'features_birt.csv'
)
