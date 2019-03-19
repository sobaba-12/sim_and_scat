# Run locally

To run the interactive components of the resource locally rather than on the web, it is necessary to have Jupyter Notebooks installed.
The easiest way to get Jupyter Notebooks is to install the [Anaconda Python](https://www.anaconda.com/download/) package.
Once the Jupyter Notebooks in available on your computer it is necessary to clone the following GitHub repository; [github.com/pythoninchemistry/sim_and_scat](https://github.com/pythoninchemistry/sim_and_scat).
Having cloned the content the last thing before running is to ensure that you have all of the necessary Python packages installed.
This can be achieved by building the `conda environment` available in the [reprository](https://github.com/pythoninchemistry/sim_and_scat/blob/master/environment.yml), information about building an environment from a yaml file can be found in the [conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file). 

This will download and install the necessary packages for the resource.
Now that the computer is ready to run the course it can all be found, in order, in the `run_local` directory.

Please be aware that if you are running the resource locally, when the text references the "Interact" button at the top of the page, this may be ignored. 
This button is only present in the web interface to allow web users to launch a MyBinder Jupyter Notebook.
