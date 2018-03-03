# Gender-Classifier-Model-in-scikit-learn

## Basic Info
<p> A simple machine learning model that uses the scikit-learn machine learning library to train a decision tree on a small dataset relating to height, weight and shoe sizes of male and female and then predicting gender based on a set of body metrics. </p>

## What is a Decision Tree?
<p> A decision tree is a set of rules used to classify data into categories. It looks at variables in a dataset, determines which are most important, and then comes up with a tree of decisions which best partitions the data. The tree is created by splitting data up by variables and then counting to see how many are in each bucket after each split.</p>

<p>
 Trained using the following scikit-learn model:
<ol>
<li> DecisionTreeClassifier </li>
</ol>
</p>

## Instructions

<ol>
<li> Make sure that Python is installed and the path is properly configured. </li>
<li> Install the dependency using Conda package manager i,e open your command propmt and type in conda install scikit-learn. </li>
<li> Install the Git desktop client. </li>
<li> Clone the repository: git clone https://github.com/jimsonsulit/python-machine-learning-exercises</li>
<li> Navigate to the directory where you can find the Python file. </li>



scikit-learn
============

scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

The project was started in 2007 by David Cournapeau as a Google Summer
of Code project, and since then many volunteers have contributed. See
the `AUTHORS.rst <AUTHORS.rst>`_ file for a complete list of contributors.

It is currently maintained by a team of volunteers.

Website: http://scikit-learn.org


Installation
------------

Dependencies
~~~~~~~~~~~~

scikit-learn requires:

- Python (>= 2.7 or >= 3.4)
- NumPy (>= 1.8.2)
- SciPy (>= 0.13.3)

For running the examples Matplotlib >= 1.3.1 is required.

scikit-learn also uses CBLAS, the C interface to the Basic Linear Algebra
Subprograms library. scikit-learn comes with a reference implementation, but
the system CBLAS will be detected by the build system and used if present.
CBLAS exists in many implementations; see `Linear algebra libraries
<http://scikit-learn.org/stable/modules/computational_performance.html#linear-algebra-libraries>`_
for known issues.

User installation
~~~~~~~~~~~~~~~~~

If you already have a working installation of numpy and scipy,
the easiest way to install scikit-learn is using ``pip`` ::

    pip install -U scikit-learn

or ``conda``::

    conda install scikit-learn

The documentation includes more detailed `installation instructions <http://scikit-learn.org/stable/install.html>`_.


Setting up a development environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quick tutorial on how to go about setting up your environment to
contribute to scikit-learn: https://github.com/scikit-learn/scikit-learn/blob/master/CONTRIBUTING.md


Citation
~~~~~~~~

If you use scikit-learn in a scientific publication, we would appreciate citations: http://scikit-learn.org/stable/about.html#citing-scikit-learn
