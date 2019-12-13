# Hurricane Loss Model

Hurricane loss model to estimate expected annual economic loss.

## Instructions
1. Clone the repository and cd into the root directory.
2. Build the python / linux container.
    ``` 
    docker build -t oasis-assignment .
    ```
3. Run the container's bash shell
    ```
    docker run -it oasis-assignment /bin/bash
    ```
4. Call the hurricane model.
   
   ```
    gethurricaneloss 0.4 0.5 0.6 0.7 --n100
   ```
5. For help on understanding the parameters, type the following command
   ```
    gethurricaneloss -h
   ```
    
    ```
    positional arguments:
    florida_landfall_rate Annual rate of land-falling hurricanes in Florida
    florida_mean          LogNormal parameter mean
    florida_stdev         LogNormal parameter std deviation
    gulf_landfall_rate    Annual rate of land-falling hurricanes in Gulf states
    
    optional arguments:
      --n N               Number of Monte Carlo Simulations
    ```
   
    ![gethurricaneloss](img/help.png?raw=true)
   
   
